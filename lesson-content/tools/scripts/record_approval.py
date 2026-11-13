#!/usr/bin/env python3
"""Registra una aprobación del maestro después del veredicto musical independiente."""
import argparse
import hashlib
import json
import re
from pathlib import Path

import audit_delivery
import curriculum as tools
import integrate


def read_review(path):
    text = path.read_text(encoding='utf-8')
    first_line = text.lstrip().splitlines()[0]
    if not re.search(r'^(?:verdict:?\s+)?approved\b', first_line.strip('* '), re.I):
        raise ValueError(f'Revisión no aprobada: {path}')
    issues = []
    blocks = re.findall(r'```json\s*(.*?)```', text, re.S)
    if not blocks:
        raise ValueError('La revisión necesita un array JSON de incidencias')
    for block in blocks:
        records = json.loads(block)
        if not isinstance(records, list):
            raise ValueError('El bloque de incidencias debe ser un array')
        for issue in records:
            if issue['status'] != 'resolved':
                raise ValueError(f'Incidencia pendiente: {issue["issueId"]}')
        issues.extend(records)

    return issues


def record_approval(category, batch, lesson_ids):
    root = tools.ROOT
    project = root.parent
    reports = root / 'audits'
    review = reports / category / f'batch-{batch:02}-review.md'
    issues = read_review(review)
    snapshot = root / 'drafts' / category / 'checks'
    integrate.assemble(root / 'approved', root / 'drafts', snapshot, 'batch', [category], True)
    errors, data = tools.validate(snapshot, 'batch')
    if errors:
        raise ValueError('\n'.join(errors))
    if any(not lesson.startswith(f'lesson-{category}-') for lesson in lesson_ids):
        raise ValueError('Lecciones fuera de la categoría solicitada')
    developed = {stage['lessonId'] for stage in data['stages']}
    if not set(lesson_ids) <= developed:
        raise ValueError('No todas las lecciones solicitadas están compuestas')
    metrics = audit_delivery.musical_metrics(data)
    physical = [finding for finding in metrics['findings']
                if finding['kind'] != 'identicalMidiNeedsPedagogicalJustification']
    if physical:
        raise ValueError(json.dumps(physical, ensure_ascii=False))

    register_path = reports / 'batch-register.json'
    register = json.loads(register_path.read_text(encoding='utf-8'))
    for previous in register:
        if set(previous['fingerprint']['lessonIds']) & set(lesson_ids):
            raise ValueError('Lección ya registrada como aprobada')
        if previous['category'] == category:
            current = audit_delivery.subset_fingerprint(data, previous['fingerprint']['lessonIds'])
            if current != previous['fingerprint']:
                raise ValueError('Una lección aprobada anteriormente fue alterada')
    freeze = json.loads((reports / 'contract-freeze.json').read_text(encoding='utf-8'))
    if not freeze['massProductionAuthorized']:
        raise ValueError('Piloto no autorizado')
    for filename, expected in {**freeze['sha256'], **freeze['pilotSha256']}.items():
        if hashlib.sha256((project / filename).read_bytes()).hexdigest() != expected:
            raise ValueError(f'Contrato congelado alterado: {filename}')

    midi = audit_delivery.audit_midi(data, reports / category / f'batch-{batch:02}-midi', 202603)
    entry = {'category': category, 'batch': batch, 'verdict': 'approved',
             'review': str(review.relative_to(project)),
             'reviewSha256': hashlib.sha256(review.read_bytes()).hexdigest(),
             'fingerprint': audit_delivery.subset_fingerprint(data, lesson_ids)}
    register.append(entry)
    issue_path = reports / 'issues.json'
    all_issues = {issue['issueId']: issue for issue in json.loads(issue_path.read_text(encoding='utf-8'))}
    all_issues.update({issue['issueId']: issue for issue in issues})
    technical_path = reports / 'batch-technical-checks.json'
    technical = json.loads(technical_path.read_text(encoding='utf-8'))
    technical[f'{category}-{batch:02}'] = {
        'technicalStatus': 'passed', 'masterStatus': 'approved-after-independent-review',
        'counts': {name: len(rows) for name, rows in data.items()},
        'metrics': metrics, 'midi': midi, 'approvedLessonIds': sorted(lesson_ids),
    }
    for path, payload in ((register_path, register), (issue_path, list(all_issues.values())),
                          (technical_path, technical)):
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return entry


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('category')
    parser.add_argument('batch', type=int)
    parser.add_argument('lesson_ids', nargs='+')
    args = parser.parse_args()
    try:
        entry = record_approval(args.category, args.batch, args.lesson_ids)
    except (ValueError, KeyError, OSError) as error:
        parser.exit(1, f'{error}\n')
    print(json.dumps(entry, ensure_ascii=False))


if __name__ == '__main__':
    main()
