#!/usr/bin/env python3
"""Valida el contrato Piano Lab y exporta/importa progresiones."""

import argparse
import json
import math
import re
import sqlite3
import struct
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_NAMES = (
    'categories', 'skills', 'lessons', 'stages', 'progressions',
    'chord-events', 'note-events',
)
SCHEMA_VERSION = '1.0.0'


def schema_specs():
    text = {'type': 'string', 'minLength': 1}
    identifier = {'type': 'string', 'pattern': '^[A-Za-z0-9][A-Za-z0-9_-]*$'}
    positive = {'type': 'integer', 'minimum': 1}

    def record(properties, required):
        return {
            'type': 'object',
            'properties': properties,
            'required': required,
            'additionalProperties': False,
        }

    definitions = {
        'categories': record({
            'id': identifier, 'slug': text, 'name': text,
            'description': text, 'order': positive,
        }, ['id', 'slug', 'name', 'description', 'order']),
        'skills': record({
            'id': identifier, 'categoryId': identifier, 'name': text,
            'description': text, 'order': positive,
        }, ['id', 'categoryId', 'name', 'description', 'order']),
        'lessons': record({
            'id': identifier, 'primarySkillId': identifier,
            'orderInCategory': positive, 'title': text,
            'difficulty': {'type': 'integer', 'minimum': 1, 'maximum': 5},
            'goal': text, 'introMd': text,
            'prerequisiteLessonIds': {
                'type': 'array', 'items': identifier, 'uniqueItems': True,
            },
            'targetMinutes': positive,
            'styleTags': {'type': 'array', 'items': text, 'minItems': 1, 'uniqueItems': True},
        }, ['id', 'primarySkillId', 'orderInCategory', 'title', 'difficulty',
            'goal', 'introMd', 'prerequisiteLessonIds', 'targetMinutes', 'styleTags']),
        'stages': record({
            'id': identifier, 'lessonId': identifier, 'order': positive,
            'title': text, 'explanationMd': text, 'task': text,
            'changeFromPrevious': text,
            'successCriteria': {'type': 'array', 'items': text, 'minItems': 1},
            'simplifyHint': text, 'extendHint': text,
        }, ['id', 'lessonId', 'order', 'title', 'explanationMd', 'task',
            'changeFromPrevious', 'successCriteria']),
        'progressions': record({
            'id': identifier, 'stageId': identifier,
            'kind': {'type': 'string', 'enum': ['primary', 'alternative', 'simplified', 'advanced']},
            'order': positive, 'title': text,
            'keyTonic': {'type': 'string', 'enum': ['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B']},
            'keyMode': {'type': 'string', 'enum': ['major', 'minor']},
            'style': text, 'bpm': {'type': 'number', 'exclusiveMinimum': 0},
            'timeSignature': record({
                'numerator': positive,
                'denominator': {'type': 'integer', 'enum': [2, 4, 8, 16]},
            }, ['numerator', 'denominator']),
            'totalBars': positive, 'description': text,
            'loopable': {'type': 'boolean'},
        }, ['id', 'stageId', 'kind', 'order', 'title', 'keyTonic', 'keyMode',
            'style', 'bpm', 'timeSignature', 'totalBars', 'description', 'loopable']),
        'chord-events': record({
            'id': identifier, 'progressionId': identifier, 'order': positive,
            'symbol': text, 'function': text,
            'startBeat': {'type': 'number', 'minimum': 0},
            'durationBeats': {'type': 'number', 'exclusiveMinimum': 0},
        }, ['id', 'progressionId', 'order', 'symbol', 'function', 'startBeat', 'durationBeats']),
        'note-events': record({
            'id': identifier, 'progressionId': identifier,
            'midi': {'type': 'integer', 'minimum': 0, 'maximum': 127},
            'startBeat': {'type': 'number', 'minimum': 0},
            'durationBeats': {'type': 'number', 'exclusiveMinimum': 0},
            'velocity': {'type': 'integer', 'minimum': 1, 'maximum': 127},
            'role': {'type': 'string', 'enum': ['bass', 'harmony', 'melody', 'ornament']},
            'hand': {'type': 'string', 'enum': ['left', 'right', 'either']},
        }, ['id', 'progressionId', 'midi', 'startBeat', 'durationBeats', 'velocity', 'role', 'hand']),
    }
    return {
        name: {
            '$schema': 'https://json-schema.org/draft/2020-12/schema',
            'type': 'array',
            'items': definition,
        }
        for name, definition in definitions.items()
    }


def make_schemas():
    """Write canonical array schemas; runtime validation reads these files."""
    for name, schema in schema_specs().items():
        path = ROOT / 'schemas' / f'{name}.schema.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(schema, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def check_schema_version():
    readme = ROOT / 'README.md'
    text = readme.read_text(encoding='utf-8')
    versions = re.findall(r'\*\*schemaVersion: ([^*]+)\*\*', text)
    if versions != [SCHEMA_VERSION]:
        raise ValueError(f'README debe declarar una sola schemaVersion: {SCHEMA_VERSION}')


def load_data(directory, mode=None):
    def reject_duplicate_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f'clave JSON duplicada: {key}')
            result[key] = value
        return result

    def reject_non_finite(value):
        raise ValueError(f'constante JSON no válida: {value}')

    data = {name: [] for name in SCHEMA_NAMES}
    names = SCHEMA_NAMES[:3] if mode == 'design' else SCHEMA_NAMES
    for name in names:
        path = directory / f'{name}.json'
        if path.exists():
            data[name] = json.loads(
                path.read_text(encoding='utf-8'),
                object_pairs_hook=reject_duplicate_keys,
                parse_constant=reject_non_finite,
            )
        else:
            data[name] = []
        if not isinstance(data[name], list):
            raise ValueError(f'{path}: se esperaba un array JSON')
    return data


def validate(directory, mode):
    try:
        import jsonschema
    except ImportError as exc:
        raise RuntimeError('Falta jsonschema; instala con lesson-content/.venv/bin/python -m pip install -r lesson-content/tools/requirements.txt desde la raíz del proyecto') from exc

    check_schema_version()
    data = load_data(directory, mode)
    errors = []
    validators = {}
    schema_names = SCHEMA_NAMES[:3] if mode == 'design' else SCHEMA_NAMES
    for name in schema_names:
        schema_path = ROOT / 'schemas' / f'{name}.schema.json'
        schema = json.loads(schema_path.read_text(encoding='utf-8'))
        validators[name] = jsonschema.Draft202012Validator(schema)
        for error in validators[name].iter_errors(data[name]):
            errors.append(f'{name}{list(error.path)}: {error.message}')
    if errors:
        return errors, data

    entities = dict(zip(SCHEMA_NAMES, data.values()))
    maps = {name: {row['id']: row for row in rows} for name, rows in entities.items()}
    for name, rows in entities.items():
        if len(maps[name]) != len(rows):
            errors.append(f'{name}: IDs duplicados')

    categories = maps['categories']
    category_orders = [category['order'] for category in entities['categories']]
    if len(category_orders) != len(set(category_orders)):
        errors.append('categories: order duplicado')
    if category_orders and sorted(category_orders) != list(range(1, len(category_orders) + 1)):
        errors.append('categories: order debe ser correlativo desde 1')
    slugs = [category['slug'] for category in entities['categories']]
    if len(slugs) != len(set(slugs)):
        errors.append('categories: slug duplicado')
    skills = maps['skills']
    lessons = maps['lessons']
    stages = maps['stages']
    progressions = maps['progressions']

    if mode != 'design' and len(categories) != 6:
        errors.append(f'{mode} requiere 6 categorías (hay {len(categories)})')
    skills_by_category = defaultdict(list)
    lessons_by_category = defaultdict(list)
    for skill in entities['skills']:
        category_id = skill['categoryId']
        if category_id not in categories:
            errors.append(f"skill {skill['id']}: categoryId inexistente")
        else:
            skills_by_category[category_id].append(skill)
    for category in entities['categories']:
        ordered = sorted(skill['order'] for skill in skills_by_category[category['id']])
        if ordered != list(range(1, len(ordered) + 1)):
            errors.append(f"{category['id']}: orden de skills debe ser correlativo desde 1")
        if mode != 'design' and not 4 <= len(ordered) <= 6:
            errors.append(f"{category['id']}: {mode} requiere 4-6 skills (hay {len(ordered)})")

    for lesson in entities['lessons']:
        skill = skills.get(lesson['primarySkillId'])
        if skill is None:
            errors.append(f"lesson {lesson['id']}: primarySkillId inexistente")
            continue
        lessons_by_category[skill['categoryId']].append(lesson)
        for prerequisite in lesson['prerequisiteLessonIds']:
            if prerequisite not in lessons:
                errors.append(f"lesson {lesson['id']}: prerequisite {prerequisite} inexistente")

    for category in entities['categories']:
        ordered = sorted(lesson['orderInCategory'] for lesson in lessons_by_category[category['id']])
        if len(ordered) != len(set(ordered)):
            errors.append(f"{category['id']}: orderInCategory duplicado")
        if mode != 'design' and ordered != list(range(1, 16)):
            errors.append(f"{category['id']}: {mode} requiere 15 lessons ordenadas 1-15 (hay {len(ordered)})")

    prerequisites = {lesson['id']: lesson['prerequisiteLessonIds'] for lesson in entities['lessons']}
    visiting, visited = set(), set()

    def visit(lesson_id):
        if lesson_id in visiting:
            errors.append(f'ciclo de prerrequisitos en {lesson_id}')
            return
        if lesson_id in visited:
            return
        visiting.add(lesson_id)
        for prerequisite in prerequisites.get(lesson_id, []):
            if prerequisite in prerequisites:
                visit(prerequisite)
        visiting.remove(lesson_id)
        visited.add(lesson_id)

    for lesson_id in prerequisites:
        visit(lesson_id)

    stages_by_lesson = defaultdict(list)
    for stage in entities['stages']:
        if stage['lessonId'] not in lessons:
            errors.append(f"stage {stage['id']}: lesson inexistente")
        stages_by_lesson[stage['lessonId']].append(stage)

    # Global coverage checks all 90 lessons, including those with zero stages.
    coverage_lessons = [lesson['id'] for lesson in entities['lessons']] if mode == 'global' else list(stages_by_lesson)
    for lesson_id in coverage_lessons:
        lesson_stages = sorted(stages_by_lesson[lesson_id], key=lambda stage: stage['order'])
        orders = [stage['order'] for stage in lesson_stages]
        if not 3 <= len(orders) <= 6:
            errors.append(f'{lesson_id}: requiere 3-6 stages (hay {len(orders)})')
        if orders != list(range(1, len(orders) + 1)):
            errors.append(f'{lesson_id}: orden de stages debe ser correlativo desde 1')
        if len(orders) in (3, 6):
            intro = lessons[lesson_id]['introMd'].lower()
            justifications = ('porque', 'criterio', 'justifica', 'justificación', 'debido', 'razón')
            if not any(word in intro for word in justifications):
                errors.append(f'{lesson_id}: 3/6 stages requiere justificación textual en introMd')

    progressions_by_stage = defaultdict(list)
    for progression in entities['progressions']:
        if progression['stageId'] not in stages:
            errors.append(f"progression {progression['id']}: stageId inexistente")
        progressions_by_stage[progression['stageId']].append(progression)
    for stage in entities['stages']:
        primaries = [p for p in progressions_by_stage[stage['id']] if p['kind'] == 'primary']
        if len(primaries) != 1:
            errors.append(f"stage {stage['id']}: requiere exactamente una primary")
    for stage_id, related in progressions_by_stage.items():
        for kind in {p['kind'] for p in related}:
            orders = sorted(p['order'] for p in related if p['kind'] == kind)
            if orders != list(range(1, len(orders) + 1)):
                errors.append(f'{stage_id}/{kind}: order debe ser correlativo desde 1')

    chord_events = defaultdict(list)
    note_events = defaultdict(list)
    chord_orders = defaultdict(list)
    for event in entities['chord-events']:
        if event['progressionId'] not in progressions:
            errors.append(f"chord {event['id']}: progressionId inexistente")
        else:
            chord_events[event['progressionId']].append(event)
            chord_orders[event['progressionId']].append(event['order'])
    for progression_id, orders in chord_orders.items():
        if sorted(orders) != list(range(1, len(orders) + 1)):
            errors.append(f'{progression_id}: order de chord-events debe ser correlativo desde 1')
        ordered_by_order = sorted(chord_events[progression_id], key=lambda event: event['order'])
        if ordered_by_order != sorted(ordered_by_order, key=lambda event: event['startBeat']):
            errors.append(f'{progression_id}: order de chord-events no concuerda con cronología')
    for event in entities['note-events']:
        if event['progressionId'] not in progressions:
            errors.append(f"note {event['id']}: progressionId inexistente")
        else:
            note_events[event['progressionId']].append(event)

    for progression in entities['progressions']:
        pid = progression['id']
        meter = progression['timeSignature']
        total_beats = progression['totalBars'] * meter['numerator'] * 4 / meter['denominator']
        if not 40 <= progression['bpm'] <= 180:
            errors.append(f'{pid}: bpm fuera de rango 40-180')
        chords = chord_events[pid]
        notes = note_events[pid]
        if not chords:
            errors.append(f'{pid}: sin chord events')
        if not notes:
            errors.append(f'{pid}: sin note events')
        ordered_chords = sorted(chords, key=lambda event: event['startBeat'])
        for index, event in enumerate(ordered_chords):
            start = event['startBeat']
            end = start + event['durationBeats']
            if end > total_beats + 1e-7:
                errors.append(f"{pid}/{event['id']}: acorde fuera del loop")
            if index and start < ordered_chords[index - 1]['startBeat'] + ordered_chords[index - 1]['durationBeats'] - 1e-7:
                errors.append(f'{pid}: acordes solapados')
            if index and start > ordered_chords[index - 1]['startBeat'] + ordered_chords[index - 1]['durationBeats'] + 1e-7:
                errors.append(f'{pid}: hueco en cobertura de acordes')
        if ordered_chords and ordered_chords[0]['startBeat'] > 1e-7:
            errors.append(f'{pid}: cobertura de acordes no empieza en beat 0')
        if ordered_chords and abs(ordered_chords[-1]['startBeat'] + ordered_chords[-1]['durationBeats'] - total_beats) > 1e-7:
            errors.append(f'{pid}: cobertura de acordes no alcanza el final del loop')
        seen_attacks = set()
        for event in chords + notes:
            for value in (event['startBeat'], event['durationBeats']):
                on_quarter_grid = abs(value * 4 - round(value * 4)) <= 1e-7
                on_triplet_grid = abs(value * 3 - round(value * 3)) <= 1e-7
                if not (on_quarter_grid or on_triplet_grid):
                    errors.append(f"{pid}/{event['id']}: beat no representable en grid 0.25/1/3")
            if event['startBeat'] + event['durationBeats'] > total_beats + 1e-7:
                errors.append(f"{pid}/{event['id']}: evento fuera del loop")
        for note in notes:
            attack = (note['midi'], note['startBeat'], note['role'])
            if attack in seen_attacks:
                errors.append(f'{pid}: ataque duplicado {attack}')
            seen_attacks.add(attack)
            if not 21 <= note['midi'] <= 108:
                print(f'ADVERTENCIA rango piano {pid}: midi {note["midi"]}', file=sys.stderr)
            if note['hand'] == 'left' and note['midi'] > 72:
                print(f'ADVERTENCIA tocabilidad mano izquierda {pid}: midi {note["midi"]}', file=sys.stderr)
            if note['hand'] == 'right' and note['midi'] < 48:
                print(f'ADVERTENCIA tocabilidad mano derecha {pid}: midi {note["midi"]}', file=sys.stderr)

    return errors, data


def midi_file(progression, notes, output):
    ppq = 960
    meter = progression['timeSignature']
    total_ticks = round(progression['totalBars'] * meter['numerator'] * 4 / meter['denominator'] * ppq)
    tempo = round(60_000_000 / progression['bpm'])

    def vlq(value):
        value = max(0, int(value))
        encoded = [value & 0x7f]
        value >>= 7
        while value:
            encoded.insert(0, (value & 0x7f) | 0x80)
            value >>= 7
        return bytes(encoded)

    events = [
        (0, b'\xff\x51\x03' + tempo.to_bytes(3, 'big')),
        (0, b'\xff\x58\x04' + bytes([int(meter['numerator']), int(math.log2(meter['denominator'])), 24, 8])),
    ]
    for note in notes:
        start = round(note['startBeat'] * ppq)
        end = round((note['startBeat'] + note['durationBeats']) * ppq)
        events.extend([
            (start, bytes([0x90, int(note['midi']), int(note['velocity'])])),
            (end, bytes([0x80, int(note['midi']), 0])),
        ])
    events.sort(key=lambda event: (event[0], event[1][0] == 0x90))
    track = bytearray()
    previous_tick = 0
    for tick, message in events:
        track.extend(vlq(tick - previous_tick))
        track.extend(message)
        previous_tick = tick
    track.extend(vlq(max(0, total_ticks - previous_tick)))
    track.extend(b'\xff\x2f\x00')
    body = b'MThd' + struct.pack('>IHHH', 6, 0, 1, ppq)
    body += b'MTrk' + struct.pack('>I', len(track)) + track
    Path(output).write_bytes(body)


def init_db(conn):
    statements = [
        '''CREATE TABLE IF NOT EXISTS categories (
            id TEXT PRIMARY KEY,
            slug TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            sort_order INTEGER NOT NULL UNIQUE
        )''',
        '''CREATE TABLE IF NOT EXISTS skills (
            id TEXT PRIMARY KEY,
            category_id TEXT NOT NULL REFERENCES categories(id),
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            sort_order INTEGER NOT NULL,
            UNIQUE(category_id, sort_order)
        )''',
        '''CREATE TABLE IF NOT EXISTS lessons (
            id TEXT PRIMARY KEY,
            primary_skill_id TEXT NOT NULL REFERENCES skills(id),
            order_in_category INTEGER NOT NULL,
            title TEXT NOT NULL,
            difficulty INTEGER NOT NULL,
            goal TEXT NOT NULL,
            intro_md TEXT NOT NULL,
            target_minutes INTEGER NOT NULL,
            style_tags TEXT NOT NULL
        )''',
        '''CREATE TABLE IF NOT EXISTS lesson_prerequisites (
            lesson_id TEXT NOT NULL REFERENCES lessons(id) ON DELETE CASCADE,
            prerequisite_lesson_id TEXT NOT NULL REFERENCES lessons(id),
            sort_order INTEGER NOT NULL,
            PRIMARY KEY(lesson_id, prerequisite_lesson_id),
            UNIQUE(lesson_id, sort_order)
        )''',
        '''CREATE TABLE IF NOT EXISTS stages (
            id TEXT PRIMARY KEY,
            lesson_id TEXT NOT NULL REFERENCES lessons(id),
            sort_order INTEGER NOT NULL,
            title TEXT NOT NULL,
            explanation_md TEXT NOT NULL,
            task TEXT NOT NULL,
            change_from_previous TEXT NOT NULL,
            success_criteria TEXT NOT NULL,
            simplify_hint TEXT,
            extend_hint TEXT,
            UNIQUE(lesson_id, sort_order)
        )''',
        '''CREATE TABLE IF NOT EXISTS progressions (
            id TEXT PRIMARY KEY,
            stage_id TEXT NOT NULL REFERENCES stages(id),
            kind TEXT NOT NULL,
            sort_order INTEGER NOT NULL,
            title TEXT NOT NULL,
            key_tonic TEXT NOT NULL,
            key_mode TEXT NOT NULL,
            style TEXT NOT NULL,
            bpm REAL NOT NULL,
            time_num INTEGER NOT NULL,
            time_den INTEGER NOT NULL,
            total_bars INTEGER NOT NULL,
            description TEXT NOT NULL,
            loopable INTEGER NOT NULL,
            UNIQUE(stage_id, kind, sort_order)
        )''',
        '''CREATE UNIQUE INDEX IF NOT EXISTS one_primary_per_stage
            ON progressions(stage_id) WHERE kind = 'primary' ''',
        '''CREATE TABLE IF NOT EXISTS chord_events (
            id TEXT PRIMARY KEY,
            progression_id TEXT NOT NULL REFERENCES progressions(id),
            sort_order INTEGER NOT NULL,
            symbol TEXT NOT NULL,
            harmonic_function TEXT NOT NULL,
            start_beat REAL NOT NULL,
            duration_beats REAL NOT NULL,
            UNIQUE(progression_id, sort_order)
        )''',
        '''CREATE TABLE IF NOT EXISTS note_events (
            id TEXT PRIMARY KEY,
            progression_id TEXT NOT NULL REFERENCES progressions(id),
            midi INTEGER NOT NULL,
            start_beat REAL NOT NULL,
            duration_beats REAL NOT NULL,
            velocity INTEGER NOT NULL,
            role TEXT NOT NULL,
            hand TEXT NOT NULL,
            UNIQUE(progression_id, midi, start_beat, role)
        )''',
        '''CREATE TRIGGER IF NOT EXISTS unique_lesson_order_by_category_insert
            BEFORE INSERT ON lessons
            WHEN EXISTS (
                SELECT 1 FROM lessons existing
                JOIN skills old_skill ON old_skill.id = existing.primary_skill_id
                JOIN skills new_skill ON new_skill.id = NEW.primary_skill_id
                WHERE old_skill.category_id = new_skill.category_id
                  AND existing.order_in_category = NEW.order_in_category
                  AND existing.id <> NEW.id
            )
            BEGIN SELECT RAISE(ABORT, 'duplicate lesson order in category'); END''',
        '''CREATE TRIGGER IF NOT EXISTS unique_lesson_order_by_category_update
            BEFORE UPDATE OF primary_skill_id, order_in_category ON lessons
            WHEN EXISTS (
                SELECT 1 FROM lessons existing
                JOIN skills old_skill ON old_skill.id = existing.primary_skill_id
                JOIN skills new_skill ON new_skill.id = NEW.primary_skill_id
                WHERE old_skill.category_id = new_skill.category_id
                  AND existing.order_in_category = NEW.order_in_category
                  AND existing.id <> NEW.id
            )
            BEGIN SELECT RAISE(ABORT, 'duplicate lesson order in category'); END''',
    ]
    for statement in statements:
        conn.execute(statement)


TABLES = {
    'categories': ('categories', 'id,slug,name,description,sort_order', ('id', 'slug', 'name', 'description', 'order')),
    'skills': ('skills', 'id,category_id,name,description,sort_order', ('id', 'categoryId', 'name', 'description', 'order')),
    'lessons': ('lessons', 'id,primary_skill_id,order_in_category,title,difficulty,goal,intro_md,target_minutes,style_tags', ('id', 'primarySkillId', 'orderInCategory', 'title', 'difficulty', 'goal', 'introMd', 'targetMinutes', 'styleTags')),
    'stages': ('stages', 'id,lesson_id,sort_order,title,explanation_md,task,change_from_previous,success_criteria,simplify_hint,extend_hint', ('id', 'lessonId', 'order', 'title', 'explanationMd', 'task', 'changeFromPrevious', 'successCriteria', 'simplifyHint', 'extendHint')),
    'progressions': ('progressions', 'id,stage_id,kind,sort_order,title,key_tonic,key_mode,style,bpm,time_num,time_den,total_bars,description,loopable', ('id', 'stageId', 'kind', 'order', 'title', 'keyTonic', 'keyMode', 'style', 'bpm', 'timeSignature', 'totalBars', 'description', 'loopable')),
    'chord-events': ('chord_events', 'id,progression_id,sort_order,symbol,harmonic_function,start_beat,duration_beats', ('id', 'progressionId', 'order', 'symbol', 'function', 'startBeat', 'durationBeats')),
    'note-events': ('note_events', 'id,progression_id,midi,start_beat,duration_beats,velocity,role,hand', ('id', 'progressionId', 'midi', 'startBeat', 'durationBeats', 'velocity', 'role', 'hand')),
}


def values_for(name, row):
    values = [row.get(field) for field in TABLES[name][2]]
    if name == 'lessons':
        values[-1] = json.dumps(values[-1], ensure_ascii=False)
    elif name == 'stages':
        values[7] = json.dumps(values[7], ensure_ascii=False)
        values[8] = row.get('simplifyHint')
        values[9] = row.get('extendHint')
    elif name == 'progressions':
        meter = row['timeSignature']
        values[9:10] = [meter['numerator'], meter['denominator']]
        values[-1] = int(values[-1])
    return tuple(values)


def validate_prerequisite_table(connection):
    columns = connection.execute('PRAGMA table_info(lesson_prerequisites)').fetchall()
    column_names = {column[1] for column in columns}
    primary_key = sorted((column[1], column[5]) for column in columns if column[5])
    expected_primary_key = [('lesson_id', 1), ('prerequisite_lesson_id', 2)]
    sort_order = next((column for column in columns if column[1] == 'sort_order'), None)
    unique_pairs = []
    for index in connection.execute('PRAGMA index_list(lesson_prerequisites)').fetchall():
        if index[2]:
            indexed_columns = [row[2] for row in connection.execute(f'PRAGMA index_info({index[1]})')]
            unique_pairs.append(indexed_columns)

    if (
        not {'lesson_id', 'prerequisite_lesson_id', 'sort_order'} <= column_names
        or sort_order is None
        or not sort_order[3]
        or primary_key != expected_primary_key
        or ['lesson_id', 'sort_order'] not in unique_pairs
    ):
        raise ValueError(
            'lesson_prerequisites incompatible; usa una base SQLite nueva para el esquema actual'
        )


def import_sql(directory, db, mode):
    issues, data = validate(directory, mode)
    if issues:
        raise ValueError('validación falló: ' + '; '.join(issues))
    connection = sqlite3.connect(db)
    try:
        connection.execute('PRAGMA foreign_keys=ON')
        connection.execute('BEGIN')
        init_db(connection)
        validate_prerequisite_table(connection)
        with connection:
            for name in SCHEMA_NAMES:
                table, columns, _ = TABLES[name]
                names = columns.split(',')
                placeholders = ','.join('?' for _ in names)
                updates = ','.join(f'{column}=excluded.{column}' for column in names[1:])
                sql = f'INSERT INTO {table} ({columns}) VALUES ({placeholders}) ON CONFLICT(id) DO UPDATE SET {updates}'
                for row in data[name]:
                    connection.execute(sql, values_for(name, row))
            for lesson in data['lessons']:
                connection.execute('DELETE FROM lesson_prerequisites WHERE lesson_id=?', (lesson['id'],))
                connection.executemany(
                    'INSERT INTO lesson_prerequisites VALUES(?,?,?)',
                    [
                        (lesson['id'], prerequisite, sort_order)
                        for sort_order, prerequisite in enumerate(lesson['prerequisiteLessonIds'], start=1)
                    ],
                )
        return connection
    except Exception:
        connection.rollback()
        connection.close()
        raise


def main():
    parser = argparse.ArgumentParser(description='Herramientas curriculares Piano Lab schemaVersion 1.0.0')
    commands = parser.add_subparsers(dest='command', required=True)
    validate_parser = commands.add_parser('validate', help='Valida schemas e integridad')
    validate_parser.add_argument('--mode', choices=['design', 'pilot', 'batch', 'global'], required=True)
    validate_parser.add_argument('--data', type=Path, default=ROOT / 'approved')
    export_parser = commands.add_parser('export-midi', help='Exporta MIDI formato 0, PPQ 960')
    export_parser.add_argument('progression_id')
    export_parser.add_argument('--data', type=Path, default=ROOT / 'approved')
    export_parser.add_argument('--output', type=Path, required=True)
    import_parser = commands.add_parser('import-sqlite', help='Importa a SQLite de forma transaccional e idempotente')
    import_parser.add_argument('--data', type=Path, default=ROOT / 'approved')
    import_parser.add_argument('--database', type=Path, required=True)
    import_parser.add_argument('--mode', choices=['pilot', 'batch', 'global'], required=True)
    args = parser.parse_args()
    try:
        if args.command == 'validate':
            issues, _ = validate(args.data, args.mode)
            for issue in issues:
                print('ERROR:', issue)
            if issues:
                return 1
            print('Validación correcta')
            return 0
        if args.command == 'export-midi':
            issues, data = validate(args.data, 'batch')
            if issues:
                raise ValueError('validación falló: ' + '; '.join(issues))
            progressions = {row['id']: row for row in data['progressions']}
            if args.progression_id not in progressions:
                raise ValueError('progressionId desconocido')
            progression = progressions[args.progression_id]
            notes = [row for row in data['note-events'] if row['progressionId'] == args.progression_id]
            midi_file(progression, notes, args.output)
            print(args.output)
            return 0
        connection = import_sql(args.data, args.database, args.mode)
        connection.close()
        print(f'Importación correcta: {args.database}')
        return 0
    except Exception as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
