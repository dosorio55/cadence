import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location('integrate', SCRIPTS / 'integrate.py')
integrate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(integrate)


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        root = Path(self.temporary.name)
        self.design = root / 'data'
        self.work = root / 'work'
        self.partition = self.work / 'rhythm'
        self.design.mkdir()
        self.partition.mkdir(parents=True)
        self.lesson = {'id': 'lesson-rhythm-001', 'primarySkillId': 'skill-pulse'}
        self.write(self.design, 'categories', [{'id': 'cat-rhythm', 'slug': 'rhythm'}])
        self.write(self.design, 'skills', [{'id': 'skill-pulse', 'categoryId': 'cat-rhythm'}])
        self.write(self.design, 'lessons', [self.lesson])
        self.write(self.partition, 'lessons', [self.lesson])
        self.write(self.partition, 'stages', [{'id': 'stage-1', 'lessonId': self.lesson['id']}])
        self.write(self.partition, 'progressions', [{'id': 'prog-1', 'stageId': 'stage-1'}])
        self.write(self.partition, 'chord-events', [{'id': 'chord-1', 'progressionId': 'prog-1'}])
        self.write(self.partition, 'note-events', [{'id': 'note-1', 'progressionId': 'prog-1'}])

    def write(self, directory, name, rows):
        (directory / f'{name}.json').write_text(json.dumps(rows), encoding='utf-8')

    def test_complete_union_preserves_events(self):
        data = integrate.collect(self.design, self.work, complete=True)
        self.assertEqual(data['note-events'], [{'id': 'note-1', 'progressionId': 'prog-1'}])
        self.assertEqual(data['lessons'], [self.lesson])

    def test_in_place_assembly_preserves_design_bytes(self):
        original = {
            name: (self.design / f'{name}.json').read_bytes()
            for name in integrate.DESIGN
        }

        with patch.object(integrate.tools, 'validate', return_value=([], {})):
            integrate.assemble(self.design, self.work, self.design, 'global')

        for name, expected in original.items():
            self.assertEqual((self.design / f'{name}.json').read_bytes(), expected)

        for name in integrate.CONTENT:
            self.assertEqual(
                integrate.read_array(self.design / f'{name}.json'),
                integrate.read_array(self.partition / f'{name}.json'),
            )

    def test_duplicate_json_property_is_rejected_before_merge(self):
        path = self.partition / 'note-events.json'
        path.write_text('[{"id":"n1","id":"n2","progressionId":"prog-1"}]')
        with self.assertRaisesRegex(ValueError, 'clave duplicada'):
            integrate.collect(self.design, self.work)

    def test_changed_design_is_rejected(self):
        self.write(self.partition, 'lessons', [{**self.lesson, 'title': 'alterado'}])
        with self.assertRaisesRegex(ValueError, 'Diseño alterado'):
            integrate.collect(self.design, self.work)

    def test_undeveloped_lesson_is_rejected(self):
        self.write(self.partition, 'stages', [])
        with self.assertRaisesRegex(ValueError, 'no cubren exactamente'):
            integrate.collect(self.design, self.work)

    def test_cross_partition_reference_is_rejected(self):
        self.write(self.partition, 'note-events', [{'id': 'note-1', 'progressionId': 'otra'}])
        with self.assertRaisesRegex(ValueError, 'fuera de la partición'):
            integrate.collect(self.design, self.work)

    def test_missing_event_file_is_not_silently_empty(self):
        (self.partition / 'chord-events.json').unlink()
        with self.assertRaises(FileNotFoundError):
            integrate.collect(self.design, self.work)

    def test_empty_work_directory_is_rejected(self):
        with tempfile.TemporaryDirectory() as empty:
            with self.assertRaisesRegex(ValueError, 'No hay lecciones'):
                integrate.collect(self.design, Path(empty))

    def test_duplicate_event_id_is_rejected(self):
        self.write(self.partition, 'note-events', [
            {'id': 'note-1', 'progressionId': 'prog-1'},
            {'id': 'note-1', 'progressionId': 'prog-1'},
        ])
        with self.assertRaisesRegex(ValueError, 'ID repetido'):
            integrate.collect(self.design, self.work)


if __name__ == '__main__':
    unittest.main()
