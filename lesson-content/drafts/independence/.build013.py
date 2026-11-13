import json, shutil, subprocess
from pathlib import Path
root=Path(__file__).parent
out=root/'pending-013'
checks=out/'checks'
checks.mkdir(parents=True,exist_ok=True)
lesson=json.loads((root.parent.parent/'data/lessons.json').read_text())
lesson=[x for x in lesson if x['id']=='lesson-independence-013']
(out/'lessons.json').write_text(json.dumps(lesson,ensure_ascii=False,indent=2)+'\n')
# Snapshot canonical design and four musical tables before composing.
for name in ('categories','skills','lessons','stages','progressions','chord-events','note-events'):
    src=(root.parent.parent/'approved'/f'{name}.json')
    if name in ('stages','progressions','chord-events','note-events'):
        src=root/'pending-012'/'checks'/f'{name}.json'
    shutil.copyfile(src,checks/f'{name}.json')
for name in ('stages','progressions','chord-events','note-events'):
    (out/f'{name}.json').write_text('[]\n')
stages=[]; progs=[]; chords=[]; notes=[]
labels=['Fijar el vamp','Repetir la frase','Ampliar la respuesta','Desplazar la síncopa','Elegir un silencio']
changes=['LH establece ostinato: C3/G3, offsets 0/0.5/2/2.5, duración 0.25. RH presenta E4 y G4.','Se añade Bb4 en offset 3 de la segunda frase (compases 5–8); la primera frase y LH permanecen iguales.','Solo E4 de compases 5–8 pasa de duración 0.5 a 1.5; demás notas de 02 no cambian.','Solo G4 de compases 5–8 pasa de offset 2 a 1.5 y duración 0.5 a 1; cruza ligado el ataque de beat 2; E4 y Bb4 quedan como en 03.','Desde 04 se omite Bb4 en global beat 23; se omite además únicamente Bb4 de compás 8 offset 3, para no acumular silencios.']
for s in range(1,6):
    sid=f'stage-independence-013-{s:02d}'; pid=f'prog-independence-013-{s:02d}-primary'
    stages.append({'id':sid,'lessonId':'lesson-independence-013','order':s,'title':labels[s-1],'explanationMd':changes[s-1]+' El vamp C7/I7 queda fijo; el bajo reducido raíz–quinta es una armonía parcial y Bb explicita la séptima menor de C7.','task':changes[s-1]+' Toca a 88 BPM, cuenta cuatro negras por compás y mantén independientes ambas manos.','changeFromPrevious':changes[s-1],'successCriteria':[changes[s-1]+' LH conserva sin excepción las 32 notas idénticas, duración 0.25 y velocidad 65.'],'simplifyHint':'Aísla primero LH en 0/0.5/2/2.5; suma RH lentamente sin alterar sus duraciones.','extendHint':'Cuenta los offsets y duraciones de RH mientras mantienes intactas las 32 notas del ostinato.'})
    progs.append({'id':pid,'stageId':sid,'kind':'primary','order':1,'title':labels[s-1],'keyTonic':'C','keyMode':'major','style':'funk','bpm':88,'timeSignature':{'numerator':4,'denominator':4},'totalBars':8,'description':'Vamp C7/I7: un acorde por cuatro compases, repetido; cada acorde dura 16 negras. LH C3/G3 alternados en offsets 0, 0.5, 2, 2.5, duración 0.25 (32 ataques idénticos). RH usa solo E4, G4 y Bb4: melodía de C7; Bb es su séptima. Textura armónica parcial raíz/quinta más línea explícita, sin acordes RH.','loopable':True})
    for bar in range(8):
      start=bar*4; sym='C7' if bar%4<4 else 'C7'
      if bar in (0,4): chords.append({'id':f'chord-independence-013-{s:02d}-{bar+1:02d}','progressionId':pid,'order':bar//4+1,'symbol':sym,'function':'I7','startBeat':start,'durationBeats':16})
      for j,(off,pitch) in enumerate(zip((0,.5,2,2.5),(48,55,48,55))):
        notes.append({'id':f'note-independence-013-{s:02d}-lh-{bar*4+j+1:03d}','progressionId':pid,'midi':pitch,'startBeat':start+off,'durationBeats':.25,'velocity':65,'role':'bass','hand':'left'})
      for off,pitch,dur in [(0,64,.5),(2,67,.5)]:
        if s==3 and bar>=4 and pitch==64: dur=1.5
        if s==4 and bar>=4 and pitch==67: off,dur=1.5,1
        notes.append({'id':f'note-independence-013-{s:02d}-rh-{bar*3+1:03d}-{pitch}','progressionId':pid,'midi':pitch,'startBeat':start+off,'durationBeats':dur,'velocity':72,'role':'melody','hand':'right'})
      if s>=2 and bar>=4 and s<5 or (s==5 and bar>=4 and bar!=5 and bar!=7):
        notes.append({'id':f'note-independence-013-{s:02d}-rh-bb-{bar+1:02d}','progressionId':pid,'midi':70,'startBeat':start+3,'durationBeats':.5,'velocity':72,'role':'melody','hand':'right'})
    if s==5:
      # retain only one silence from response, as requested: bar 6 removed above, remove bar 8 response here
      notes=[n for n in notes if not (n['progressionId']==pid and n['midi']==70 and n['startBeat']==31)]
for name,data in [('stages',stages),('progressions',progs),('chord-events',chords),('note-events',notes)]:
 p=out/f'{name}.json'; old=json.loads(p.read_text()); p.write_text(json.dumps(old+data,ensure_ascii=False,indent=2)+'\n')
# Export exactly five MIDI files through project exporter.
for s in range(1,6):
 pid=f'prog-independence-013-{s:02d}-primary'
 subprocess.run([str(root.parent.parent/'.venv/bin/python'),str(root.parent.parent/'tools/scripts/curriculum.py'),'export-midi',pid,'--data',str(out),'--output',str(out/f'independence-013-{s:02d}.mid')],check=True)
