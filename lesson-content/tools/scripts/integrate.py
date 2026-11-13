#!/usr/bin/env python3
"""Integra particiones sin cambiar el diseño pedagógico aprobado."""
import argparse
import json
import tempfile
from pathlib import Path

import curriculum as tools


DESIGN = ('categories', 'skills', 'lessons')
CONTENT = ('stages', 'progressions', 'chord-events', 'note-events')


def read_array(path):
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f'{path}: clave duplicada {key}')
            result[key] = value
        return result

    def finite_constant(value):
        raise ValueError(f'{path}: constante JSON inválida {value}')

    records = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=unique_keys,
                         parse_constant=finite_constant)
    if not isinstance(records, list):
        raise ValueError(f'{path}: se esperaba un array')

    return records


def collect(design_dir, work_dir, categories=None, complete=False):
    data = {name: read_array(design_dir / f'{name}.json') for name in DESIGN}
    data.update({name: [] for name in CONTENT})
    category_ids = {row['slug']: row['id'] for row in data['categories']}
    skills = {row['id']: row for row in data['skills']}
    lessons = {row['id']: row for row in data['lessons']}
    selected = list(categories) if categories else list(category_ids)
    unknown = set(selected) - category_ids.keys()
    if unknown:
        raise ValueError(f'Categorías desconocidas: {sorted(unknown)}')

    collected_lessons = set()
    seen = {name: set() for name in CONTENT}
    for slug in selected:
        partition = work_dir / slug
        if not partition.is_dir():
            if complete or categories:
                raise ValueError(f'Falta partición: {partition}')
            continue

        owned = read_array(partition / 'lessons.json')
        owned_ids = set()
        for lesson in owned:
            lesson_id = lesson['id']
            if lesson_id in collected_lessons:
                raise ValueError(f'Lección repetida: {lesson_id}')
            if lesson_id not in lessons or lesson != lessons[lesson_id]:
                raise ValueError(f'Diseño alterado: {lesson_id}')
            if skills[lesson['primarySkillId']]['categoryId'] != category_ids[slug]:
                raise ValueError(f'Lección fuera de su categoría: {lesson_id}')

            collected_lessons.add(lesson_id)
            owned_ids.add(lesson_id)

        partition_data = {name: read_array(partition / f'{name}.json') for name in CONTENT}
        stage_ids = {row['id'] for row in partition_data['stages']}
        progression_ids = {row['id'] for row in partition_data['progressions']}
        developed = {row['lessonId'] for row in partition_data['stages']}
        if developed != owned_ids:
            raise ValueError(f'{slug}: las etapas no cubren exactamente sus lecciones')

        for row in partition_data['progressions']:
            if row['stageId'] not in stage_ids:
                raise ValueError(f'{slug}: progresión enlazada fuera de la partición')

        for name in ('chord-events', 'note-events'):
            if any(row['progressionId'] not in progression_ids for row in partition_data[name]):
                raise ValueError(f'{slug}: {name} enlazados fuera de la partición')

        for name, rows in partition_data.items():
            for row in rows:
                if row['id'] in seen[name]:
                    raise ValueError(f'{name}: ID repetido {row["id"]}')
                seen[name].add(row['id'])

            data[name].extend(rows)

    if not collected_lessons:
        raise ValueError('No hay lecciones desarrolladas para integrar')

    if complete and collected_lessons != lessons.keys():
        missing = sorted(lessons.keys() - collected_lessons)
        raise ValueError(f'Lecciones sin partición: {missing}')

    return data


def write_data(data, output):
    output.mkdir(parents=True, exist_ok=True)
    for name, rows in data.items():
        path = output / f'{name}.json'
        pending = path.with_suffix('.json.tmp')
        pending.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        pending.replace(path)


def assemble(design_dir, work_dir, output, mode, categories=None, check=False):
    data = collect(design_dir, work_dir, categories, complete=mode == 'global')
    with tempfile.TemporaryDirectory(prefix='piano-lab-integrate-') as temporary:
        snapshot = Path(temporary)
        write_data(data, snapshot)
        errors, _ = tools.validate(snapshot, mode)
        if errors:
            raise ValueError('\n'.join(str(error) for error in errors))

    if check:
        for name, rows in data.items():
            existing = read_array(output / f'{name}.json')
            expected = sorted(rows, key=lambda row: row['id'])
            if sorted(existing, key=lambda row: row['id']) != expected:
                raise ValueError(f'{name}: consolidado distinto de la unión de particiones')
    else:
        content = data
        if output.resolve() == design_dir.resolve():
            content = {name: data[name] for name in CONTENT}

        write_data(content, output)

    return {name: len(rows) for name, rows in data.items()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--design', type=Path, default=tools.ROOT / 'approved')
    parser.add_argument('--work', type=Path, default=tools.ROOT / 'drafts')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--mode', choices=('pilot', 'batch', 'global'), required=True)
    parser.add_argument('--category', action='append')
    parser.add_argument('--check', action='store_true', help='Comprueba la unión sin escribir')
    args = parser.parse_args()
    try:
        counts = assemble(args.design, args.work, args.output, args.mode, args.category, args.check)
    except (ValueError, KeyError, OSError) as error:
        parser.exit(1, f'{error}\n')

    print(json.dumps({'mode': args.mode, 'counts': counts, 'unionVerified': args.check}, ensure_ascii=False))


if __name__ == '__main__':
    main()
