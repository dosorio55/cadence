import hashlib
import importlib.util
import json
import struct
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
import curriculum
import record_approval

spec = importlib.util.spec_from_file_location('audit_delivery', SCRIPTS / 'audit_delivery.py')
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class MidiAuditTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.path = Path(self.temporary.name) / 'test.mid'
        self.progression = {'bpm': 80, 'timeSignature': {'numerator': 4, 'denominator': 4}, 'totalBars': 2}
        self.notes = [
            {'midi': 48, 'startBeat': 0, 'durationBeats': 1, 'velocity': 70},
            {'midi': 60, 'startBeat': 1 / 3, 'durationBeats': 2 / 3, 'velocity': 80},
            {'midi': 60, 'startBeat': 1, 'durationBeats': 0.5, 'velocity': 76},
        ]

    def test_roundtrip_chord_triplet_repeated_note_and_silent_tail(self):
        curriculum.midi_file(self.progression, self.notes, self.path)
        result = audit.inspect_midi(self.path)
        self.assertEqual(result['ppq'], 960)
        self.assertEqual(result['endTick'], 7680)
        self.assertEqual(result['tempos'], [(0, 750000)])
        self.assertEqual(result['meters'], [(0, 4, 4)])
        self.assertEqual(result['notes'], [(0, 960, 48, 70), (320, 960, 60, 80), (960, 1440, 60, 76)])

    def test_sounding_same_pitch_overlap_is_rejected(self):
        self.notes.append({'midi': 60, 'startBeat': 0.5, 'durationBeats': 1, 'velocity': 75})
        curriculum.midi_file(self.progression, self.notes, self.path)
        with self.assertRaisesRegex(ValueError, 'solapadas'):
            audit.inspect_midi(self.path)

    def test_truncated_track_is_rejected(self):
        curriculum.midi_file(self.progression, self.notes, self.path)
        self.path.write_bytes(self.path.read_bytes()[:-1])
        with self.assertRaisesRegex(ValueError, 'Longitud'):
            audit.inspect_midi(self.path)

    def test_approval_fingerprint_ignores_order_but_detects_note_changes(self):
        data = {'lessons': [{'id': 'l1'}], 'stages': [{'id': 's1', 'lessonId': 'l1'}],
                'progressions': [{'id': 'p1', 'stageId': 's1'}], 'chord-events': [],
                'note-events': [{'id': 'n1', 'progressionId': 'p1', 'midi': 60},
                                {'id': 'n2', 'progressionId': 'p1', 'midi': 64}]}
        first = audit.subset_fingerprint(data, ['l1'])
        data['note-events'].reverse()
        self.assertEqual(first, audit.subset_fingerprint(data, ['l1']))
        data['note-events'][0]['midi'] = 65
        self.assertNotEqual(first['sha256'], audit.subset_fingerprint(data, ['l1'])['sha256'])

    def test_register_rejects_open_issue_despite_approved_heading(self):
        review = Path(self.temporary.name) / 'review.md'
        review.write_text('approved\n```json\n[{"issueId":"X-1","status":"open"}]\n```')
        with self.assertRaisesRegex(ValueError, 'Incidencia pendiente'):
            record_approval.read_review(review)
        review.write_text('rejected\n```json\n[]\n```')
        with self.assertRaisesRegex(ValueError, 'no aprobada'):
            record_approval.read_review(review)
        review.write_text('verdict: approved\n```json\n[]\n```')
        self.assertEqual(record_approval.read_review(review), [])

    def test_approval_gate_rejects_open_blockers_and_changed_review(self):
        data = {'lessons': [{'id': 'l1'}], 'stages': [], 'progressions': [],
                'chord-events': [], 'note-events': []}
        root = Path(self.temporary.name)
        review = root / 'review.md'
        review.write_text('approved')
        freeze = {'schemaVersion': '1.0.0', 'massProductionAuthorized': True,
                  'sha256': {}, 'pilotSha256': {}}
        (root / 'contract-freeze.json').write_text(json.dumps(freeze))
        register = [{'category': 'test', 'batch': 1, 'verdict': 'approved',
                     'fingerprint': audit.subset_fingerprint(data, ['l1']),
                     'review': str(review),
                     'reviewSha256': hashlib.sha256(review.read_bytes()).hexdigest()}]
        (root / 'batch-register.json').write_text(json.dumps(register))
        issues_path = root / 'issues.json'
        issues_path.write_text('[]')
        self.assertEqual(audit.audit_approvals(data, root)['lessonsCovered'], 1)

        for severity in ('blocker', 'major'):
            issues_path.write_text(json.dumps([
                {'issueId': 'TOOLS-X', 'severity': severity, 'status': 'open'},
            ]))
            with self.assertRaisesRegex(ValueError, 'Incidencia pendiente de cierre: TOOLS-X'):
                audit.audit_approvals(data, root)

        issues_path.write_text(json.dumps([
            {'issueId': 'TOOLS-X', 'severity': 'major', 'status': 'resolved'},
            {'issueId': 'TEXT-X', 'severity': 'minor', 'status': 'open'},
        ]))
        self.assertEqual(audit.audit_approvals(data, root)['lessonsCovered'], 1)

        review.write_text('rejected')
        with self.assertRaisesRegex(ValueError, 'Revisión aprobada alterada'):
            audit.audit_approvals(data, root)

    def test_metrics_flag_overlap_reach_and_unchanged_stage(self):
        data = {'progressions': [{'id': 'p1', 'stageId': 's1', 'kind': 'primary'},
                                 {'id': 'p2', 'stageId': 's2', 'kind': 'primary'}],
                'stages': [{'id': 's1', 'lessonId': 'l1', 'order': 1},
                           {'id': 's2', 'lessonId': 'l1', 'order': 2}],
                'note-events': []}
        for pid in ('p1', 'p2'):
            for midi, role in ((60, 'harmony'), (76, 'melody'), (60, 'melody')):
                data['note-events'].append({'progressionId': pid, 'midi': midi, 'role': role,
                                            'hand': 'right', 'startBeat': 0,
                                            'durationBeats': 1, 'velocity': 80})
        result = audit.musical_metrics(data)
        kinds = {finding['kind'] for finding in result['findings']}
        self.assertEqual(kinds, {'handReachReview', 'samePitchOverlap',
                                'identicalMidiNeedsPedagogicalJustification'})
        self.assertEqual(result['progressionsAnalyzed'], 2)

    def test_unclosed_note_is_rejected(self):
        track = b'\x00\x90\x3c\x50\x00\xff\x2f\x00'
        header = b'MThd' + struct.pack('>IHHH', 6, 0, 1, 960)
        self.path.write_bytes(header + b'MTrk' + struct.pack('>I', len(track)) + track)
        with self.assertRaisesRegex(ValueError, 'sin cierre'):
            audit.inspect_midi(self.path)


if __name__ == '__main__':
    unittest.main()
