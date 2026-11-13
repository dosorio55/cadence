import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import curriculum


def fixture():
    data = complete_design()
    target = next(lesson for lesson in data['lessons'] if lesson['id'] == 'lesson-1-1')
    target.update({
        'title': 'X', 'introMd': 'Tres etapas porque se justifica el formato reducido.',
        'prerequisiteLessonIds': ['lesson-1-2', 'lesson-1-10'],
        'goal': 'X', 'difficulty': 1, 'targetMinutes': 10, 'styleTags': ['jazz'],
    })
    data['stages'] = [
        {'id': f'stage-x-{i}', 'lessonId': 'lesson-1-1', 'order': i, 'title': 'X', 'explanationMd': 'X', 'task': 'X', 'changeFromPrevious': 'X', 'successCriteria': ['X']}
        for i in range(1, 4)
    ]
    data['progressions'] = [
        {'id': f'prog-x-{i}', 'stageId': f'stage-x-{i}', 'kind': 'primary', 'order': 1, 'title': 'X', 'keyTonic': 'C', 'keyMode': 'major', 'style': 'jazz', 'bpm': 80, 'timeSignature': {'numerator': 4, 'denominator': 4}, 'totalBars': 1, 'description': 'X', 'loopable': True}
        for i in range(1, 4)
    ]
    data['chord-events'] = [
        {'id': f'chord-x-{i}', 'progressionId': f'prog-x-{i}', 'order': 1, 'symbol': 'C', 'function': 'I', 'startBeat': 0, 'durationBeats': 4}
        for i in range(1, 4)
    ]
    data['note-events'] = [
        {'id': f'note-x-{i}', 'progressionId': f'prog-x-{i}', 'midi': 60, 'startBeat': 0, 'durationBeats': 1, 'velocity': 80, 'role': 'harmony', 'hand': 'right'}
        for i in range(1, 4)
    ]
    return data


def complete_design():
    data = {name: [] for name in curriculum.SCHEMA_NAMES}
    for category_index in range(1, 7):
        category_id = f'cat-{category_index}'
        data['categories'].append({'id': category_id, 'slug': f'cat-{category_index}', 'name': 'C', 'description': 'D', 'order': category_index})
        for skill_index in range(1, 6):
            skill_id = f'skill-{category_index}-{skill_index}'
            data['skills'].append({'id': skill_id, 'categoryId': category_id, 'name': 'S', 'description': 'D', 'order': skill_index})
            for lesson_index in range(1, 4):
                lesson_order = (skill_index - 1) * 3 + lesson_index
                data['lessons'].append({'id': f'lesson-{category_index}-{lesson_order}', 'primarySkillId': skill_id, 'orderInCategory': lesson_order, 'title': 'L', 'difficulty': 1, 'goal': 'G', 'introMd': 'Tres etapas porque este ejemplo justifica el formato.', 'prerequisiteLessonIds': [], 'targetMinutes': 10, 'styleTags': ['jazz']})
    return data


def complete_global():
    data = complete_design()
    for lesson in data['lessons']:
        for stage_order in range(1, 4):
            stage_id = f"stage-{lesson['id']}-{stage_order}"
            progression_id = f"prog-{lesson['id']}-{stage_order}"
            data['stages'].append({'id': stage_id, 'lessonId': lesson['id'], 'order': stage_order, 'title': 'S', 'explanationMd': 'E', 'task': 'T', 'changeFromPrevious': 'C', 'successCriteria': ['S']})
            data['progressions'].append({'id': progression_id, 'stageId': stage_id, 'kind': 'primary', 'order': 1, 'title': 'P', 'keyTonic': 'C', 'keyMode': 'major', 'style': 'jazz', 'bpm': 80, 'timeSignature': {'numerator': 4, 'denominator': 4}, 'totalBars': 1, 'description': 'D', 'loopable': True})
            data['chord-events'].append({'id': f'chord-{progression_id}', 'progressionId': progression_id, 'order': 1, 'symbol': 'C', 'function': 'I', 'startBeat': 0, 'durationBeats': 4})
            data['note-events'].append({'id': f'note-{progression_id}', 'progressionId': progression_id, 'midi': 60, 'startBeat': 0, 'durationBeats': 1, 'velocity': 80, 'role': 'harmony', 'hand': 'right'})
    return data


class CurriculumTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.directory = Path(self.temp.name)
        self.write_data(fixture())

    def tearDown(self):
        self.temp.cleanup()

    def write_data(self, data):
        for name, rows in data.items():
            (self.directory / f'{name}.json').write_text(json.dumps(rows), encoding='utf-8')

    def test_disk_schemas_validate_arrays_and_reject_extra_field(self):
        import jsonschema
        schema_path = curriculum.ROOT / 'schemas' / 'categories.schema.json'
        schema = json.loads(schema_path.read_text())
        self.assertEqual(schema['type'], 'array')
        jsonschema.validate([fixture()['categories'][0]], schema)
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate({'id': 'cat-x'}, schema)
        path = self.directory / 'categories.json'
        rows = json.loads(path.read_text())
        rows[0]['invented'] = 1
        path.write_text(json.dumps(rows))
        errors, _ = curriculum.validate(self.directory, 'pilot')
        self.assertTrue(any('Additional properties' in error for error in errors))

    def test_reject_version_mismatch(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'README.md').write_text('schemaVersion: 2.0.0')
            with patch.object(curriculum, 'ROOT', root):
                with self.assertRaisesRegex(ValueError, 'schemaVersion'):
                    curriculum.validate(self.directory, 'pilot')

    def test_global_requires_all_categories_and_every_lesson_staged(self):
        data = complete_design()
        self.write_data(data)
        errors, _ = curriculum.validate(self.directory, 'global')
        self.assertTrue(any('lesson-1-1: requiere 3-6 stages (hay 0)' in error for error in errors))
        data['categories'].append({'id': 'cat-empty', 'slug': 'empty', 'name': 'E', 'description': 'E', 'order': 7})
        self.write_data(data)
        errors, _ = curriculum.validate(self.directory, 'global')
        self.assertTrue(any('cat-empty: global requiere 4-6 skills (hay 0)' in error for error in errors))

    def test_reject_duplicate_json_keys_and_non_finite_numbers(self):
        path = self.directory / 'categories.json'
        path.write_text('[{"id":"cat-x","id":"again"}]')
        with self.assertRaisesRegex(ValueError, 'duplicada'):
            curriculum.validate(self.directory, 'pilot')
        path.write_text('[{"id":"cat-x","slug":"x","name":"X","description":"X","order":1,"extra":NaN}]')
        with self.assertRaisesRegex(ValueError, 'no válida'):
            curriculum.validate(self.directory, 'pilot')

    def test_reject_primary_grid_and_chord_gap(self):
        path = self.directory / 'progressions.json'
        rows = json.loads(path.read_text())
        rows.pop()
        path.write_text(json.dumps(rows))
        errors, _ = curriculum.validate(self.directory, 'pilot')
        self.assertTrue(any('exactamente una primary' in error for error in errors))
        path = self.directory / 'progressions.json'
        path.write_text(json.dumps(fixture()['progressions']))
        path = self.directory / 'note-events.json'
        rows = json.loads(path.read_text())
        rows[0]['startBeat'] = 0.1
        path.write_text(json.dumps(rows))
        errors, _ = curriculum.validate(self.directory, 'pilot')
        self.assertTrue(any('grid' in error for error in errors))
        path = self.directory / 'chord-events.json'
        rows = json.loads(path.read_text())
        rows[0]['durationBeats'] = 2
        path.write_text(json.dumps(rows))
        errors, _ = curriculum.validate(self.directory, 'pilot')
        self.assertTrue(any('no alcanza el final del loop' in error for error in errors))
        chord_path = self.directory / 'chord-events.json'
        chords = fixture()['chord-events']
        chords.extend([
            {'id': 'chord-x-1b', 'progressionId': 'prog-x-1', 'order': 2, 'symbol': 'G', 'function': 'V', 'startBeat': 4, 'durationBeats': 4},
        ])
        chords[0]['order'] = 2
        chords[-1]['order'] = 1
        chord_path.write_text(json.dumps(chords))
        progression_path = self.directory / 'progressions.json'
        progressions = fixture()['progressions']
        progressions[0]['totalBars'] = 2
        progression_path.write_text(json.dumps(progressions))
        errors, _ = curriculum.validate(self.directory, 'pilot')
        self.assertTrue(any('no concuerda con cronología' in error for error in errors))

    def test_midi_end_of_track_reaches_full_loop(self):
        progression = fixture()['progressions'][0]
        progression['totalBars'] = 2
        notes = fixture()['note-events'][:1]
        output = self.directory / 'test.mid'
        curriculum.midi_file(progression, notes, output)
        raw = output.read_bytes()
        self.assertEqual(raw[:4], b'MThd')
        self.assertEqual(int.from_bytes(raw[12:14], 'big'), 960)
        self.assertIn(b'\xff\x51\x03\x0b\x71\xb0', raw)
        self.assertIn(b'\xff\x58\x04\x04\x02', raw)
        self.assertIn(bytes([0x90, 60, 80]), raw)
        self.assertIn(bytes([0x80, 60, 0]), raw)
        self.assertTrue(raw.endswith(b'\xb4\x40\xff\x2f\x00'))

    def test_cli_pilot_import_and_midi_export(self):
        script = curriculum.ROOT / 'tools' / 'scripts' / 'curriculum.py'
        db = self.directory / 'cli.sqlite'
        result = subprocess.run([sys.executable, str(script), 'import-sqlite', '--mode', 'pilot', '--data', str(self.directory), '--database', str(db)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        midi = self.directory / 'cli.mid'
        result = subprocess.run([sys.executable, str(script), 'export-midi', 'prog-x-1', '--data', str(self.directory), '--output', str(midi)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(midi.read_bytes()[:4], b'MThd')
        notes_path = self.directory / 'note-events.json'
        notes = json.loads(notes_path.read_text())
        notes[0]['midi'] = 128
        notes_path.write_text(json.dumps(notes))
        invalid_output = self.directory / 'invalid.mid'
        result = subprocess.run([sys.executable, str(script), 'export-midi', 'prog-x-1', '--data', str(self.directory), '--output', str(invalid_output)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(invalid_output.exists())
        connection = sqlite3.connect(db)
        self.assertEqual(connection.execute('SELECT COUNT(*) FROM lessons').fetchone()[0], 90)
        connection.close()

    def test_cli_validates_and_exports_integer_floats_as_midi_bytes(self):
        data = fixture()
        data['progressions'][0]['timeSignature']['numerator'] = 4.0
        data['note-events'][0]['midi'] = 60.0
        data['note-events'][0]['velocity'] = 80.0
        self.write_data(data)
        script = curriculum.ROOT / 'tools' / 'scripts' / 'curriculum.py'
        result = subprocess.run([sys.executable, str(script), 'validate', '--mode', 'pilot', '--data', str(self.directory)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

        midi = self.directory / 'integer-floats.mid'
        result = subprocess.run([sys.executable, str(script), 'export-midi', 'prog-x-1', '--data', str(self.directory), '--output', str(midi)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        raw = midi.read_bytes()
        self.assertIn(bytes([0xff, 0x58, 0x04, 4, 2]), raw)
        self.assertIn(bytes([0x90, 60, 80]), raw)
        self.assertIn(bytes([0x80, 60, 0]), raw)

        data['note-events'][0]['midi'] = 60.5
        self.write_data(data)
        result = subprocess.run([sys.executable, str(script), 'export-midi', 'prog-x-1', '--data', str(self.directory), '--output', str(self.directory / 'fractional.mid')], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('validación falló', result.stderr)

    def test_cli_global_import(self):
        data = complete_global()
        self.write_data(data)
        script = curriculum.ROOT / 'tools' / 'scripts' / 'curriculum.py'
        database = self.directory / 'global.sqlite'
        result = subprocess.run([sys.executable, str(script), 'import-sqlite', '--mode', 'global', '--data', str(self.directory), '--database', str(database)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        connection = sqlite3.connect(database)
        self.assertEqual(connection.execute('SELECT COUNT(*) FROM lessons').fetchone()[0], 90)
        self.assertEqual(connection.execute('SELECT COUNT(*) FROM stages').fetchone()[0], 270)
        connection.close()

    def test_sqlite_idempotent_and_rollback_after_database_error(self):
        db = self.directory / 'test.sqlite'
        connection = curriculum.import_sql(self.directory, db, 'pilot')
        connection.close()
        connection = curriculum.import_sql(self.directory, db, 'pilot')
        prerequisite_order = connection.execute(
            'SELECT prerequisite_lesson_id, sort_order FROM lesson_prerequisites WHERE lesson_id=? ORDER BY sort_order',
            ('lesson-1-1',),
        ).fetchall()
        self.assertEqual(prerequisite_order, [('lesson-1-2', 1), ('lesson-1-10', 2)])
        self.assertEqual(connection.execute('SELECT COUNT(*) FROM lesson_prerequisites').fetchone()[0], 2)
        before = connection.execute('SELECT * FROM lessons').fetchall()
        connection.execute("CREATE TRIGGER reject_note BEFORE INSERT ON note_events BEGIN SELECT RAISE(ABORT,'forced failure'); END")
        connection.commit()
        connection.close()
        lesson_path = self.directory / 'lessons.json'
        lessons = json.loads(lesson_path.read_text())
        lessons[0]['title'] = 'Cambio que debe revertirse'
        lesson_path.write_text(json.dumps(lessons))
        with self.assertRaises(sqlite3.IntegrityError):
            curriculum.import_sql(self.directory, db, 'pilot')
        connection = sqlite3.connect(db)
        self.assertEqual(connection.execute('SELECT * FROM lessons').fetchall(), before)
        self.assertEqual(connection.execute('SELECT COUNT(*) FROM note_events').fetchone()[0], 3)
        self.assertEqual(
            connection.execute(
                'SELECT prerequisite_lesson_id, sort_order FROM lesson_prerequisites WHERE lesson_id=? ORDER BY sort_order',
                ('lesson-1-1',),
            ).fetchall(),
            [('lesson-1-2', 1), ('lesson-1-10', 2)],
        )
        connection.close()

    def test_legacy_prerequisite_table_aborts_and_rolls_back(self):
        database = self.directory / 'legacy.sqlite'
        connection = sqlite3.connect(database)
        connection.execute('''CREATE TABLE lesson_prerequisites (
            lesson_id TEXT NOT NULL,
            prerequisite_lesson_id TEXT NOT NULL,
            PRIMARY KEY(lesson_id, prerequisite_lesson_id)
        )''')
        connection.commit()
        connection.close()
        with self.assertRaisesRegex(ValueError, 'base SQLite nueva'):
            curriculum.import_sql(self.directory, database, 'pilot')
        connection = sqlite3.connect(database)
        tables = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")}
        self.assertEqual(tables, {'lesson_prerequisites'})
        connection.close()


if __name__ == '__main__':
    unittest.main()
