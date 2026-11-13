import json
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT.parents[1] / 'approved'

lessons = json.loads((DATA / 'lessons.json').read_text())
previous_note_events = json.loads((ROOT / 'note-events.json').read_text()) if (ROOT / 'note-events.json').exists() else []
previous_melody_notes = {
    (note['progressionId'], note['midi'], note['startBeat'], note['durationBeats'], note['velocity'], note['role'], note['hand']): note['id']
    for note in previous_note_events
}


def note_id(number, progression_id, pitch, start, duration, velocity, role, hand, fallback):
    if number == '002':
        key = (progression_id, pitch, start, duration, velocity, role, hand)
        return previous_melody_notes.get(key, fallback)

    return fallback


lesson_ids = {'lesson-melody-001', 'lesson-melody-002', 'lesson-melody-003'}
lessons = [lesson for lesson in lessons if lesson['id'] in lesson_ids]

plans = {
    '001': [
        [(0,67,1),(4,67,1),(8,67,1),(12,67,1)],
        [(0,64,1),(4,60,1),(8,65,1),(12,67,1)],
        [(0,64,1),(4,60,1),(8,65,1),(12,71,1)],
        [(0,72,1),(4,64,1),(8,69,1),(12,74,1)],
    ],
    '002': [
        [(0,64,.5),(1,67,.5),(2,72,1),(4,64,.5),(5,67,.5),(6,72,1)],
        [(0,64,.5),(1,67,.5),(2,72,1),(4,64,.5),(5,67,.5),(6,72,1),(8,64,.5),(9,67,.5),(10,72,1),(12,64,.5),(13,67,.5),(14,72,1)],
        [(0,64,.5),(1,67,.5),(2,72,1),(4,64,.5),(5,67,.5),(6,72,1),(8,64,.5),(9,67,.5),(10,69,1),(12,64,.5),(13,67,.5),(14,69,1)],
        [(0,64,.5),(1,67,.5),(2,72,1),(4,64,.5),(5,67,.5),(6,72,1),(8,64,.5),(9,67,.5),(10,69,1),(12,64,.5),(13,67,.5),(14,69,1),(15.5,67,.5)],
    ],
    '003': [
        [(0,64,3.5),(4,60,3.5),(8,57,1),(12,59,1)],
        [(0,64,3.5),(3.5,62,.5),(4,60,3.5),(8,57,1),(12,59,1)],
        [(0,64,3.5),(3.5,62,.5),(4,60,3.5),(7.5,59,.5),(8,57,1),(12,59,1)],
        [(0,64,3.5),(4,60,3.5),(7.5,59,.5),(8,57,1),(12,59,1)],
    ],
}

stage_titles = {
    '001': ['Base: nota indiferente','B: destinos acordales','Cambia un destino','Elección autónoma'],
    '002': ['Presenta la célula','Repite en compases 3 y 4','Adapta una altura','Respuesta de referencia'],
    '003': ['Apoyos sin conexión','Paso débil E–D–C','Añade C–B–A','Elige una frontera'],
}
changes = {
    '001': [
        'Presentación A: G4 (67) en los cuatro inicios, sobre el mismo plan C–Am–F–G.',
        'B frente a A: sustituye solo las cuatro alturas derechas por E4, C4, F4 y G4 en 0, 4, 8 y 12; bajo y armonía no cambian.',
        'Frente a B, cambia solo el último objetivo G4 (67) por B4 (71), otra nota del acorde G; los tres primeros objetivos quedan iguales.',
        'Referencia autónoma: C5, E4, A4 y D5 son una elección posible de notas del acorde; elige tus propios objetivos, no una solución única.',
    ],
    '002': [
        'Presentación: motivo de tres notas, dos breves y una larga, seguido por aire.',
        'Frente a 01, repite el mismo motivo en los compases 3 y 4; conserva ritmo, alturas y pausa sobre Am7.',
        'Frente a 02, cambia solo la última altura de cada repetición en compases 3 y 4: C5 pasa a A4, acorde con Am7.',
        'Referencia autónoma: añade una respuesta breve conservando las tres notas del motivo y dejando su pausa; hay otras respuestas válidas.',
    ],
    '003': [
        'Presentación: conserva los cuatro apoyos; la derecha deja espacio entre ellos.',
        'Frente a 01, añade solo D4 (62) en 3.5: E4–D4–C4 es paso diatónico débil con entrada y salida conjuntas.',
        'Conserva E4–D4–C4 y añade solo B3 (59) en 7.5: C4–B3–A3 resuelve por grado conjunto.',
        'Vuelve a la base y conserva solo el paso de la frontera 8 (B3@7.5); puedes elegir otra conexión diatónica débil, no es una solución única.',
    ],
}
explanations = {
    '001': [
        'A: oye G4 repetido aunque cambien bajo y acorde. La línea no intenta señalar cada cambio.',
        'B: compara con A. Cada ataque ahora coincide con una nota del acorde: E de C, C de Am, F de F y G de G.',
        'A/B: solo cambia el objetivo final; B4 también pertenece a G y ofrece otro color acordal que G4.',
        'La referencia usa otras notas del acorde en cada llegada. Canta y escoge tus objetivos: el ejemplo no es respuesta única.',
    ],
    '002': [
        'Canta E4–G4–C5 y siente la pausa antes de la repetición.',
        'A/B: el motivo que aparecía en compases 1 y 2 ahora también suena en 3 y 4; no cambia su célula.',
        'A/B: compara C5 y A4 al final de las dos últimas células; ritmo y primeras dos notas siguen iguales.',
        'Usa la célula como referencia para responder; conserva tres notas y una pausa, con alturas propias.',
    ],
    '003': [
        'Escucha E4, C4, A3 y B3 como apoyos; el bajo sostiene las raíces y deja aire a la línea.',
        'D4 entra en 3.5, parte débil, entre E4 y C4; comprueba ambos pasos conjuntos y la llegada a C4 en 4.',
        'El nuevo B3 entra en 7.5 entre C4 y A3; escucha la resolución conjunta sobre el siguiente apoyo.',
        'Se retira el paso E–D–C y se conserva C–B–A en la frontera 8; decide si esa conexión sirve a tu frase.',
    ],
}
tasks = {
    '001': [
        'Toca cada nota derecha al inicio del compás y compara su estabilidad con los cambios del bajo.',
        'Alterna A y B; comprueba que solo cambia la selección de alturas de la melodía.',
        'Compara los finales G4 y B4 sobre G; canta ambos objetivos antes de tocarlos.',
        'Escoge una nota del acorde por compás y explica por qué la elegiste.',
    ],
    '002': [
        'Canta la célula, toca sus tres notas y respeta la pausa.',
        'Compara las repeticiones nuevas de compases 3 y 4 con las de 1 y 2.',
        'Repite el motivo y escucha cómo cambia solo su última altura en Am7.',
        'Inventa una respuesta breve que mantenga el motivo reconocible y su espacio.',
    ],
    '003': [
        'Toca los apoyos sin rellenar los huecos; canta E–C y C–A.',
        'Aísla E–D–C y verifica que D entra débil y resuelve por grado conjunto.',
        'Practica E–D–C y C–B–A por separado y luego sobre el bajo.',
        'Elige una frontera para un paso diatónico débil y comprueba entrada y resolución.',
    ],
}
success = {
    '001': [
        ['Mantengo G4 en los cuatro inicios','Oigo que G4 no señala por igual los cuatro cambios'],
        ['E, C, F y G pertenecen a los acordes de llegada','Puedo comparar A y B sin cambiar el pulso'],
        ['Solo cambia el último objetivo','Reconozco ambos finales como notas de G'],
        ['Puedo cantar mis objetivos antes de tocarlos','Sé que la referencia no es la única respuesta'],
    ],
    '002': [
        ['Toco tres notas con ritmo reconocible','Dejo la pausa después de la célula'],
        ['Repito la célula en los compases 3 y 4','Conservo alturas, contorno y pausa'],
        ['Cambio una sola altura en cada respuesta','El motivo sigue reconocible'],
        ['Mi respuesta conserva la célula de tres notas','Dejo espacio y no impongo una solución única'],
    ],
    '003': [
        ['Distingo los cuatro apoyos','Puedo cantar las conexiones sin adornos'],
        ['D entra en parte débil','E–D y D–C avanzan por grado conjunto'],
        ['B entra en parte débil','C–B y B–A resuelven por grado conjunto'],
        ['Elijo una sola frontera','Puedo cantar entrada, paso y destino'],
    ],
}
simplify = {
    '001': [
        'Toca G4 una vez al inicio de cada compás; conserva bajo y quinta izquierdos.',
        'Practica primero los cuatro objetivos acordales sin bajo; luego añade la izquierda.',
        'Compara solo G4 y B4 sobre el último compás antes de tocar la frase completa.',
        'Elige una nota del acorde por compás; reduce a dos llegadas si hace falta.',
    ],
    '002': [
        'Toca las tres notas E–G–C más despacio y conserva la pausa.',
        'Repite la célula de tres notas solo en el compás 3, manteniendo la pausa.',
        'Cambia únicamente la última de las tres notas; conserva ritmo y pausa.',
        'Responde una sola vez con tres notas y una pausa.',
    ],
    '003': [
        'Toca solo los apoyos E4, C4, A3 y B3; conserva sus huecos.',
        'Practica E–D–C sin bajo y cuenta D en 4&.',
        'Practica primero E–D–C y después C–B–A, sin añadir más notas.',
        'Conserva solo el paso C–B–A en 4& del compás 2.',
    ],
}
extend = {
    '001': 'Escoge una nota acordal distinta para una llegada y compara su color sin cambiar el ritmo.',
    '002': 'Varía una altura cada vez y conserva el ritmo, las tres notas y la pausa.',
    '003': 'Elige otra frontera de acorde y compón un paso diatónico de entrada y salida conjuntas.',
}

chords = [('C','I',0),('Am','vi',4),('F','IV',8),('G','V',12)]
roots = [48,45,41,43]
fifths = [55,52,48,50]
stages, progressions, chord_events, note_events = [], [], [], []

for lesson in lessons:
    number = lesson['id'][-3:]
    for index, melody in enumerate(plans[number], 1):
        stage_id = f'stage-melody-{number}-{index:02d}'
        progression_id = f'prog-melody-{number}-{index:02d}-primary'
        stages.append({
            'id': stage_id,
            'lessonId': lesson['id'],
            'order': index,
            'title': stage_titles[number][index-1],
            'explanationMd': explanations[number][index-1] + ' El bajo y la melodía representan parcialmente el plan armónico; no son bloques de acordes completos.',
            'task': tasks[number][index-1],
            'changeFromPrevious': changes[number][index-1],
            'successCriteria': success[number][index-1],
            'simplifyHint': simplify[number][index-1],
            'extendHint': extend[number],
        })
        progressions.append({
            'id': progression_id,
            'stageId': stage_id,
            'kind': 'primary',
            'order': 1,
            'title': {'001':'Objetivos sobre I–vi–IV–V','002':'Motivo de tres notas','003':'Apoyos con paso débil'}[number],
            'keyTonic': 'C',
            'keyMode': 'major',
            'style': lesson['styleTags'][0],
            'bpm': 72,
            'timeSignature': {'numerator':4,'denominator':4},
            'totalBars': 4,
            'description': 'Referencia a dos manos: bajo sencillo y melodía monofónica; el plan armónico se representa parcialmente, no como voicings completos.',
            'loopable': True,
        })
        progression_chords = chords
        progression_roots = roots
        progression_fifths = fifths
        if number == '002':
            progression_chords = [('C','I',0),('C','I',4),('Am7','vi7',8),('Am7','vi7',12)]
            progression_roots = [48,48,45,45]
            progression_fifths = [55,55,52,52]
        for order, (symbol, function, start) in enumerate(progression_chords, 1):
            chord_events.append({
                'id':f'chord-melody-{number}-{index:02d}-primary-{order:03d}',
                'progressionId':progression_id,
                'order':order,
                'symbol':symbol,
                'function':function,
                'startBeat':start,
                'durationBeats':4,
            })
        note_order = 1
        for bar, root in enumerate(progression_roots):
            bass_notes = [(root,)]
            if number == '001':
                bass_notes = [(root, progression_fifths[bar])]
            for pitch in bass_notes[0]:
                note_events.append({
                    'id':note_id(number, progression_id, pitch, bar*4, 4, 58, 'bass', 'left', f'note-melody-{number}-{index:02d}-primary-{note_order:04d}'),
                    'progressionId':progression_id,
                    'midi':pitch,
                    'startBeat':bar*4,
                    'durationBeats':4,
                    'velocity':58,
                    'role':'bass',
                    'hand':'left',
                })
                note_order += 1
        for beat, pitch, duration in melody:
            note_events.append({
                'id':note_id(number, progression_id, pitch, beat, duration, 76, 'melody', 'right', f'note-melody-{number}-{index:02d}-primary-{note_order:04d}'),
                'progressionId':progression_id,
                'midi':pitch,
                'startBeat':beat,
                'durationBeats':duration,
                'velocity':76,
                'role':'melody',
                'hand':'right',
            })
            note_order += 1

for name, rows in (
    ('lessons',lessons),
    ('stages',stages),
    ('progressions',progressions),
    ('chord-events',chord_events),
    ('note-events',note_events),
):
    (ROOT / f'{name}.json').write_text(
        json.dumps(rows,ensure_ascii=False,indent=2)+'\n',
        encoding='utf-8',
    )
