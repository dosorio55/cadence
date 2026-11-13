import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
CURRICULUM = ROOT.parents[1]
DATA = CURRICULUM / 'approved'


def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))


def write_json(path, rows):
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def verify_batch_one(existing):
    sys.path.insert(0, str(CURRICULUM / 'tools' / 'scripts'))
    spec = importlib.util.spec_from_file_location(
        'audit_delivery', CURRICULUM / 'tools' / 'scripts' / 'audit_delivery.py'
    )
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)

    register = read_json(CURRICULUM / 'audits' / 'batch-register.json')
    approval = next(row for row in register
                    if row['category'] == 'melody' and row['batch'] == 1)
    lesson_ids = set(approval['fingerprint']['lessonIds'])
    actual = audit.subset_fingerprint(existing, lesson_ids)
    if actual != approval['fingerprint']:
        raise ValueError('El lote melody 001–003 no coincide con su aprobación congelada')


existing = {
    name: read_json(ROOT / f'{name}.json')
    for name in ('lessons', 'stages', 'progressions', 'chord-events', 'note-events')
}
verify_batch_one(existing)
new_lesson_ids = {'lesson-melody-004', 'lesson-melody-005', 'lesson-melody-006'}
old_stage_ids = {row['id'] for row in existing['stages'] if row['lessonId'] in new_lesson_ids}
old_progression_ids = {row['id'] for row in existing['progressions'] if row['stageId'] in old_stage_ids}
existing['lessons'] = [row for row in existing['lessons'] if row['id'] not in new_lesson_ids]
existing['stages'] = [row for row in existing['stages'] if row['lessonId'] not in new_lesson_ids]
existing['progressions'] = [row for row in existing['progressions'] if row['stageId'] not in old_stage_ids]
existing['chord-events'] = [row for row in existing['chord-events'] if row['progressionId'] not in old_progression_ids]
existing['note-events'] = [row for row in existing['note-events'] if row['progressionId'] not in old_progression_ids]

all_lessons = read_json(DATA / 'lessons.json')
new_lessons = [row for row in all_lessons
               if row['id'] in {'lesson-melody-004', 'lesson-melody-005', 'lesson-melody-006'}]
if len(new_lessons) != 3:
    raise ValueError('No se encontraron exactamente las fichas aprobadas M004–M006')

plans = {
    '004': [
        [(0, 65, 1), (4, 59, 1), (8, 67, 1), (12, 64, 1)],
        [(0, 65, 1), (3.5, 60, .5), (4, 59, 1), (8, 67, 1), (12, 64, 1)],
        [(0, 65, 1), (3.5, 60, .5), (4, 59, 1), (7.5, 69, .5), (8, 67, 1), (12, 64, 1)],
        [(0, 65, 1), (3.5, 60, .5), (4, 59, 1), (7.5, 69, .5), (8, 67, 1), (11.5, 65, .5), (12, 64, 1)],
    ],
    '005': [
        [(0,64,1),(1,67,1),(2,64,1),(3,67,1),
         (4,62,1),(5,65,1),(6,67,1),(7,59,1),
         (8,64,1),(9,67,1),(10,69,1),(11,67,1),
         (12,67,1),(13,64,1),(14,67,1),(15,60,1)],
        [(0,64,1),(1,67,1),(2,64,1),(3,67,1),
         (4,62,1),(5,65,1),(6,67,1),
         (8,64,1),(9,67,1),(10,69,1),(11,67,1),
         (12,67,1),(13,64,1),(14,67,1),(15,60,1)],
        [(0,64,1),(1,67,1),(2,64,1),(3,67,1),
         (4,62,1),(5,65,1),(6,67,1),
         (8,64,1),(9,67,1),(10,72,1),(11,67,1),
         (12,67,1),(13,64,1),(14,67,1),(15,60,1)],
        [(0,64,1),(1,67,1),(2,64,1),(3,67,1),
         (4,62,1),(5,65,1),(6,67,1),
         (8,64,1),(9,67,1),(10,72,1),(11,67,1),
         (12,67,1),(13,64,1),(14,67,1),(15,64,1)],
    ],
    '006': [
        [(0,60,1),(4,57,1),(8,53,1),(12,55,1)],
        [(0,64,1),(4,57,1),(8,53,1),(12,55,1)],
        [(0,64,1),(4,60,1),(8,53,1),(12,55,1)],
        [(0,64,1),(4,60,1),(8,57,1),(12,55,1)],
        [(0,64,1),(4,60,1),(8,57,1),(12,59,1)],
    ],
}

chord_plans = {
    '004': [('Dm7','ii7',50),('G7','V7',43),('Cmaj7','Imaj7',48),('Cmaj7','Imaj7',48)],
    '005': [('Cmaj7','Imaj7',48),('G7','V7',43),('Am7','vi7',45),('Cmaj7','Imaj7',48)],
    '006': [('Cmaj7','Imaj7',48),('Am7','vi7',45),('Fmaj7','IVmaj7',41),('G7','V7',43)],
}

stage_content = {
    '004': {
        'titles': ['Objetivos directos','Prepara B con C','Prepara G con A','Elige otra llegada'],
        'changes': [
            'Presentación A: notas objetivo F4, B3, G4 y E4 en los inicios 0, 4, 8 y 12 sobre ii–V–I–I.',
            'B frente a A: añade solo C4@3.5; resuelve por semitono diatónico descendente a B3 justo en el ataque de G7.',
            'Conserva C4–B3 y añade solo A4@7.5; resuelve por grado conjunto a G4 en el ataque de Cmaj7.',
            'Mantén las dos llegadas y añade solo F4@11.5, que resuelve a E4 en el último ataque de Cmaj7; elige otros objetivos si lo deseas.',
        ],
        'explanations': [
            'A: cada nota objetivo entra con su acorde; la izquierda marca solo las raíces para dejar espacio a la línea.',
            'A/B: C4 es la vecina diatónica superior de B3 y cae exactamente cuando entra G7; el acorde y el bajo no cambian.',
            'A/B: añade A4 antes de G4 en la nueva frontera; escucha la llegada prevista sin adelantarla.',
            'La referencia prepara E4 con F4 justo antes del ataque; puedes escoger otra llegada y conservar la vecina superior diatónica.',
        ],
        'tasks': [
            'Toca primero los cuatro objetivos en el inicio de cada acorde; canta el cambio de compás.',
            'Compara llegada directa B3 con C4–B3; no muevas el ataque de B3.',
            'Añade A4–G4 y conserva intacta la preparación anterior.',
            'Prueba la llegada final de referencia y luego inventa otra con su propio destino.',
        ],
        'criteria': [
            ['Cada objetivo entra con el acorde previsto','La izquierda permanece sencilla'],
            ['C4 está en parte débil','C4 resuelve a B3 en el ataque de G7'],
            ['A4 resuelve a G4 en el ataque de Cmaj7','La llegada no se adelanta'],
            ['La vecina es diatónica y superior','El objetivo cae en el ataque previsto'],
        ],
        'simplify': [
            'Deja solo las raíces en la izquierda y toca en la derecha los cuatro objetivos al inicio de cada compás.',
            'Aísla C4@3.5–B3@4 y conserva B3 en el ataque de G7.',
            'Practica C4–B3 y A4–G4 por separado antes de unirlos.',
            'Usa una sola vecina superior y su objetivo; deja las otras llegadas directas.',
        ],
        'extend': 'Elige otro objetivo en la progresión y prepara su ataque con una vecina diatónica superior.',
    },
    '005': {
        'titles': ['Una línea sin respirar','Pregunta y pausa','Respuesta transformada','Cierre propio'],
        'changes': [
            'Presentación: línea continua de cuatro compases; los compases 1–2 plantean la pregunta y 3–4 responden con notas relacionadas, sin pausa.',
            'Frente a 01, retira solo B3@7: queda una pausa real de una negra entre la pregunta y la respuesta.',
            'Conserva la pausa y cambia solo A4@10 por C5; la respuesta se aparta de la pregunta sin perder el pulso.',
            'Mantén pregunta, pausa y respuesta; cambia solo el cierre C4@15 por E4, otra llegada estable sobre Cmaj7.',
        ],
        'explanations': [
            'Escucha los dos primeros compases como pregunta y los dos últimos como respuesta todavía enlazada, sin respirar.',
            'A/B: la pregunta termina en G4; el silencio de beat 7 deja una negra completa antes de la respuesta en beat 8.',
            'A/B: C5 en la respuesta cambia una sola altura y pertenece a Am7; el resto de la frase permanece.',
            'E4 cierra sobre Cmaj7 sin ser la única respuesta posible; puedes elegir otra nota estable para terminar.',
        ],
        'tasks': [
            'Toca la línea seguida y marca con la voz dónde empiezan sus dos mitades.',
            'Cuenta el silencio completo entre beat 7 y beat 8; no adelantes la respuesta.',
            'Compara A4 y C5 en la respuesta sin alterar el resto de la pregunta.',
            'Prueba el cierre E4 y luego elige una nota estable propia sobre el acorde final.',
        ],
        'criteria': [
            ['Distingo los primeros dos compases de los últimos dos','Mantengo el pulso continuo'],
            ['Hay una negra completa de silencio','La respuesta entra en beat 8'],
            ['La pausa se mantiene','La respuesta conserva relación con la pregunta'],
            ['La respuesta dura dos compases','El cierre es estable y no lo considero único'],
        ],
        'simplify': [
            'Toca solo la primera y última nota de cada compás, sin introducir la pausa todavía.',
            'Toca el inicio y cierre de pregunta y respuesta; conserva la pausa de una negra.',
            'Cambia solo A4 por C5 y mantén intactos el ritmo y el silencio.',
            'Responde con pocas notas y conserva la pausa y el cierre estable.',
        ],
        'extend': 'Conserva la pausa y transforma una nota de la respuesta sin perder su vínculo con la pregunta.',
    },
    '006': {
        'titles': ['Raíces de referencia','Primera tercera real','Tercera de Am7','Tercera de Fmaj7','Tercera de G7: elige el registro'],
        'changes': [
            'Presentación: una raíz al inicio de cada acorde: C4 sobre C, A3 sobre Am, F3 sobre F y G3 sobre G.',
            'Frente a 01, cambia solo C4 por E4: E es la tercera real de Cmaj7; las otras raíces siguen como referencia.',
            'Frente a 02, cambia solo A3 por C4: C es la tercera real de Am7; F3 y G3 siguen como raíces.',
            'Frente a 03, cambia solo F3 por A3: A es la tercera real de Fmaj7; G3 sigue como raíz.',
            'Frente a 04, cambia solo G3 por B3: B es la tercera real de G7. Mapa completo C→E, A→C, F→A, G→B; elige tus octavas.',
        ],
        'explanations': [
            'A: las notas son las raíces impresas en cada acorde, no terceras inferidas.',
            'A/B: en Cmaj7, C es raíz y E es tercera; verifica ambas alturas contra el símbolo y el bajo.',
            'A/B: en Am7, A es raíz y C es tercera; los otros dos compases aún usan raíces.',
            'A/B: en Fmaj7, F es raíz y A es tercera; el último compás todavía muestra la raíz G.',
            'En G7, G es raíz y B es tercera. La referencia muestra una ruta posible; elige registro y frase sin cambiar el acorde.',
        ],
        'tasks': [
            'Canta cada raíz junto al nombre del acorde antes de tocarla.',
            'Compara C4 y E4 sobre Cmaj7; identifica la raíz y la tercera reales.',
            'Compara A3 y C4 sobre Am7; nombra raíz y tercera antes de tocar.',
            'Compara F3 y A3 sobre Fmaj7; no cambies las otras llegadas.',
            'Comprueba G–B en G7 y escoge octavas cómodas para las cuatro terceras.',
        ],
        'criteria': [
            ['Identifico las raíces C, A, F y G','No llamo tercera a la raíz'],
            ['E pertenece como tercera a Cmaj7','Las otras tres notas siguen siendo raíces'],
            ['C es tercera de Am7','F3 y G3 siguen siendo raíces'],
            ['A es tercera de Fmaj7','G3 sigue siendo raíz'],
            ['B es tercera de G7','Relaciono cada objetivo con la raíz escrita'],
        ],
        'simplify': [
            'Toca solo la raíz de cada acorde y di su nombre; conserva el mismo plan armónico.',
            'Compara C4 y E4 sobre Cmaj7 antes de añadir los demás compases.',
            'Practica A3 y C4 sobre Am7; conserva las otras alturas.',
            'Practica F3 y A3 sobre Fmaj7; no cambies la armonía.',
            'Toca una tercera correcta por acorde en una octava cómoda; no rellenes los pulsos.',
        ],
        'extend': 'Elige otra octava cómoda para una tercera real y comprueba la relación raíz-tercera en cada símbolo.',
    },
}

for lesson in new_lessons:
    number = lesson['id'][-3:]
    chord_plan = chord_plans[number]
    for stage_order, melody in enumerate(plans[number], 1):
        stage_id = f'stage-melody-{number}-{stage_order:02d}'
        progression_id = f'prog-melody-{number}-{stage_order:02d}-primary'
        content = stage_content[number]
        existing['stages'].append({
            'id': stage_id,
            'lessonId': lesson['id'],
            'order': stage_order,
            'title': content['titles'][stage_order-1],
            'explanationMd': content['explanations'][stage_order-1] + ' El bajo y la melodía representan parcialmente el plan armónico; no son bloques completos.',
            'task': content['tasks'][stage_order-1],
            'changeFromPrevious': content['changes'][stage_order-1],
            'successCriteria': content['criteria'][stage_order-1],
            'simplifyHint': content['simplify'][stage_order-1],
            'extendHint': content['extend'],
        })
        existing['progressions'].append({
            'id': progression_id,
            'stageId': stage_id,
            'kind': 'primary',
            'order': 1,
            'title': lesson['title'],
            'keyTonic': 'C',
            'keyMode': 'major',
            'style': lesson['styleTags'][0],
            'bpm': 72,
            'timeSignature': {'numerator': 4, 'denominator': 4},
            'totalBars': 4,
            'description': 'Referencia a dos manos con bajo sencillo y melodía monofónica; la armonía se representa parcialmente, no como voicings completos.',
            'loopable': True,
        })
        for order, (symbol, function, root) in enumerate(chord_plan, 1):
            existing['chord-events'].append({
                'id': f'chord-melody-{number}-{stage_order:02d}-primary-{order:03d}',
                'progressionId': progression_id,
                'order': order,
                'symbol': symbol,
                'function': function,
                'startBeat': (order-1)*4,
                'durationBeats': 4,
            })
            existing['note-events'].append({
                'id': f'note-melody-{number}-{stage_order:02d}-primary-{order:04d}',
                'progressionId': progression_id,
                'midi': root,
                'startBeat': (order-1)*4,
                'durationBeats': 4,
                'velocity': 58,
                'role': 'bass',
                'hand': 'left',
            })
        for order, (beat, pitch, duration) in enumerate(melody, 5):
            existing['note-events'].append({
                'id': f'note-melody-{number}-{stage_order:02d}-primary-{order:04d}',
                'progressionId': progression_id,
                'midi': pitch,
                'startBeat': beat,
                'durationBeats': duration,
                'velocity': 76,
                'role': 'melody',
                'hand': 'right',
            })
    existing['lessons'].append(lesson)

for name, rows in existing.items():
    write_json(ROOT / f'{name}.json', rows)

verify_batch_one({
    name: read_json(ROOT / f'{name}.json')
    for name in ('lessons', 'stages', 'progressions', 'chord-events', 'note-events')
})
print('Batch 1 conservado; generadas M004–M006.')
