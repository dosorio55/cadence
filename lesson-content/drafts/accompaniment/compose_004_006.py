import json
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT.parents[1] / 'approved'
lessons = json.loads((DATA / 'lessons.json').read_text(encoding='utf-8'))
selected = {f'lesson-accompaniment-{number:03}' for number in (4, 5, 6)}
lesson_rows = [lesson for lesson in lessons if lesson['id'] in selected]

harmony004 = ['C', 'G', 'Am', 'F']
roots004 = [36, 43, 33, 41]
voicings004 = [
    [[48, 52], [55, 59], [57, 60], [53, 57]],
    [[60, 64], [67, 71], [69, 72], [65, 69]],
    [[60, 64, 67], [67, 71, 74], [69, 72, 76], [65, 69, 72]],
    [[60, 64], [67, 71], [69, 72], [65, 69]],
    [[60, 64, 67], [67, 71], [69, 72, 76], [65, 69]],
]
harmony006 = ['C', 'G', 'Am', 'F'] * 2
roots006 = [36, 43, 33, 41] * 2
voicings006 = [
    [[60, 64, 67], [67, 71, 74], [69, 72, 76], [65, 69, 72]] * 2,
    [[60, 64, 67], [59, 62, 67], [69, 72, 76], [65, 69, 72]] * 2,
    [[60, 64, 67], [59, 62, 67], [60, 64, 69], [60, 65, 69]] * 2,
    [[55, 60, 64], [55, 59, 62], [57, 60, 64], [57, 60, 65]] * 2,
    [[55, 60, 64], [55, 59, 62], [52, 57, 60], [53, 57, 60],
     [52, 55, 60], [55, 59, 62], [57, 60, 64], [57, 60, 65]],
]
melody005 = [[62, 65], [71, 69], [64, 67], [72, 71]]
roots005 = [38, 43, 36, 36]
shells005 = [[53, 60], [53, 59], [52, 59], [52, 59]]

stages = []
progressions = []
chords = []
notes = []


def add_note(progression_id, midi, start, duration, role, hand, velocity=72):
    index = sum(note['progressionId'] == progression_id for note in notes) + 1
    notes.append({
        'id': f'note-accompaniment-{progression_id.split("-")[2]}-{progression_id.split("-")[3]}-{index:04}',
        'progressionId': progression_id,
        'midi': midi,
        'startBeat': start,
        'durationBeats': duration,
        'velocity': velocity,
        'role': role,
        'hand': hand,
    })


def stage_copy(lesson_id, order, title, explanation, task, change, criterion, simplify, extend):
    stages.append({
        'id': f'stage-accompaniment-{lesson_id[-3:]}-{order:02}',
        'lessonId': lesson_id,
        'order': order,
        'title': title,
        'explanationMd': explanation,
        'task': task,
        'changeFromPrevious': change,
        'successCriteria': [criterion, 'Mantengo el bajo, los compases y el pulso indicados.'],
        'simplifyHint': simplify,
        'extendHint': extend,
    })


specs = {
    4: [
        ('Base: dos voces en posición baja', 'A: bajo grave constante y dos voces derechas compactas; no son tríadas.', 'Toca cada díada derecha junto con su raíz izquierda al inicio del compás y sostén ambas cuatro negras.', 'Presentación de bajo grave y díadas en registro próximo.', 'Oigo dos voces derechas por acorde y la raíz correspondiente.'),
        ('Desplazar las díadas una octava', 'Compara A (01) con B: cada altura derecha sube exactamente una octava; el bajo permanece igual.', 'Sube las dos notas de cada díada doce semitonos; no cambies ataques ni duración.', 'Solo cambia el registro derecho: cada nota sube doce semitonos; no se agrega ni retira voz.', 'Cada díada conserva sus dos alturas relativas y está una octava arriba de A.'),
        ('Añadir la quinta', 'Compara A (02) con B: se conservan las dos voces y se añade una quinta del acorde en cada compás.', 'Añade la tercera nota escrita a cada díada, manteniendo las dos voces originales.', 'Se añade únicamente la quinta; armonía, bajo, registro y sostenido de cuatro negras siguen iguales.', 'Toco exactamente tres notas derechas por acorde, incluida la quinta indicada.'),
        ('Retirar la quinta', 'Compara A (03) con B: se retira la quinta y vuelven las mismas dos notas de la etapa 02.', 'Quita solo la quinta y conserva las dos alturas, el ataque y las cuatro negras de duración.', 'Se retira la quinta añadida en 03; quedan las dos voces de 02.', 'Toco dos notas derechas por acorde; ninguna quinta de 03 permanece.'),
        ('Autonomía: elegir dos o tres voces', 'Compara A (04) con B: en C y Am la referencia usa tres voces; en G y F usa dos. Elige esa densidad u otra propia.', 'Toca la referencia y luego decide en qué acordes usar dos o tres voces, sin cambiar las notas del acorde.', 'Frente a 04, se añade la quinta solo en C y Am; G y F siguen a dos voces.', 'Identifico los compases de dos y tres voces y elijo una densidad propia.'),
    ],
    5: [
        ('A: guía monofónica y bajo', 'La guía derecha es reproducible: dos notas sucesivas de una negra en beats 0 y 1 de cada compás; queda silencio de 2 a 4. La raíz izquierda ataca en 0.', 'Toca solo la guía de dos notas por compás y la raíz izquierda puntual en beat 0; no añadas shells.', 'Base de la lección: la frase guía conserva dos notas por compás y el bajo entra en 0.', 'La derecha toca solo las dos notas de guía; la izquierda toca una raíz de duración media negra en 0.'),
        ('Añadir shells en beats 2 y 3', 'A (01) frente a B: en el silencio derecho [2,4) se añaden dos ataques de shell izquierdo, en beats 2 y 3. El bajo sigue en 0.', 'Conserva la guía y toca tercera y séptima juntas en beats 2 y 3, cada bloque durante media negra.', 'Se añaden dos ataques de shell por compás, sin cambiar guía ni bajo.', 'Los dos shells entran después de la guía, en 2 y 3, y duran media negra cada uno.'),
        ('Retirar el ataque de beat 2', 'A (02) tiene shells en 2 y 3; B retira solo el de 2. Guía, bajo y shell de 3 no cambian.', 'Conserva guía y bajo; toca solo el shell de beat 3 durante media negra.', 'Se elimina solamente el shell de beat 2; el de 3 permanece intacto.', 'Hay un único shell en 3 y ninguno en 2; la derecha conserva su pausa [2,4).'),
        ('Desplazar shell de 3 a 2', 'A (03) coloca el único shell en 3; B (04) lo adelanta a 2. Guía y bajo son iguales.', 'Toca el shell de tercera y séptima en beat 2, sin ataque en beat 3; conserva la guía.', 'El único ataque del shell cambia de beat 3 a beat 2 y sigue durando media negra.', 'El shell comienza en beat 2, no en 3, y no se superpone con las dos notas de guía.'),
        ('Autonomía: elegir un hueco', 'La guía y raíz son fijas. Referencia B: un shell por compás en offsets 3, 2, 3, 2; elige un hueco por compás.', 'Compara los dos lugares de shell y decide uno por compás dentro de la pausa derecha de beats 2–4.', 'Frente a 04, los compases 1 y 3 pasan de offset 2 a 3; los compases 2 y 4 conservan offset 2. Se elige el hueco sin añadir ataques.', 'Toco un shell por compás en el offset indicado por mi elección, después de la guía.'),
    ],
    6: [
        ('A: tríadas en posición fundamental', 'Referencia A: bloques derechos C–G–Am–F repetidos, con bajo izquierdo en raíz y notas sostenidas cuatro negras.', 'Toca las ocho tríadas escritas en bloque con el bajo de raíz correspondiente.', 'Base de ocho compases: raíces izquierdas y tríadas derechas en posición fundamental.', 'Cada bloque derecho contiene las tres notas de la tríada indicada.'),
        ('Cambiar solo la inversión de G', 'Compara A (01) y B: solo G cambia a [59,62,67]; conserva G como cima común. No se prescribe avance por paso.', 'Cambia únicamente el segundo y sexto bloque a [59,62,67]; el bajo G2 y los demás acordes no cambian.', 'Invierte solo los bloques derechos de G; su cima pasa de D5 a G4, común al C anterior. Los demás bloques no cambian.', 'En ambos G la derecha toca [59,62,67] y la cima sigue siendo 67.'),
        ('Conducir la cima por pasos y unísonos', 'Compara A (02) y B: las cimas de los cuatro acordes son G–G–A–A, repetidas; el enlace usa paso o unísono.', 'Toca los ocho bloques indicados; mantén la cima común en G y A donde corresponda.', 'Frente a 02, Am y F cambian de inversión para acercar sus cimas; C y G conservan sus bloques.', 'Las cimas siguen G/G/A/A dos veces y cada bloque pertenece a su acorde.'),
        ('Otra ruta de inversiones', 'Compara A (03) y B: la ruta cambia a las cimas E–D–E–F repetidas; todas las notas son del acorde.', 'Toca la ruta alternativa completa, manteniendo raíces en la izquierda.', 'Se cambia la ruta de inversiones de los bloques derechos; raíces, armonía, ataques y duración permanecen.', 'Las cimas son E/D/E/F dos veces y los bloques contienen solo notas de sus acordes.'),
        ('Autonomía: ocho bloques y retorno', 'Referencia B: cimas E–D–C–C–C–D–E–F. El retorno de F a E al repetir el loop es por paso; elige inversiones propias sin notas ajenas.', 'Toca los ocho bloques de referencia y comprueba F→E al repetir; después crea una ruta propia con notas del acorde.', 'Frente a 04, se cambia la inversión de Am, F y C en los compases 3, 4 y 5; los otros cinco bloques quedan iguales.', 'La ruta de referencia conserva las ocho cimas y el loop retorna de F a E por paso.'),
    ],
}

for number in (4, 5, 6):
    lesson_id = f'lesson-accompaniment-{number:03}'
    lesson = next(row for row in lesson_rows if row['id'] == lesson_id)
    for order, (title, explanation, task, change, criterion) in enumerate(specs[number], 1):
        stage_copy(lesson_id, order, title, explanation, task, change, criterion,
                   'Reduce la velocidad; conserva exactamente las notas, ataques y duraciones de esta etapa.',
                   'Repite el ciclo completo conservando el recurso de esta etapa y las notas de cada acorde.')
        stage_id = f'stage-accompaniment-{number:03}-{order:02}'
        progression_id = f'prog-accompaniment-{number:03}-{order:02}-primary'
        progression_harmony = harmony004 if number == 4 else (['Dm7', 'G7', 'Cmaj7', 'Cmaj7'] if number == 5 else harmony006)
        bars = 8 if number == 6 else 4
        progressions.append({
            'id': progression_id, 'stageId': stage_id, 'kind': 'primary', 'order': 1,
            'title': title, 'keyTonic': 'C', 'keyMode': 'major',
            'style': 'jazz' if number == 5 else 'pop', 'bpm': 72 if number == 5 else 80,
            'timeSignature': {'numerator': 4, 'denominator': 4}, 'totalBars': bars,
            'description': 'Progresión y realización pianística detalladas para esta etapa; los eventos especifican todas las alturas y duraciones.',
            'loopable': True,
        })
        for bar, symbol in enumerate(progression_harmony):
            function = (['I', 'V', 'vi', 'IV'][bar % 4] if number != 5
                       else ['ii7', 'V7', 'Imaj7', 'Imaj7'][bar])
            chords.append({
                'id': f'chord-accompaniment-{number:03}-{order:02}-{bar + 1:03}',
                'progressionId': progression_id, 'order': bar + 1, 'symbol': symbol,
                'function': function, 'startBeat': bar * 4, 'durationBeats': 4,
            })
        if number == 4:
            for bar, root in enumerate(roots004):
                add_note(progression_id, root, bar * 4, 4, 'bass', 'left')
                for midi in voicings004[order - 1][bar]:
                    add_note(progression_id, midi, bar * 4, 4, 'harmony', 'right')
        elif number == 5:
            for bar, root in enumerate(roots005):
                add_note(progression_id, root, bar * 4, 0.5, 'bass', 'left')
                for beat, midi in enumerate(melody005[bar]):
                    add_note(progression_id, midi, bar * 4 + beat, 1, 'melody', 'right')
                shell_offsets = {
                    1: [],
                    2: [2, 3],
                    3: [3],
                    4: [2],
                    5: [[3, 2, 3, 2][bar]],
                }[order]
                for offset in shell_offsets:
                    for midi in shells005[bar]:
                        add_note(progression_id, midi, bar * 4 + offset, 0.5, 'harmony', 'left')
        else:
            for bar, root in enumerate(roots006):
                add_note(progression_id, root, bar * 4, 4, 'bass', 'left')
                for midi in voicings006[order - 1][bar]:
                    add_note(progression_id, midi, bar * 4, 4, 'harmony', 'right')

for name, rows in (
    ('lessons', lesson_rows), ('stages', stages), ('progressions', progressions),
    ('chord-events', chords), ('note-events', notes),
):
    path = ROOT / f'{name}.json'
    existing = json.loads(path.read_text(encoding='utf-8')) if path.exists() else []
    replacement_ids = {row['id'] for row in rows}
    preserved = [row for row in existing if row['id'] not in replacement_ids]
    path.write_text(json.dumps(preserved + rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
