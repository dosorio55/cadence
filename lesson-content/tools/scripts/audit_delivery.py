#!/usr/bin/env python3
"""Comprueba MIDI y SQL con muestras reproducibles y evidencia serializable."""
import argparse
import hashlib
import json
import random
import struct
import tempfile
from collections import defaultdict
from pathlib import Path

import curriculum as tools


def inspect_midi(path):
    raw = path.read_bytes()
    if raw[:4] != b'MThd' or len(raw) < 22:
        raise ValueError('Cabecera MIDI ausente o truncada')
    header_length, midi_format, tracks, ppq = struct.unpack('>IHHH', raw[4:14])
    if header_length != 6 or midi_format != 0 or tracks != 1 or ppq & 0x8000:
        raise ValueError('Se esperaba SMF formato 0 con PPQ')
    if raw[14:18] != b'MTrk':
        raise ValueError('Pista MIDI ausente')
    length = int.from_bytes(raw[18:22], 'big')
    track = raw[22:]
    if len(track) != length:
        raise ValueError('Longitud de pista incorrecta')

    cursor = 0
    tick = 0
    running_status = None
    active = {}
    notes = []
    tempos = []
    meters = []
    end_tick = None

    def take(count):
        nonlocal cursor
        if cursor + count > len(track):
            raise ValueError('Evento MIDI truncado')
        value = track[cursor:cursor + count]
        cursor += count
        return value

    def vlq():
        value = 0
        for _ in range(4):
            byte = take(1)[0]
            value = (value << 7) | (byte & 0x7f)
            if not byte & 0x80:
                return value
        raise ValueError('Delta MIDI demasiado largo')

    while cursor < len(track):
        tick += vlq()
        if track[cursor] & 0x80:
            status = take(1)[0]
        elif running_status is not None:
            status = running_status
        else:
            raise ValueError('Running status sin evento previo')

        if status == 0xff:
            running_status = None
            kind = take(1)[0]
            payload = take(vlq())
            if kind == 0x51:
                tempos.append((tick, int.from_bytes(payload, 'big')))
            elif kind == 0x58:
                meters.append((tick, payload[0], 2 ** payload[1]))
            elif kind == 0x2f:
                end_tick = tick
                if cursor != len(track):
                    raise ValueError('Datos después de end-of-track')
                break
            continue

        if status in (0xf0, 0xf7):
            running_status = None
            take(vlq())
            continue
        if not 0x80 <= status <= 0xef:
            raise ValueError(f'Status MIDI no soportado: {status}')

        running_status = status
        command = status & 0xf0
        payload = take(1 if command in (0xc0, 0xd0) else 2)
        if any(byte > 127 for byte in payload):
            raise ValueError('Byte de datos MIDI inválido')
        if command not in (0x80, 0x90):
            continue

        pitch, velocity = payload
        key = (status & 0x0f, pitch)
        if command == 0x90 and velocity:
            if key in active:
                raise ValueError(f'Notas MIDI solapadas en un mismo canal/altura: {key}')
            active[key] = (tick, velocity)
        else:
            if key not in active:
                raise ValueError(f'Note-off sin note-on: {key}')
            start, attack_velocity = active.pop(key)
            notes.append((start, tick, pitch, attack_velocity))

    if end_tick is None or active:
        raise ValueError('MIDI sin cierre completo de pista/notas')
    return {'ppq': ppq, 'tempos': tempos, 'meters': meters, 'endTick': end_tick, 'notes': sorted(notes)}


def audit_midi(data, samples_dir, seed):
    progression_map = {row['id']: row for row in data['progressions']}
    stages = {row['id']: row for row in data['stages']}
    lessons = {row['id']: row for row in data['lessons']}
    skills = {row['id']: row for row in data['skills']}
    by_category = defaultdict(list)
    by_progression = defaultdict(list)
    for note in data['note-events']:
        by_progression[note['progressionId']].append(note)
    for progression in data['progressions']:
        lesson = lessons[stages[progression['stageId']]['lessonId']]
        category = skills[lesson['primarySkillId']]['categoryId']
        by_category[category].append(progression['id'])

    selected = {sorted(ids)[0] for ids in by_category.values()}
    population = sorted(progression_map)
    selected.update(random.Random(seed).sample(population, min(12, len(population))))
    selected.update(pid for pid, progression in progression_map.items()
                    if stages[progression['stageId']]['lessonId'] == 'lesson-rhythm-004')
    samples_dir.mkdir(parents=True, exist_ok=True)
    evidence = []
    for pid in sorted(selected):
        progression = progression_map[pid]
        notes = by_progression[pid]
        output = samples_dir / f'{pid}.mid'
        tools.midi_file(progression, notes, output)
        parsed = inspect_midi(output)
        ppq = parsed['ppq']
        expected_notes = sorted((round(note['startBeat'] * ppq),
                                 round((note['startBeat'] + note['durationBeats']) * ppq),
                                 note['midi'], note['velocity']) for note in notes)
        meter = progression['timeSignature']
        expected_ticks = round(progression['totalBars'] * meter['numerator'] * 4 / meter['denominator'] * ppq)
        expected_tempo = round(60_000_000 / progression['bpm'])
        checks = (
            ppq == 960,
            parsed['notes'] == expected_notes,
            parsed['tempos'] == [(0, expected_tempo)],
            parsed['meters'] == [(0, meter['numerator'], meter['denominator'])],
            parsed['endTick'] == expected_ticks,
        )
        if not all(checks):
            raise ValueError(f'{pid}: MIDI no corresponde a los eventos/tempo/compás/duración')
        evidence.append({'progressionId': pid, 'file': str(output), 'notes': len(notes),
                         'ppq': ppq, 'totalTicks': expected_ticks, 'tempoMicroseconds': expected_tempo,
                         'sha256': hashlib.sha256(output.read_bytes()).hexdigest()})

    return {'seed': seed, 'sampleCount': len(evidence), 'categoriesCovered': sorted(by_category),
            'verification': 'Lectura binaria de notas, tempo, compás y cierre; no escucha humana.',
            'samples': evidence}


def subset_fingerprint(data, lesson_ids):
    lesson_ids = set(lesson_ids)
    stages = [row for row in data['stages'] if row['lessonId'] in lesson_ids]
    stage_ids = {row['id'] for row in stages}
    progressions = [row for row in data['progressions'] if row['stageId'] in stage_ids]
    progression_ids = {row['id'] for row in progressions}
    records = {
        'lessons': [row for row in data['lessons'] if row['id'] in lesson_ids],
        'stages': stages,
        'progressions': progressions,
        'chord-events': [row for row in data['chord-events'] if row['progressionId'] in progression_ids],
        'note-events': [row for row in data['note-events'] if row['progressionId'] in progression_ids],
    }
    canonical = {name: sorted(rows, key=lambda row: row['id']) for name, rows in records.items()}
    encoded = json.dumps(canonical, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()
    return {'lessonIds': sorted(lesson_ids), 'sha256': hashlib.sha256(encoded).hexdigest(),
            'counts': {name: len(rows) for name, rows in records.items()}}


def audit_approvals(data, reports_dir):
    freeze = json.loads((reports_dir / 'contract-freeze.json').read_text(encoding='utf-8'))
    if freeze['schemaVersion'] != tools.SCHEMA_VERSION or not freeze['massProductionAuthorized']:
        raise ValueError('Contrato o piloto sin aprobación de producción')
    project = tools.ROOT.parent
    for filename, expected in {**freeze['sha256'], **freeze['pilotSha256']}.items():
        if hashlib.sha256((project / filename).read_bytes()).hexdigest() != expected:
            raise ValueError(f'Contrato/diseño/piloto congelado alterado: {filename}')

    issues = json.loads((reports_dir / 'issues.json').read_text(encoding='utf-8'))
    for issue in issues:
        if issue['severity'] in ('blocker', 'major') and issue['status'] != 'resolved':
            raise ValueError(f'Incidencia pendiente de cierre: {issue["issueId"]}')

    register = json.loads((reports_dir / 'batch-register.json').read_text(encoding='utf-8'))
    covered = set()
    for approval in register:
        if approval['verdict'] != 'approved':
            raise ValueError(f'Lote sin aprobación: {approval["category"]}/{approval["batch"]}')
        fingerprint = approval['fingerprint']
        lesson_ids = set(fingerprint['lessonIds'])
        if covered & lesson_ids:
            raise ValueError('Lecciones duplicadas en el registro de aprobación')
        if subset_fingerprint(data, lesson_ids) != fingerprint:
            raise ValueError(f'Lote aprobado alterado: {approval["category"]}/{approval["batch"]}')
        review = project / approval['review']
        if hashlib.sha256(review.read_bytes()).hexdigest() != approval['reviewSha256']:
            raise ValueError(f'Revisión aprobada alterada: {review}')
        covered.update(lesson_ids)
    if covered != {lesson['id'] for lesson in data['lessons']}:
        raise ValueError('No todas las lecciones tienen revisión independiente aprobada')

    return {'approvedBatchesIncludingPilot': len(register), 'lessonsCovered': len(covered),
            'frozenContractAndPilot': 'unchanged', 'approvedRecordsAndReviews': 'unchanged'}


def musical_metrics(data):
    notes_by_progression = defaultdict(list)
    for note in data['note-events']:
        notes_by_progression[note['progressionId']].append(note)

    findings = []
    signatures = {}
    for progression in data['progressions']:
        pid = progression['id']
        notes = notes_by_progression[pid]
        signatures[pid] = sorted((note['midi'], round(note['startBeat'] * 960),
                                  round(note['durationBeats'] * 960), note['velocity'],
                                  note['hand'], note['role']) for note in notes)
        events = []
        for index, note in enumerate(notes):
            events.append((round(note['startBeat'] * 960), 1, index))
            events.append((round((note['startBeat'] + note['durationBeats']) * 960), 0, index))
        active = {}
        maxima = {hand: {'span': 0, 'notes': 0} for hand in ('left', 'right')}
        collisions = set()
        for tick, attack, index in sorted(events):
            if not attack:
                active.pop(index, None)
                continue
            note = notes[index]
            if any(other['midi'] == note['midi'] for other in active.values()):
                collisions.add((tick, note['midi']))
            active[index] = note
            for hand in maxima:
                pitches = [other['midi'] for other in active.values() if other['hand'] == hand]
                if pitches:
                    maxima[hand]['span'] = max(maxima[hand]['span'], max(pitches) - min(pitches))
                    maxima[hand]['notes'] = max(maxima[hand]['notes'], len(pitches))
        for hand, maximum in maxima.items():
            if maximum['span'] > 12 or maximum['notes'] > 5:
                findings.append({'progressionId': pid, 'kind': 'handReachReview',
                                 'hand': hand, 'maximumSemitones': maximum['span'],
                                 'maximumSimultaneousNotes': maximum['notes']})
        if collisions:
            findings.append({'progressionId': pid, 'kind': 'samePitchOverlap',
                             'positions': [{'tick': tick, 'midi': pitch} for tick, pitch in sorted(collisions)]})

    primaries = {row['stageId']: row['id'] for row in data['progressions'] if row['kind'] == 'primary'}
    stages_by_lesson = defaultdict(list)
    for stage in data['stages']:
        stages_by_lesson[stage['lessonId']].append(stage)
    for stages in stages_by_lesson.values():
        ordered = sorted(stages, key=lambda stage: stage['order'])
        for previous, current in zip(ordered, ordered[1:]):
            if signatures[primaries[previous['id']]] == signatures[primaries[current['id']]]:
                findings.append({'stageId': current['id'], 'previousStageId': previous['id'],
                                 'kind': 'identicalMidiNeedsPedagogicalJustification'})

    return {'progressionsAnalyzed': len(data['progressions']), 'findings': findings,
            'criterion': 'Alcance simultáneo > octava, más de cinco notas por mano, alturas solapadas y MIDI idéntico entre etapas requieren revisión contextual.'}


def audit_sql(directory, data):
    with tempfile.TemporaryDirectory(prefix='piano-lab-sql-') as temporary:
        database = Path(temporary) / 'curriculum.sqlite'
        connection = tools.import_sql(directory, database, 'global')
        first_dump = '\n'.join(connection.iterdump())
        counts = {}
        for name in tools.SCHEMA_NAMES:
            table = name.replace('-', '_')
            counts[table] = connection.execute(f'SELECT COUNT(*) FROM {table}').fetchone()[0]
            if counts[table] != len(data[name]):
                raise ValueError(f'SQL: conteo distinto en {table}')
        counts['lesson_prerequisites'] = connection.execute('SELECT COUNT(*) FROM lesson_prerequisites').fetchone()[0]
        expected_relations = sum(len(lesson['prerequisiteLessonIds']) for lesson in data['lessons'])
        if counts['lesson_prerequisites'] != expected_relations:
            raise ValueError('SQL: conteo incorrecto de prerrequisitos')

        for lesson in data['lessons']:
            actual = [row[0] for row in connection.execute(
                'SELECT prerequisite_lesson_id FROM lesson_prerequisites WHERE lesson_id=? ORDER BY sort_order',
                (lesson['id'],))]
            if actual != lesson['prerequisiteLessonIds']:
                raise ValueError(f'SQL: relaciones u orden de prerrequisitos alterados en {lesson["id"]}')

        for name, order_field in (('categories', 'order'), ('skills', 'order'),
                                  ('lessons', 'orderInCategory'), ('stages', 'order'),
                                  ('progressions', 'order'), ('chord-events', 'order')):
            table = name.replace('-', '_')
            column = 'order_in_category' if name == 'lessons' else 'sort_order'
            actual = dict(connection.execute(f'SELECT id,{column} FROM {table}'))
            if actual != {row['id']: row[order_field] for row in data[name]}:
                raise ValueError(f'SQL: orden alterado en {table}')

        for name in ('chord-events', 'note-events'):
            table = name.replace('-', '_')
            rows = {row[0]: row[1:] for row in connection.execute(f'SELECT id,progression_id,start_beat,duration_beats FROM {table}')}
            for event in data[name]:
                if rows[event['id']] != (event['progressionId'], event['startBeat'], event['durationBeats']):
                    raise ValueError(f'SQL: precisión temporal o referencia perdida en {event["id"]}')
        if connection.execute('PRAGMA foreign_key_check').fetchall():
            raise ValueError('SQL: referencias huérfanas')
        if connection.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
            raise ValueError('SQL: integrity_check falló')
        connection.close()

        connection = tools.import_sql(directory, database, 'global')
        second_dump = '\n'.join(connection.iterdump())
        connection.close()
        if first_dump != second_dump:
            raise ValueError('SQL: segunda importación cambia el contenido')

    return {'counts': counts, 'emptyImport': 'passed', 'secondImportIdentical': True,
            'foreignKeyCheck': 'passed', 'integrityCheck': 'passed', 'eventTimingAndReferences': 'passed',
            'prerequisiteRelationsAndOrder': 'passed', 'presentationOrder': 'passed',
            'dumpSha256': hashlib.sha256(first_dump.encode()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=tools.ROOT / 'approved')
    parser.add_argument('--samples-dir', type=Path, default=tools.ROOT / 'examples' / 'audited-midi')
    parser.add_argument('--output', type=Path, default=tools.ROOT / 'audits' / 'delivery-checks.json')
    parser.add_argument('--seed', type=int, default=202603)
    args = parser.parse_args()
    try:
        errors, data = tools.validate(args.data, 'global')
        if errors:
            raise ValueError('\n'.join(errors))
        report = {'schemaVersion': tools.SCHEMA_VERSION,
                  'counts': {name: len(rows) for name, rows in data.items()},
                  'midi': audit_midi(data, args.samples_dir, args.seed),
                  'musicalMetrics': musical_metrics(data),
                  'approvals': audit_approvals(data, tools.ROOT / 'audits'),
                  'sql': audit_sql(args.data, data)}
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    except (ValueError, OSError, KeyError) as error:
        parser.exit(1, f'{error}\n')

    print(args.output)


if __name__ == '__main__':
    main()
