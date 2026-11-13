import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[2] / 'tools' / 'scripts'))
import audit_delivery
import curriculum

root = Path(__file__).parent / 'checks'
errors, data = curriculum.validate(root, 'batch')
assert not errors, errors
by_progression = {row['id']: [] for row in data['progressions']}
for note in data['note-events']:
    by_progression[note['progressionId']].append(note)

v004 = [
    [[48, 52], [55, 59], [57, 60], [53, 57]],
    [[60, 64], [67, 71], [69, 72], [65, 69]],
    [[60, 64, 67], [67, 71, 74], [69, 72, 76], [65, 69, 72]],
    [[60, 64], [67, 71], [69, 72], [65, 69]],
    [[60, 64, 67], [67, 71], [69, 72, 76], [65, 69]],
]
roots004 = [36, 43, 33, 41]
v006 = [
    [[60, 64, 67], [67, 71, 74], [69, 72, 76], [65, 69, 72]] * 2,
    [[60, 64, 67], [59, 62, 67], [69, 72, 76], [65, 69, 72]] * 2,
    [[60, 64, 67], [59, 62, 67], [60, 64, 69], [60, 65, 69]] * 2,
    [[55, 60, 64], [55, 59, 62], [57, 60, 64], [57, 60, 65]] * 2,
    [[55, 60, 64], [55, 59, 62], [52, 57, 60], [53, 57, 60], [52, 55, 60], [55, 59, 62], [57, 60, 64], [57, 60, 65]],
]


def events(number, stage, bar, hand, role):
    pid = f'prog-accompaniment-{number:03}-{stage:02}-primary'
    return sorted((note['midi'], note['startBeat'] - 4 * bar, note['durationBeats'])
                  for note in by_progression[pid] if note['hand'] == hand and note['role'] == role
                  and 4 * bar <= note['startBeat'] < 4 * (bar + 1))

for stage in range(1, 6):
    for bar in range(4):
        assert events(4, stage, bar, 'left', 'bass') == [(roots004[bar], 4 * bar - 4 * bar, 4)]
        assert events(4, stage, bar, 'right', 'harmony') == [(midi, 0, 4) for midi in v004[stage - 1][bar]]

melody = [[62, 65], [71, 69], [64, 67], [72, 71]]
roots005 = [38, 43, 36, 36]
shells = [[53, 60], [53, 59], [52, 59], [52, 59]]
for stage in range(1, 6):
    for bar in range(4):
        assert events(5, stage, bar, 'right', 'melody') == sorted([(melody[bar][0], 0, 1), (melody[bar][1], 1, 1)])
        expected = [(roots005[bar], 0, 0.5)]
        offsets = {1: [], 2: [2, 3], 3: [3], 4: [2], 5: [[3, 2, 3, 2][bar]]}[stage]
        expected.extend((midi, offset, 0.5) for offset in offsets for midi in shells[bar])
        assert events(5, stage, bar, 'left', 'bass') == [(roots005[bar], 0, 0.5)]
        assert events(5, stage, bar, 'left', 'harmony') == sorted((midi, offset, 0.5) for offset in offsets for midi in shells[bar])

for stage in range(1, 6):
    for bar in range(8):
        assert events(6, stage, bar, 'left', 'bass') == [(([36, 43, 33, 41] * 2)[bar], 0, 4)]
        assert events(6, stage, bar, 'right', 'harmony') == [(midi, 0, 4) for midi in v006[stage - 1][bar]]

metrics = audit_delivery.musical_metrics(data)
assert metrics['findings'] == [], metrics['findings']
for progression in data['progressions']:
    notes = by_progression[progression['id']]
    output = root / f'{progression["id"]}.mid'
    curriculum.midi_file(progression, notes, output)
    parsed = audit_delivery.inspect_midi(output)
    expected = sorted((round(note['startBeat'] * 960),
                       round((note['startBeat'] + note['durationBeats']) * 960),
                       note['midi'], note['velocity']) for note in notes)
    assert parsed['notes'] == expected, progression['id']

print(json.dumps({
    'records': {name: len(data[name]) for name in ('lessons', 'stages', 'progressions', 'chord-events', 'note-events')},
    'allPlanBarsAsserted': True,
    'musicalMetricsFindings': metrics['findings'],
    'midiExportedAndBinaryInspected': len(data['progressions']),
}, ensure_ascii=False))
