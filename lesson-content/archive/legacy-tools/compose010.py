import json, shutil, subprocess
from pathlib import Path
root=Path('/home/alejandro/Projects/Development/Personal/music/cadence')
base=root/'curriculum/work/independence'
out=base/'pending-010/5JSON+checks'
check=out/'checks'
check.mkdir(parents=True,exist_ok=True)
lesson=json.loads((root/'curriculum/data/lessons.json').read_text())
lesson=[x for x in lesson if x['id']=='lesson-independence-010']
assert len(lesson)==1
(out/'lessons.json').write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
for name in ['categories.json','skills.json','lessons.json']:
 shutil.copyfile(root/'curriculum/data'/name,check/name)
stage_specs=[
 ('Base y frase inicial','En cuatro compases de Cmaj7–G7–Cmaj7–Am7, RH toca E4 en 0, B4 en 6, C5 en 8 y C5 en 12. B4, séptima de Cmaj7, resuelve a C5 en la frontera 8; LH raíz–quinta conserva sus propios ataques.', 'Toca E4 desde 0 durante 2 negras, B4 desde 6 durante 2 y C5 desde 8 durante 2 y desde 12 durante 2. Mantén LH raíz–quinta en beats 0 y 2 de cada compás, aunque RH tenga otros inicios.', 'Se establece la frase E4–B4–C5–C5; LH toca raíz–quinta en 0 y 2 de cada compás.'),
 ('Ligadura sobre el cambio','La frase conserva E4 y la primera entrada B4; B4 dura hasta 9, atravesando el cambio de bajo en 8 sin reataque. C5 entra en 9 y termina en 10.', 'Toca E4 en 0 por 2 negras y B4 en 6 por 3; sostén B4 a través del ataque LH de 8 sin volver a tocarlo. Ataca C5 en 9 por 1 negra. LH no espera.', 'B4 se ataca una sola vez en 6 y se sostiene hasta 9; C5 se ataca en 9. No hay ataque RH en 8.'),
 ('Resolución fraccionaria','B4 dura 3.5 negras desde 6 hasta 9.5; C5 entra en 9.5 y dura 0.5 hasta 10. LH mantiene inalterados sus ataques.', 'Desde 6, sostén B4 durante 3.5 negras, sin reataque en la frontera LH de 8. Ataca C5 exactamente en 9.5 y suéltalo en 10; mantén LH en 0 y 2.', 'B4 comienza en 6 y termina en 9.5; C5 comienza en 9.5 y termina en 10, mientras LH no modifica su patrón.'),
 ('Resolución autónoma','Elige una única duración de resolución que haga compatible la ligadura de B4 a través de 8 y la entrada de C5; la armonía de llegada Am7 admite C5 como tercera. LH continúa sin esperar.', 'En la respuesta final, elige una duración compatible para B4 y su resolución a C5: B4 entra en 6 y cruza 8 sin reataque; C5 debe entrar después de 8 y antes de 10 y sostenerse hasta 10. No detengas ni retrases los ataques LH.', 'Presento una duración concreta para B4 que cruza 8 sin reataque y una entrada posterior de C5 antes de 10; LH conserva exactamente sus ataques, alturas y duraciones.')]
chords=[('Cmaj7','Imaj7',0),('G7','V7',4),('Cmaj7','Imaj7',8),('Am7','vi7',12)]
progs=[]; stages=[]; ce=[]; ne=[]
for i,(title,ex,task,criteria) in enumerate(stage_specs,1):
 sid=f'stage-independence-010-{i:02d}'; pid=f'prog-independence-010-{i:02d}-primary'
 stages.append(dict(id=sid,lessonId='lesson-independence-010',order=i,title=title,explanationMd=ex,task=task,changeFromPrevious=['Patrón base: ataques LH raíz–quinta y línea RH de referencia.','B4 se prolonga a través de la frontera LH de 8 y resuelve después.','La resolución se desplaza a 9.5 sin alterar la base.','Decisión autónoma de duración compatible; LH no espera.'][i-1],successCriteria=[criteria],simplifyHint='Practica LH sola: raíz y quinta en beats 0 y 2 de cada compás; añade después los ataques y duraciones RH escritos para esta etapa.',extendHint='Mantén fijos los eventos LH y compón una frase RH que cumpla la misma ligadura y resolución sin añadir ataques en la frontera 8.'))
 progs.append(dict(id=pid,stageId=sid,kind='primary',order=1,title=title,keyTonic='C',keyMode='major',style='pop',bpm=72,timeSignature={'numerator':4,'denominator':4},totalBars=4,description=ex,loopable=True))
 for j,(sym,fn,start) in enumerate(chords,1): ce.append(dict(id=f'chord-independence-010-{i:02d}-{j:03d}',progressionId=pid,order=j,symbol=sym,function=fn,startBeat=start,durationBeats=4))
 left=[[48,55],[43,50],[48,55],[45,52]]
 for bar,pitches in enumerate(left):
  for k,pitch in enumerate(pitches): ne.append(dict(id=f'note-independence-010-{i:02d}-LH-{bar*2+k+1:04d}',progressionId=pid,midi=pitch,startBeat=bar*4+k*2,durationBeats=2,velocity=65,role='bass',hand='left'))
 rh=[(64,0,2),(71,6,2),(72,8,2),(72,12,2)] if i==1 else ([(64,0,2),(71,6,3),(72,9,1)] if i==2 else ([(64,0,2),(71,6,3.5),(72,9.5,.5)] if i==3 else [(64,0,2),(71,6,3.25),(72,9.25,.75)]))
 for j,(pitch,start,duration) in enumerate(rh,1): ne.append(dict(id=f'note-independence-010-{i:02d}-RH-{j:04d}',progressionId=pid,midi=pitch,startBeat=start,durationBeats=duration,velocity=72,role='melody',hand='right'))
for name,data in [('stages.json',stages),('progressions.json',progs),('chord-events.json',ce),('note-events.json',ne)]: (check/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
# Data-level assertions and binary MIDI export/validation.
assert all(sum(1 for n in ne if n['progressionId']==p['id'] and n['hand']=='left')==8 for p in progs)
for i,p in enumerate(progs,1):
 notes=[n for n in ne if n['progressionId']==p['id']]
 lh=[(n['midi'],n['startBeat'],n['durationBeats']) for n in notes if n['hand']=='left']
 assert lh==[(pitch,bar*4+k*2,2) for bar,pitches in enumerate([[48,55],[43,50],[48,55],[45,52]]) for k,pitch in enumerate(pitches)]
 assert all(n['velocity']==(65 if n['hand']=='left' else 72) for n in notes)
 right=sorted((n['midi'],n['startBeat'],n['durationBeats']) for n in notes if n['hand']=='right')
 expect=[(64,0,2),(71,6,2),(72,8,2),(72,12,2)] if i==1 else ([(64,0,2),(71,6,3),(72,9,1)] if i==2 else ([(64,0,2),(71,6,3.5),(72,9.5,.5)] if i==3 else [(64,0,2),(71,6,3.25),(72,9.25,.75)]))
 assert right==expect and all(n['startBeat']+n['durationBeats']<=16 for n in notes)
 assert all(a['midi']!=b['midi'] or a['startBeat']+a['durationBeats']<=b['startBeat'] or b['startBeat']+b['durationBeats']<=a['startBeat'] for a in notes for b in notes if a is not b)
 for bar, (sym,fn,start) in enumerate(chords): assert (sym,fn,start,4)==(ce[(i-1)*4+bar]['symbol'],ce[(i-1)*4+bar]['function'],ce[(i-1)*4+bar]['startBeat'],ce[(i-1)*4+bar]['durationBeats'])
# batch validator on complete snapshot and export each musical example.
script=root/'curriculum/scripts/curriculum.py'
subprocess.run([str(root/'curriculum/.venv/bin/python'),str(script),'validate','--mode','batch','--data',str(out)],check=True)
for p in progs:
 subprocess.run([str(root/'curriculum/.venv/bin/python'),str(script),'export-midi',p['id'],'--data',str(out),'--output',str(check/(p['id']+'.mid'))],check=True)
# Remove only this temporary composer script.
Path(__file__).unlink()
