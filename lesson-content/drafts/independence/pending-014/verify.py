import json
import struct
from pathlib import Path

root = Path(__file__).parent
notes = json.loads((root / 'note-events.json').read_text())
assert len(json.loads((root / 'lessons.json').read_text())) == 1
assert len(json.loads((root / 'stages.json').read_text())) == 5
bars = [[38,41,45,41],[43,47,50,47],[48,52,55,47],[48,52,43,43],[45,48,40,36],[38,41,45,41],[43,47,50,47],[48,52,43,40]]
expected_rh = {
    1: [(4+2/3,[59,65]),(28+2/3,[64,71])],
    2: [(4+2/3,[59,65]),(28+2/3,[64,71])],
    3: [(4+2/3,[59,65]),(28+2/3,[64,71])],
    4: [(5+2/3,[59,65]),(28+2/3,[64,71])],
    5: [(24+2/3,[59,65]),(28+2/3,[64,71])],
}
for stage in range(1,6):
    pid=f'prog-independence-014-{stage:02}-primary'
    events=[n for n in notes if n['progressionId']==pid]
    left=sorted((n for n in events if n['hand']=='left'),key=lambda n:n['startBeat'])
    right=sorted((n for n in events if n['hand']=='right'),key=lambda n:n['startBeat'])
    expected_left=[(b*4+k, 49 if stage>=3 and b==1 and k==3 else pitch, 1, 65) for b,row in enumerate(bars) for k,pitch in enumerate(row)]
    assert [(n['startBeat'],n['midi'],n['durationBeats'],n['velocity']) for n in left]==expected_left
    assert len(right)==4
    assert [(right[j]['startBeat'],right[j+1]['startBeat']) for j in range(0,4,2)]==[(o,o) for o,_ in expected_rh[stage]]
    assert [[right[j]['midi'],right[j+1]['midi']] for j in range(0,4,2)]==[p for _,p in expected_rh[stage]]
    assert all(n['durationBeats']==1/3 and n['velocity']==64 for n in right)
    assert sorted({n['midi'] for n in left if n['midi'] not in range(38,56)}|{n['midi'] for n in left if n['midi']==49})
    assert max(abs(a['midi']-b['midi']) for a,b in zip(left,left[1:]))<=12
    midi=(root/'checks'/f'{pid}.mid').read_bytes()
    assert midi[:14]==b'MThd'+struct.pack('>IHHH',6,0,1,960)
    assert midi.count(b'\x90')==36 and midi.count(b'\x80')==36
print('five MIDI and event assertions passed')
