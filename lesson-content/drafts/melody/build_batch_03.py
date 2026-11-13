import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
CURRICULUM = ROOT.parents[1]


def read(name):
    return json.loads((ROOT / f'{name}.json').read_text(encoding='utf-8'))


def write(name, rows):
    (ROOT / f'{name}.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


sys.path.insert(0, str(CURRICULUM / 'tools' / 'scripts'))
spec = importlib.util.spec_from_file_location('audit_delivery', CURRICULUM / 'tools' / 'scripts' / 'audit_delivery.py')
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
register = json.loads((CURRICULUM / 'audits/batch-register.json').read_text(encoding='utf-8'))
approval = next(row for row in register if row['category'] == 'melody' and row['batch'] == 1)
files = ('lessons', 'stages', 'progressions', 'chord-events', 'note-events')
data = {name: read(name) for name in files}
if audit.subset_fingerprint(data, set(approval['fingerprint']['lessonIds'])) != approval['fingerprint']:
    raise ValueError('Melody 001–003 no coincide con su huella aprobada')

ids = {'lesson-melody-007', 'lesson-melody-008', 'lesson-melody-009'}
old_stages = {r['id'] for r in data['stages'] if r['lessonId'] in ids}
old_progs = {r['id'] for r in data['progressions'] if r['stageId'] in old_stages}
for key, field in [('lessons', 'id'), ('stages', 'lessonId'), ('progressions', 'stageId'), ('chord-events', 'progressionId'), ('note-events', 'progressionId')]:
    excluded = ids if key in ('lessons', 'stages') else old_stages if key == 'progressions' else old_progs
    data[key] = [r for r in data[key] if r[field] not in excluded]

lessons_all = json.loads((CURRICULUM / 'approved/lessons.json').read_text(encoding='utf-8'))
lessons = [r for r in lessons_all if r['id'] in ids]
if len(lessons) != 3:
    raise ValueError('Deben existir exactamente M007–M009')

# Cada fila: notas de melodía (beat, MIDI, duración). Ritmo, bordaduras y cromatismos definidos a mano.
melodies = {
    '007': [
        [(0,64,1),(1,67,1),(2,69,1),(4,67,1),(5,64,1),(6,62,1),(8,64,1),(9,67,1),(10,69,1),(12,67,1),(13,64,1),(14,62,1)],
        [(0,64,1),(1.5,67,.5),(2,69,2),(4,67,1),(5,64,1),(6,62,1),(8,64,1),(9.5,67,.5),(10,69,2),(12,67,1),(13,64,1),(14,62,1)],
        [(0,64,1),(1.5,67,.5),(2,69,2),(4,67,1),(5,64,1),(6.5,62,.5),(8,64,1),(9.5,67,.5),(10,69,2),(12,67,1),(13,64,1),(14.5,62,.5)],
        [(0,64,1),(1.5,67,.5),(2,69,2),(4,67,1),(5,64,1),(6.5,62,.5),(8,64,1),(9.5,67,.5),(10,69,2),(12,67,1),(13,64,1),(14,62,.5)],
    ],
    '008': [
        [(0,64,2),(4,69,2),(8,65,2),(12,67,2)],
        [(0,64,1),(1,62,1),(2,64,1),(4,69,1),(5,67,1),(6,69,1),(8,65,1),(9,64,1),(10,65,1),(12,67,1),(13,65,1),(14,67,1)],
        [(0,64,1),(1,66,1),(2,64,1),(4,69,1),(5,71,1),(6,69,1),(8,65,1),(9,67,1),(10,65,1),(12,67,1),(13,69,1),(14,67,1)],
        [(0,64,1),(1,62,1),(2,64,1),(4,69,1),(5,67,1),(6,69,1),(8,65,1),(9,67,1),(10,65,1),(12,67,1),(13,65,1),(14,67,1)],
    ],
    '009': [
        [(0,64,2),(4,60,2),(8,57,2),(12,59,2)],
        [(0,64,2),(3.5,59,.5),(4,60,2),(8,57,2),(12,59,2)],
        [(0,64,2),(3.5,59,.5),(4,60,2),(7.5,56,.5),(8,57,2),(12,59,2)],
        [(0,64,2),(3.5,59,.5),(4,60,2),(7.5,56,.5),(8,57,2),(11.5,58,.5),(12,59,2),(15.5,63,.5)],
    ],
}
chords = {
    '007': [('Cmaj7','Imaj7',48),('Am7','vi7',45),('Fmaj7','IVmaj7',41),('G7','V7',43)],
    '008': [('Cmaj7','Imaj7',48),('Am7','vi7',45),('Fmaj7','IVmaj7',41),('G7','V7',43)],
    '009': [('Cmaj7','Imaj7',48),('Am7','vi7',45),('Fmaj7','IVmaj7',41),('G7','V7',43)],
}
content = {
 '007': {
  'titles':['Motivo a negras','Alargar sin cambiar alturas','Desplazar una pausa','Variar por cuenta propia'],
  'changes':['A: motivo de alturas E4–G4–A4–G4–E4–D4, con huecos y cuatro acordes I–vi–IV–V.','B frente a A: conserva cada altura y orden; alarga A4 y adelanta G4 medio pulso, redistribuyendo el silencio.','Mantén las alturas; desplaza el hueco del segundo compás a después de D4 y deja el resto rítmico reconocible.','Diseña otra variación solo rítmica; conserva exactamente las alturas del motivo y los cambios I–vi–IV–V.'],
  'explanations':['A presenta el contorno E–G–A–G–E–D sobre I–vi–IV–V; los espacios son parte del motivo.','A/B: las alturas y acordes no cambian; A4 dura dos negras y G4 entra en 1.5.','A/B: cambia únicamente la colocación de una pausa; compara el mismo contorno y el mismo ciclo armónico.','La referencia conserva el material tonal; inventa otra distribución de duración y silencios sin añadir alturas.'],
  'tasks':['Toca y canta el motivo; marca los silencios contando negras.','Compara A y B y señala qué nota se alargó y dónde entra G4.','Toca ambas versiones sin alterar ninguna altura; identifica el hueco desplazado.','Inventa una variación rítmica, anótala en beats y ejecútala sobre los mismos cuatro acordes.'],
  'criteria':[['Reconozco el contorno E–G–A–G–E–D','El pulso sigue regular en los silencios'],['Las alturas coinciden con A','A4 se alarga y G4 entra en 1.5'],['El contorno y alturas permanecen','La pausa cambia de ubicación'],['La variación usa solo alturas del motivo','Puedo repetirla sobre I–vi–IV–V']],
  'simple':['Toca E4, G4, A4, G4, E4, D4 a negras, una nota por pulso.','Practica solo A4@2–G4@1.5 con metrónomo lento.','Vuelve a A y cambia solo una pausa, sin mover las alturas.','Conserva cuatro notas del motivo y crea un único silencio nuevo.'],
  'extend':'Crea una segunda variación rítmica y alterna A/B sin cambiar alturas ni progresión.'},
 '008': {
  'titles':['Apoyos largos','Vecina inferior','Vecina superior','Elige dirección y resuelve'],
  'changes':['A: notas estructurales E4, A4, F4 y G4, sostenidas dos negras al inicio de cada acorde.','B frente a A: inserta una vecina diatónica inferior y vuelve a la misma nota: E–D–E, A–G–A, F–E–F, G–F–G.','Cambia dirección: sustituye las vecinas inferiores por vecinas superiores diatónicas, siempre regresando al apoyo original.','Escoge superior o inferior para cada apoyo; cada salida debe volver a la misma altura, sin alterar armonía.'],
  'explanations':['La línea muestra apoyos del acorde y deja espacio después de cada nota larga.','D–E, G–A, E–F y F–G son movimientos diatónicos de grado conjunto de ida y regreso.','F–E–F sobre Cmaj7, B–A–B sobre Am7, G–F–G sobre Fmaj7 y A–G–A sobre G7 retornan al apoyo.','La vecina diatónica cambia momentáneamente el apoyo y resuelve a la misma nota, no a un destino nuevo.'],
  'tasks':['Toca cada apoyo y cuenta las dos negras antes de la siguiente entrada.','Toca apoyo–nota inferior–mismo apoyo; comprueba que la última altura repite la primera.','Compara dirección superior con inferior y verifica el retorno exacto.','Elige una dirección por acorde, escribe las alturas y comprueba el regreso antes de tocar.'],
  'criteria':[['Reconozco E4, A4, F4, G4 como apoyos','Dejo el espacio escrito'],['Cada vecina es diatónica e inferior','La nota final repite el apoyo inicial'],['Cada vecina es diatónica y superior','La resolución regresa a idéntica nota'],['La decisión de dirección es explícita','Cada bordadura retorna antes de otro apoyo']],
  'simple':['Toca solo E4, A4, F4 y G4 en el primer pulso de cada acorde.','Practica cada pareja inferior–apoyo por separado, sin bajo.','Practica solo F4–E4–F4 y B3–A3–B3.','Elige una sola bordadura completa y repítela lentamente.'],
  'extend':'Escribe una bordadura propia para cada acorde; verifica escala diatónica y retorno a la misma nota.'},
 '009': {
  'titles':['Terceras objetivo','Aproximar E','Resolver C y A','Cuatro llegadas cromáticas'],
  'changes':['A: terceras E4, C4, A3 y B3 en Cmaj7, Am7, Fmaj7 y G7.','B frente a A: añade B3@3.5 antes de C4@4, aproximación cromática inferior de medio pulso; conserva el objetivo.','Añade G#3@7.5–A3@8; junto a B3–C4, son dos aproximaciones cromáticas inferiores de medio pulso.','Añade A#3@11.5–B3@12 y D#4@15.5–E4@0 al repetir el loop. Una aproximación por acorde, nunca una cadena.'],
  'explanations':['A fija la tercera de cada acorde como destino; la izquierda toca raíces largas y la línea es monofónica.','B3 es cromática inferior a C4; ocupa la parte débil y resuelve por semitono al entrar Am7.','G#3→A3 sobre Fmaj7 completa la tercera aproximación; todas duran medio pulso y llegan a las terceras anunciadas.','A#3→B3 prepara la tercera de G7; D#4@15.5 prepara E4@0 del siguiente ciclo. Cada cromatismo resuelve exacto.'],
  'tasks':['Toca E–C–A–B en los cambios; nombra la tercera antes de cada ataque.','Compara C4 directa con B3–C4; mantén el objetivo en el beat 4.','Añade G#3–A3 sobre Fmaj7; conserva B3–C4 y no desplaces llegadas.','Toca B–C, G#–A, A#–B y D#–E en la vuelta; cuenta cada ataque débil y resuelve en medio pulso.'],
  'criteria':[['Cada objetivo es tercera del acorde escrito','La línea no añade otra altura'],['B está un semitono bajo C','Resuelve en beat 4 y dura medio pulso'],['B→C y G#→A resuelven exacto','Cada nota cromática dura medio pulso'],['Una aproximación por acorde','La resolución coincide con la tercera objetivo']],
  'simple':['Toca solo las cuatro terceras en los inicios de acorde.','Aísla D#4@3.5–E4@4, sin acompañamiento.','Practica una pareja cromática a la vez, con metrónomo.','Usa solo D#–E en el primer acorde; deja los demás objetivos directos.'],
  'extend':'Elige otro registro para las mismas cuatro terceras y conserva cada aproximación inferior de un semitono.'}
}

for lesson in lessons:
    n = lesson['id'][-3:]
    for order, melody in enumerate(melodies[n], 1):
        sid = f'stage-melody-{n}-{order:02d}'
        pid = f'prog-melody-{n}-{order:02d}-primary'
        c = content[n]
        data['stages'].append({'id':sid,'lessonId':lesson['id'],'order':order,'title':c['titles'][order-1],
            'explanationMd':c['explanations'][order-1]+' Referencia a dos manos: bajo monofónico y melodía; no son bloques armónicos completos.',
            'task':c['tasks'][order-1],'changeFromPrevious':c['changes'][order-1],'successCriteria':c['criteria'][order-1],
            'simplifyHint':c['simple'][order-1],'extendHint':c['extend']})
        data['progressions'].append({'id':pid,'stageId':sid,'kind':'primary','order':1,'title':lesson['title'],'keyTonic':'C','keyMode':'major',
            'style':lesson['styleTags'][0],'bpm':72,'timeSignature':{'numerator':4,'denominator':4},'totalBars':4,
            'description':'Plan explícito de bajo fundamental y melodía monofónica; armonía parcial, no voicing completo.','loopable':True})
        for i,(symbol,function,root) in enumerate(chords[n]):
            data['chord-events'].append({'id':f'chord-melody-{n}-{order:02d}-primary-{i+1:03d}','progressionId':pid,'order':i+1,'symbol':symbol,'function':function,'startBeat':i*4,'durationBeats':4})
            data['note-events'].append({'id':f'note-melody-{n}-{order:02d}-primary-{i+1:04d}','progressionId':pid,'midi':root,'startBeat':i*4,'durationBeats':4,'velocity':58,'role':'bass','hand':'left'})
        for i,(beat,pitch,duration) in enumerate(melody,5):
            data['note-events'].append({'id':f'note-melody-{n}-{order:02d}-primary-{i:04d}','progressionId':pid,'midi':pitch,'startBeat':beat,'durationBeats':duration,'velocity':76,'role':'melody','hand':'right'})
    data['lessons'].append(lesson)

for name, rows in data.items():
    write(name, rows)
if audit.subset_fingerprint({name:read(name) for name in files}, set(approval['fingerprint']['lessonIds'])) != approval['fingerprint']:
    raise ValueError('La huella de melody 001–003 cambió')
print('Preservadas 001–006; compuestas M007–M009.')
