import json
import struct
from pathlib import Path

root = Path(__file__).parent
notes = json.loads((root / "note-events.json").read_text())
assert len(json.loads((root / "lessons.json").read_text())) == 1
assert len(json.loads((root / "stages.json").read_text())) == 4
bar_lh = [[48, 52, 59], [45, 48, 55], [50, 53, 60], [43, 47, 53], [48, 52, 59], [45, 48, 55], [43, 47, 53], [48, 52, 59]]
bar_rh = [[64, 67, 64, 67], [64, 67, 64, 67], [65, 69, 65, 69], [71, 65, 71, 65], [64, 67, 64, 67], [64, 67, 64, 67], [71, 65, 71, 65], [64, 72, 64, 72]]
for stage in range(1, 5):
    pid = f"prog-expression-013-{stage:02}-primary"
    stage_notes = [x for x in notes if x["progressionId"] == pid]
    left = [x for x in stage_notes if x["hand"] == "left"]
    right = [x for x in stage_notes if x["hand"] == "right"]
    assert len(left) == 24
    assert [(x["startBeat"], x["midi"], x["durationBeats"], x["velocity"]) for x in left] == [(bar * 4, pitch, 4, 55) for bar, pitches in enumerate(bar_lh) for pitch in pitches]
    expected = [(bar * 4 + offset, bar_rh[bar][i], duration, 84 if stage == 4 and bar == 7 and i == 0 else 72) for bar in range(8) for i, (offset, duration) in enumerate(zip([0, 2 / 3, 2, 8 / 3], [2 / 3, 1 / 3, 2 / 3, 1 / 3])) if not (stage == 2 and bar == 3 and i >= 2) and not (stage in (3, 4) and bar == 6 and i >= 2)]
    assert [(x["startBeat"], x["midi"], x["durationBeats"], x["velocity"]) for x in right] == expected
    midi = (root / f"prog-expression-013-{stage:02}-primary.mid").read_bytes()
    assert midi[:14] == b"MThd" + struct.pack(">IHHH", 6, 0, 1, 960)
    assert b"\xff\x51\x03\x0c\xb75" in midi
    assert midi.count(b"\x90") == len(left) + len(right)
    assert midi.count(b"\x80") == len(left) + len(right)
print("4 MIDI and all event assertions passed")
