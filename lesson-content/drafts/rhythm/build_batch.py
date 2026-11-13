#!/usr/bin/env python3
"""Serializa planes explícitos del lote rhythm 001–003 y conserva el piloto aprobado."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / 'drafts' / 'rhythm'
PILOT = ROOT / 'examples' / 'pilot-data'

def load(path):
    return json.loads(path.read_text(encoding='utf-8'))

def save(path, rows):
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

def add_note(rows, lesson, stage, pid, pitch, start, duration, role, hand, velocity):
    order = lesson['orderInCategory']
    index = sum(1 for row in rows if row['progressionId'] == pid) + 1
    rows.append({'id': f'note-rhythm-{order:03d}-{stage:02d}-primary-{index:04d}',
                 'progressionId': pid, 'midi': pitch, 'startBeat': start,
                 'durationBeats': duration, 'velocity': velocity, 'role': role, 'hand': hand})

lessons_all = load(ROOT / 'approved' / 'lessons.json')
lessons = {row['id']: row for row in lessons_all}
selected = ['lesson-rhythm-001', 'lesson-rhythm-002', 'lesson-rhythm-003']

plans = {
 'lesson-rhythm-001': {
  'style': 'pop', 'tonic': 'C', 'chords': [('C','Cmaj','I',[48,[60,64,67]]),('G','Gmaj','V',[43,[59,62,67]]),('Am','Am','vi',[45,[57,60,64]]),('F','Fmaj','IV',[41,[57,60,65]])],
  'stages': [
   ('Pulso en cuatro compases','A: ataca el bajo en cada negra; derecha: tríada larga al inicio del compás. Cuenta cuatro negras sin acelerar.','Presentación: cuatro compases I–V–vi–IV con bajo a negras y tríadas largas.','Mantengo cuatro negras regulares por compás y no acorto la tríada derecha.'),
   ('Pulso compartido','Compara con etapa 01: el bajo sigue a negras y la derecha reataca la tríada en los tiempos musicales uno y tres, desplazamientos locales 0 y 2 (blancas).','Se añaden reataques derechos en beat 2 local de cada compás; el bajo mantiene sus cuatro negras.','El bajo conserva cuatro ataques regulares aunque la derecha rearticule en blancas.'),
   ('Respirar arriba','A = base sostenida de la etapa 01: bajo a negras y tríada larga al inicio de cada compás. B = esta etapa: reinicia esa base y retira solo la tríada del compás 3; cuenta sus cuatro pulsos mientras el bajo continúa.','Se vuelve explícitamente a la base sostenida de la etapa 01; sobre ella se omite solo la tríada derecha del compás 3. El bajo continúa a negras y el ciclo conserva sus 16 pulsos.','La derecha calla el compás elegido y reentra en el uno sin mover el pulso.'),
   ('Elegir dónde respirar','A referencia: etapa 01. Diseña una vuelta con una tríada derecha menos, en cualquier compás; la izquierda sigue a negras durante los cuatro compases.','Autonomía: la referencia mantiene I–V–vi–IV y bajo estable; el estudiante elige el compás de silencio derecho.','Puedo elegir un compás para respirar arriba y completar cuatro compases sin acortar el ciclo.')
  ],
  'rhythm': 'pulse'
 },
 'lesson-rhythm-002': {
  'style': 'pop', 'tonic': 'C', 'chords': [('C','Cmaj','I',[48,[60,64,67]]),('G','Gmaj','V',[43,[59,62,67]])],
  'stages': [
   ('Oír la rejilla con negras','Durante dos compases por acorde, toca bajo en blancas y una tríada derecha en negras. Cuenta también las subdivisiones entre ataques.','Base: C dos compases y G dos; derecha en negras, izquierda en blancas para establecer la cuadrícula.','Sostengo blancas izquierdas y cuento las subdivisiones regulares entre negras derechas.'),
   ('Corcheas continuas','Compara con etapa 01: la derecha toca dos ataques por negra durante los cuatro compases; izquierda sigue en blancas.','Solo cambia la subdivisión derecha: de negras a corcheas continuas sobre la misma armonía y bajo.','Las corcheas mantienen distancia regular y el bajo no cambia de patrón.'),
   ('Dejar dos huecos','Compara A (corcheas continuas, etapa 02) con B: omite dos corcheas derechas en cada compás, sin desplazar las restantes.','Se eliminan ataques derechos en beat 1& y 3&; la rejilla continúa por debajo de los silencios.','Puedo contar cada hueco y las notas restantes no se adelantan ni se retrasan.'),
   ('Elegir silencios','A = etapa 02, corcheas continuas. B = esta referencia (etapa 04), con huecos en los tiempos musicales dos y cuatro de cada compás (desplazamientos locales 1 y 3). En tu vuelta puedes elegir otras dos corcheas; conserva el bajo en blancas y la rejilla.','A es la corchea continua de la etapa 02; B ilustra huecos en tiempos musicales dos/cuatro (offsets locales 1/3). Es una elección de referencia, no las posiciones obligatorias del estudiante.','Mantengo la subdivisión imaginada durante dos silencios elegidos y vuelvo a entrar a tiempo.')
  ],
  'rhythm': 'subdivision'
 },
 'lesson-rhythm-003': {
  'style': 'pop', 'tonic': 'C', 'chords': [('C','Cmaj','I',[48,[60,64,67]]),('G','Gmaj','V',[43,[59,62,67]]),('Am','Am','vi',[45,[57,60,64]]),('F','Fmaj','IV',[41,[57,60,65]])],
  'stages': [
   ('Acordes en el uno','A: por cada compás toca bajo en uno y tres, y una tríada derecha corta solo en uno. Cuenta los cuatro pulsos completos.','Base de contraste: I–V–vi–IV, bajo en uno/tres y acorde derecho en uno; aún no hay backbeat completo.','El bajo conserva uno y tres, y puedo contar dos y cuatro sin atacarlos.'),
   ('Backbeat en dos y cuatro','Compara A de etapa 01 con B: desplaza ataques derechos de cada uno a beats 1 y 3; conserva bajo en uno y tres.','Los ataques derechos pasan a beats 1 y 3 locales (tiempos 2 y 4); una tónica sostenida a través del ciclo aísla el patrón.','Oigo el acorde en dos y cuatro de cada compás y el bajo permanece en uno/tres.'),
   ('Sostener el patrón al cambiar acorde','Mantén el backbeat en beats 1 y 3 locales en los cuatro compases; la armonía cambia en cada uno, el patrón no.','Se pasa de la tónica sostenida de la etapa 02 a I–V–vi–IV; el backbeat dos/cuatro no se mueve.','Cada cambio armónico ocurre con bajo en uno; los acordes siguen en dos/cuatro.'),
   ('Elegir un descanso','A referencia: etapa 03. Elige un único compás donde omitir el acorde de cuatro; conserva el de dos y todos los bajos uno/tres.','Autonomía: retirar el ataque del cuatro en un compás elegido convierte el patrón fijo en una decisión de frase sin borrar el backbeat.','Puedo señalar el compás de descanso y volver a dos/cuatro sin perder el pulso.')
  ],
  'rhythm': 'style-patterns'
 }
}

stages=[]; progressions=[]; chords=[]; notes=[]
for lesson_id in selected:
    lesson=lessons[lesson_id]; plan=plans[lesson_id]
    save(WORK/'lessons.json', []) if False else None
    for si,(title,explanation,change,criterion) in enumerate(plan['stages'],1):
        sid=f'stage-rhythm-{lesson["orderInCategory"]:03d}-{si:02d}'
        pid=f'prog-rhythm-{lesson["orderInCategory"]:03d}-{si:02d}-primary'
        task={
          'lesson-rhythm-001':'Toca los cuatro compases a 80 BPM. Mantén el bajo en negras y realiza los cambios indicados sin acelerar.',
          'lesson-rhythm-002':'Toca cuatro compases a 80 BPM. Bajo en blancas; completa la tarea rítmica derecha contando la subdivisión.',
          'lesson-rhythm-003':'Toca cuatro compases a 80 BPM. Bajo en uno y tres; ubica los acordes derechos en los tiempos señalados.'
        }[lesson_id]
        stage_title = 'Tónica estable: acorde en uno' if lesson_id=='lesson-rhythm-003' and si==1 else title
        if lesson_id=='lesson-rhythm-003' and si==1:
            explanation='A = tónica C sostenida durante los cuatro compases, bajo en los tiempos musicales uno/tres y tríada corta en uno. Esta base deja el mismo bajo y armonía que B de la etapa 02 para aislar el cambio de colocación a dos/cuatro.'
            change='Presentación de la base de contraste: un único ChordEvent C/I cubre 0–16; bajo C3 local 0/2 en cada compás y RH C mayor local 0, duración 0.5.'
            criterion='Identifico el pulso de bajo en uno/tres y la tríada breve en uno sin cambiar la tónica.'
        stages.append({'id':sid,'lessonId':lesson_id,'order':si,'title':stage_title,'explanationMd':explanation,'task':task,'changeFromPrevious':change,'successCriteria':[criterion],'simplifyHint':'Baja el tempo y practica primero cada mano por separado.','extendHint':'Repite cuatro vueltas seguidas manteniendo el pulso interno.'})
        progression_title = 'C sostenido: acorde en uno' if lesson_id=='lesson-rhythm-003' and si==1 else title
        progression_description = ('C/I continuo durante 16 beats para comparar el acorde en uno de 003-01 con el backbeat de 003-02 sin cambiar armonía ni bajo.' if lesson_id=='lesson-rhythm-003' and si==1 else f'{lesson["title"]}: ejemplo pop específico de etapa, cuatro compases.')
        progressions.append({'id':pid,'stageId':sid,'kind':'primary','order':1,'title':progression_title,'keyTonic':'C','keyMode':'major','style':'pop','bpm':80,'timeSignature':{'numerator':4,'denominator':4},'totalBars':4,'description':progression_description, 'loopable':True})
        # Harmonic plan: four bars for lessons 001/003; two chords, two bars each, for 002.
        chord_plan=plan['chords']
        if lesson_id=='lesson-rhythm-003' and si in (1,2):
            chord_plan=plan['chords'][:1]
        for ci,(sym,quality,func,(bass,rh)) in enumerate(chord_plan,1):
            start=(ci-1)*4 if lesson_id!='lesson-rhythm-002' else (ci-1)*8
            dur=16 if lesson_id=='lesson-rhythm-003' and si in (1,2) else (4 if lesson_id!='lesson-rhythm-002' else 8)
            chords.append({'id':f'chord-rhythm-{lesson["orderInCategory"]:03d}-{si:02d}-primary-{ci:03d}','progressionId':pid,'order':ci,'symbol':sym+('maj7' if False else ''),'function':func,'startBeat':start,'durationBeats':dur})
        for bi in range(4):
            ci=0 if lesson_id=='lesson-rhythm-003' and si in (1,2) else (bi if lesson_id!='lesson-rhythm-002' else bi//2)
            sym,quality,func,(bass,rh)=chord_plan[ci]
            bar=bi*4
            if lesson_id=='lesson-rhythm-001':
                # Stable bass quarters in every bar; RH long triad except chosen stage-specific rest.
                for beat in range(4): add_note(notes,lesson,si,pid,bass,bar+beat,1,'bass','left',72)
                if si==2:
                    for beat in (0,2):
                        for pitch in rh: add_note(notes,lesson,si,pid,pitch,bar+beat,2,'harmony','right',66)
                elif not (si==3 and bi==2) and not (si==4 and bi==1):
                    for pitch in rh: add_note(notes,lesson,si,pid,pitch,bar,4,'harmony','right',66)
            elif lesson_id=='lesson-rhythm-002':
                for beat in (0,2): add_note(notes,lesson,si,pid,bass,bar+beat,2,'bass','left',72)
                for eighth in range(8):
                    # Stage 01 uses quarter notes; later stages fill or selectively leave the eighth-note grid.
                    omit=(si==1 and eighth % 2 == 1) or (si==3 and eighth in (1,5)) or (si==4 and eighth in (2,6))
                    if not omit:
                        for pitch in rh: add_note(notes,lesson,si,pid,pitch,bar+eighth*0.5,0.5,'harmony','right',62)
            else:
                if lesson_id=='lesson-rhythm-003' and si==2:
                    ci=0
                    sym,quality,func,(bass,rh)=chord_plan[0]
                for beat in (0,2): add_note(notes,lesson,si,pid,bass,bar+beat,1,'bass','left',72)
                for beat in ((1,3) if si>1 else (0,)):
                    if not (si==4 and bi==2 and beat==3):
                        for pitch in rh: add_note(notes,lesson,si,pid,pitch,bar+beat,0.5,'harmony','right',64)

def add_note(rows,lesson,stage,pid,pitch,start,duration,role,hand,velocity):
    order=lesson['orderInCategory']
    index=sum(1 for row in rows if row['progressionId']==pid)+1
    rows.append({'id':f'note-rhythm-{order:03d}-{stage:02d}-primary-{index:04d}','progressionId':pid,'midi':pitch,'startBeat':start,'durationBeats':duration,'velocity':velocity,'role':role,'hand':hand})

# Keep exact approved lesson 004 and musical records from the frozen pilot snapshot.
old_lessons=load(WORK/'lessons.json')
old_ids={'lesson-rhythm-004'}
old_lessons=[row for row in old_lessons if row['id'] in old_ids]
for row in selected:
    pass
for name, generated in [('stages',stages),('progressions',progressions),('chord-events',chords),('note-events',notes)]:
    frozen=load(PILOT/f'{name}.json')
    # Prevent accidental mutation of the approved pilot partition.
    current=load(WORK/f'{name}.json')
    frozen_lesson_rows=[r for r in frozen if (r.get('lessonId')=='lesson-rhythm-004' or r.get('stageId','').startswith('stage-rhythm-004') or r.get('progressionId','').startswith('prog-rhythm-004'))]
    current_rows=[r for r in current if (r.get('lessonId')=='lesson-rhythm-004' or r.get('stageId','').startswith('stage-rhythm-004') or r.get('progressionId','').startswith('prog-rhythm-004'))]
    assert current_rows==frozen_lesson_rows, f'approved pilot changed in {name}'
    save(WORK/f'{name}.json',frozen_lesson_rows+generated)
# Exact design copies: new lessons plus already approved 004.
copy=[lessons[x] for x in ['lesson-rhythm-001','lesson-rhythm-002','lesson-rhythm-003','lesson-rhythm-004']]
save(WORK/'lessons.json',copy)
