import json, struct
from pathlib import Path
p=Path(__file__).parent/'pending-013'
for i in range(1,6):
    pid=f'prog-independence-013-{i:02d}-primary'
    notes=[n for n in json.loads((p/'note-events.json').read_text()) if n['progressionId']==pid]
    lh=[n for n in notes if n['hand']=='left']
    rh=[n for n in notes if n['hand']=='right']
    assert len(lh)==32 and all(n['midi']==([48,55][int((n['startBeat']%4) in (0.5,2.5))]) for n in lh)
    assert all(n['durationBeats']==.25 and n['velocity']==65 for n in lh)
    assert {n['midi'] for n in rh} <= {64,67,70}
    raw=(p/f'independence-013-{i:02d}.mid').read_bytes()
    assert raw[:4]==b'MThd' and raw.count(b'MTrk')==1 and len(raw)>100
