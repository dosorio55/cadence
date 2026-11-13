import json
from pathlib import Path
root = Path(__file__).parent
src = root.parent / 'checks'
out = root / 'expression'
out.mkdir(exist_ok=True)
for name in ('categories','skills','lessons'):
    data = json.loads((src / f'{name}.json').read_text())
    (out / f'{name}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
lesson = 'lesson-expression-012'
canonical = next(x for x in json.loads((src/'lessons.json').read_text()) if x['id'] == lesson)
stages=[]; progressions=[]; chords=[]; notes=[]
lhs=[[48,52],[45,48],[41,45],[43,47]]
rhs=[[64,67],[69,64],[65,69],[67,62]]
functions=['I','vi','IV','V']
for n in range(1,5):
    sid=f'stage-expression-012-{n:02}'
    pid=f'prog-expression-012-{n:02}-primary'
    rd=[0.5,0.5,2,1.75][n-1]
    ld=[0.5,0.25,0.25,0.25][n-1]
    title=['Articulación pareja','Izquierda breve','Melodía ligada','Independencia de duración'][n-1]
    description=['Ambas manos separan sus ataques por dos pulsos y cada nota dura 0.5.','Solo la izquierda acorta cada nota a 0.25; la derecha mantiene 0.5.','La derecha sostiene cada nota durante dos pulsos, hasta el ataque siguiente; sin pedal.','La derecha sostiene 1.75 pulsos y deja 0.25 de separación antes del ataque siguiente; la izquierda conserva 0.25.'][n-1]
    stages.append({'id':sid,'lessonId':lesson,'order':n,'title':title,'explanationMd':description,'task':'Toca los cuatro compases sin cambiar ataques, alturas ni velocidades; compara únicamente las duraciones indicadas.','changeFromPrevious':description if n==1 else f'Solo cambia la duración de la derecha respecto a la etapa {n-1:02}; conserva todas las demás notas, ataques, velocidades y duraciones izquierdas.','successCriteria':['Los cuatro compases mantienen los mismos ataques, alturas y velocidades.','Puedo distinguir la articulación independiente de ambas manos sin usar pedal.'],'simplifyHint':'Practica cada mano por separado y cuenta cuatro pulsos por compás.','extendHint':'Canta una melodía conocida en el mismo registro, sin añadir notas ni una tercera parte.'})
    progressions.append({'id':pid,'stageId':sid,'kind':'primary','order':1,'title':title,'keyTonic':'C','keyMode':'major','style':'pop','bpm':90,'timeSignature':{'numerator':4,'denominator':4},'totalBars':4,'description':description,'loopable':False})
    for bar in range(4):
        start=bar*4
        chords.append({'id':f'ce-expression-012-{n:02}-{bar+1:02}','progressionId':pid,'order':bar+1,'symbol':['C','Am','F','G'][bar],'function':functions[bar],'startBeat':start,'durationBeats':4})
        for hand,pitches,vel,dur in [('left',lhs[bar],55,ld),('right',rhs[bar],76,rd)]:
            for j,pitch in enumerate(pitches):
                notes.append({'id':f'ne-expression-012-{n:02}-{bar+1:02}-{hand}-{j+1}','progressionId':pid,'midi':pitch,'startBeat':start+j*2,'durationBeats':dur,'velocity':vel,'role':'accompaniment' if hand=='left' else 'melody','hand':hand})
for name,data in [('stages',stages),('progressions',progressions),('chord-events',chords),('note-events',notes)]:
    (out/f'{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
checks=root/'checks'
checks.mkdir(exist_ok=True)
for name in ('categories','skills','lessons','stages','progressions','chord-events','note-events'):
    source=json.loads((src/f'{name}.json').read_text())
    if name=='stages': source=[x for x in source if x['lessonId']!=lesson]+stages
    elif name=='progressions': source=[x for x in source if not x['id'].startswith('prog-expression-012-')]+progressions
    elif name=='chord-events': source=[x for x in source if not x['progressionId'].startswith('prog-expression-012-')]+chords
    elif name=='note-events': source=[x for x in source if not x['progressionId'].startswith('prog-expression-012-')]+notes
    # The existing canonical design is retained byte-for-data exactly.
    (checks/f'{name}.json').write_text(json.dumps(source,ensure_ascii=False,indent=2)+'\n')
