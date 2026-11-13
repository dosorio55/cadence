import json
import shutil
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[4]
out = Path(__file__).parent
checks = out / 'checks'
checks.mkdir(exist_ok=True)
lesson = next(x for x in json.loads((root / 'lesson-content/approved/lessons.json').read_text()) if x['id'] == 'lesson-independence-014')
for name in ('categories', 'skills', 'lessons'):
    shutil.copy2(root / f'lesson-content/approved/{name}.json', checks / f'{name}.json')
(out / 'lessons.json').write_text(json.dumps([lesson], ensure_ascii=False, indent=2) + '\n')

stage_text = [
('Fijar walking y dos respuestas', 'Estudia la línea izquierda a negras y coloca únicamente dos shells RH: G7 en global 4+2/3 (B–F) y Cmaj7 en 28+2/3 (E–B). Cada nota RH dura 1/3 y lleva velocidad 64; las aproximaciones diatónicas conducen por grado conjunto a la raíz siguiente.', 'Establece LH de 32 negras y las dos respuestas RH de dos notas, sin melodía adicional.', 'Toca 8 compases a 72 BPM, 32 notas LH de duración 1 y velocidad 65; RH tiene exactamente dos ataques shell y ningún salto LH supera una octava.'),
('Añadir dos shells', 'Conserva literalmente el walking de 01. Añade solo dos respuestas RH de dos notas: shell G7 en global 4+2/3 (B–F) y shell Cmaj7 en 28+2/3 (E–B). Cada nota dura 1/3 y lleva velocidad 64.', 'RH incorpora exactamente dos ataques de shell; LH queda idéntica.', 'Hay cuatro notas RH en total, en los dos onsets indicados, parejas [59,65] y [64,71], duración 1/3; LH coincide exactamente con 01.'),
('Aproximar con Db', 'La línea permanece fija salvo el beat 7: sustituye G por Db3 (MIDI 49), aproximación cromática superior que resuelve por semitono descendente a C3 en el beat 8. No es C# que sube a D; no se rearmoniza ni cambia RH.', 'Solo cambia LH beat 7: G2(43) pasa a Db3(49); las demás notas, incluidos acordes y RH, no cambian.', 'LH contiene 32 notas; el único cromatismo es MIDI 49 en beat 7 y resuelve a MIDI 48 en beat 8. Los dos shells RH son idénticos a 02.'),
('Desplazar la primera respuesta', 'Desde 03, mueve únicamente el shell G7 del beat global 4+2/3 a 5+2/3; conserva [59,65], duración 1/3 y todas las notas LH.', 'La respuesta G7 se retrasa una negra; lo demás es 03.', 'RH tiene exactamente dos parejas: G7 [59,65] en 5+2/3 y Cmaj7 [64,71] en 28+2/3, cada nota dura 1/3.'),
('Elegir respuestas autónomas', 'Desde 04, mueve solo la respuesta G7 a global 24+2/3, donde vuelve G7. La respuesta Cmaj7 se queda en 28+2/3. Elige exactamente esos dos shells compatibles; no añadas tercera respuesta ni melodía derecha.', 'La respuesta G7 pasa de 5+2/3 a 24+2/3; LH y shell Cmaj7 quedan como en 04.', 'RH contiene exactamente dos shells compatibles, G7 en 24+2/3 y Cmaj7 en 28+2/3; LH conserva las 32 notas de 03.')]

stages=[]; progressions=[]; chords=[]; notes=[]
barlines=[[38,41,45,41],[43,47,50,47],[48,52,55,47],[48,52,43,43],[45,48,40,36],[38,41,45,41],[43,47,50,47],[48,52,43,40]]
chord_names=['Dm7','G7','Cmaj7','Cmaj7','Am7','Dm7','G7','Cmaj7']
functions=['ii7','V7','Imaj7','Imaj7','vi7','ii7','V7','Imaj7']
for i,(title,explanation,change,criterion) in enumerate(stage_text,1):
    sid=f'stage-independence-014-{i:02}'
    pid=f'prog-independence-014-{i:02}-primary'
    stages.append({'id':sid,'lessonId':lesson['id'],'order':i,'title':title,'explanationMd':explanation,'task':f'Practica la secuencia completa de ocho compases a 72 BPM. {criterion}','changeFromPrevious':change,'successCriteria':[criterion],'simplifyHint':'Aísla primero un compás con metrónomo; después enlaza los ocho sin cambiar el pulso ni las notas no indicadas.','extendHint':'Toca manos separadas y vuelve a reunirlas manteniendo exactamente los onsets y duraciones escritos.'})
    progressions.append({'id':pid,'stageId':sid,'kind':'primary','order':1,'title':title,'keyTonic':'C','keyMode':'major','style':'jazz','bpm':72,'timeSignature':{'numerator':4,'denominator':4},'totalBars':8,'description':'Ocho compases Dm7–G7–Cmaj7–Cmaj7–Am7–Dm7–G7–Cmaj7. Walking LH a negras, una nota por beat y duración 1. Aproximaciones diatónicas F→G, B→C, B→C, G→A, C→D, F→G, B→C, E→D (loop). En etapa 03 beat 7: Db3 MIDI 49 cromático superior hacia C3 MIDI 48 en beat 8; no C# ascendente a D. RH: solo dos shells indicados por etapa, nunca melodía adicional.' ,'loopable':True})
    for b,(sym,fun) in enumerate(zip(chord_names,functions)):
        chords.append({'id':f'chord-independence-014-{i:02}-{b+1:03}','progressionId':pid,'order':b+1,'symbol':sym,'function':fun,'startBeat':b*4,'durationBeats':4})
    for b,row in enumerate(barlines):
        for beat,pitch in enumerate(row):
            if i>=3 and b==1 and beat==3: pitch=49
            notes.append({'id':f'note-independence-014-{i:02}-{b*4+beat+1:03}','progressionId':pid,'midi':pitch,'startBeat':b*4+beat,'durationBeats':1,'velocity':65,'role':'bass','hand':'left'})
    shells=[]
    if i in (1,2,3): shells=[(4+2/3,[59,65]),(28+2/3,[64,71])]
    if i in (4,5): shells=[(5+2/3,[59,65]),(28+2/3,[64,71])]
    if i==5: shells=[(24+2/3,[59,65]),(28+2/3,[64,71])]
    for onset,pitches in shells:
        for p in pitches:
            notes.append({'id':f'note-independence-014-{i:02}-rh-{len(notes):03}','progressionId':pid,'midi':p,'startBeat':onset,'durationBeats':1/3,'velocity':64,'role':'harmony','hand':'right'})
for filename,rows in [('stages',stages),('progressions',progressions),('chord-events',chords),('note-events',notes)]:
    text=json.dumps(rows,ensure_ascii=False,indent=2)+'\n'
    (out/f'{filename}.json').write_text(text)
    (checks/f'{filename}.json').write_text(text)
for i in range(1,6):
    pid=f'prog-independence-014-{i:02}-primary'
    midi=checks/f'{pid}.mid'
    subprocess.run([str(root/'lesson-content/.venv/bin/python'),str(root/'lesson-content/tools/scripts/curriculum.py'),'export-midi',pid,'--data',str(checks),'--output',str(midi)],check=True)
    (out/f'{pid}.mid').write_bytes(midi.read_bytes())
print('built five progressions and MIDI files')
