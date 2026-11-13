#!/usr/bin/env python3
"""Añade el lote rhythm 005–007 con planes explícitos y conserva lotes aprobados."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / 'drafts' / 'rhythm'
DATA = ROOT / 'approved'


def read(name):
    return json.loads((WORK / f'{name}.json').read_text(encoding='utf-8'))


def write(name, rows):
    (WORK / f'{name}.json').write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8'
    )


def add_note(rows, lesson_order, stage_order, progression_id, midi, start, duration,
             role, hand, velocity):
    count = sum(row['progressionId'] == progression_id for row in rows) + 1
    rows.append({
        'id': f'note-rhythm-{lesson_order:03d}-{stage_order:02d}-primary-{count:04d}',
        'progressionId': progression_id,
        'midi': midi,
        'startBeat': start,
        'durationBeats': duration,
        'velocity': velocity,
        'role': role,
        'hand': hand,
    })


design_lessons = {row['id']: row for row in json.loads((DATA / 'lessons.json').read_text(encoding='utf-8'))}
new_lessons = [design_lessons[f'lesson-rhythm-{order:03d}'] for order in (5, 6, 7)]

# Each stage plan states the audible comparison and the exact transformation.
stage_plans = {
    5: [
        ('Corcheas rectas',
         'A = esta referencia: sobre ii–V–I–I, la derecha repite cada nota dos veces en corcheas rectas (offsets locales 0 y 0.5 por negra). La izquierda toca raíces en blancas. Cuenta la negra sin alterar el pulso.',
         'Base: frase de ataques parejos en subdivisión binaria, bajo en blancas y cuatro compases ii–V–I–I.',
         'Cuento la negra estable y distingo dos ataques iguales dentro de cada pulso.'),
        ('Referencia ternaria',
         'Compara A (etapa 01, offsets 0/0.5) con B: conserva cada pulso, nota y bajo, pero coloca el segundo ataque a 2/3 de negra. La pareja dura 2/3 + 1/3; es una referencia de swing, no una proporción obligatoria para todo tempo o frase.',
         'En cada negra, el segundo ataque pasa de offset 0.5 a 2/3; las notas y el bajo en blancas se mantienen.',
         'Mantengo el pulso y puedo comparar recto frente a largo-corto sin acelerar.'),
        ('Swing con un espacio',
         'Compara A (etapa 02, ternario continuo) con B: conserva el swing y deja en silencio el ataque corto del último pulso del compás 4 (beat global 15 + 2/3). No rellenes ese hueco.',
         'Se elimina un ataque corto en beat 15 + 2/3; los otros ataques ternarios, la armonía y las blancas del bajo siguen iguales.',
         'Sostengo la subdivisión ternaria imaginada durante el silencio final y cierro en el compás previsto.'),
        ('Elegir una pausa',
         'A referencia = etapa 02 continua. B de referencia omite la nota larga del beat global 5 del compás 2 y conserva su ataque corto en 5 + 2/3. Elige otro lugar para respirar; la proporción ternaria es una posibilidad, no una regla universal.',
         'Se conserva la referencia ternaria de etapa 02 y se deja un hueco propio: en este ejemplo se omite el ataque largo de beat 5; la izquierda sigue en blancas.',
         'Puedo elegir una pausa sin perder la negra, la colocación ternaria ni la llegada final.'),
    ],
    6: [
        ('Vuelta completa de ocho compases',
         'A = referencia completa I–V–vi–IV repetida dos veces. La izquierda marca negras y la derecha toca un bloque corto en los tiempos musicales uno y tres de cada compás. Cuenta ocho compases sin cambiar el patrón.',
         'Presentación de la vuelta completa: bajo en cada negra y acordes derechos en offsets locales 0 y 2 durante ocho compases.',
         'Mantengo ocho compases y puedo contar el pulso durante todos los ataques de ambas manos.'),
        ('Callar la derecha un compás',
         'Compara A (etapa 01) con B: conserva armonía y bajo, pero retira todos los bloques derechos del compás 4 (beats globales 12–16). El bajo sigue marcando negras; reentra la derecha en el compás 5, beat 16.',
         'Se suprimen solo los ataques derechos del compás 4; bajo, tempo, armonía y las demás entradas permanecen iguales.',
         'La izquierda mantiene el ciclo durante el compás sin derecha y ambas manos retoman su patrón en el compás 5.'),
        ('Retirar parte del bajo y volver juntos',
         'Compara con etapa 02: conserva el silencio derecho del compás 4 y además omite el bajo en los tiempos musicales dos y tres del compás 6 (beats globales 21 y 22). Tras el último bajo del compás, ambas manos reentran juntas en el compás 7, beat 24.',
         'Se añaden dos silencios de bajo en el compás 6, beats globales 21/22; la derecha sigue en silencio en el compás 4. Reentrada conjunta en beat 24.',
         'Cuento los dos ataques de bajo ausentes y reentro con ambas manos juntas en beat 24, sin acortar el loop.'),
        ('Decidir dónde dejar aire',
         'A = referencia completa de etapa 01; B = esta referencia, que traslada el silencio derecho del compás 4 al compás 2 y conserva los dos huecos de bajo del compás 6. Elige tu propio compás de aire para la derecha y uno o dos ataques de bajo que retirar; deja una reentrada común clara.',
         'Autonomía: se mueve el compás de silencio derecho de 4 a 2; se mantienen los dos ataques de bajo ausentes en compás 6. La referencia reentra en compás 3 y en compás 7 tras cada hueco.',
         'Puedo elegir silencios para ambas manos, conservar los ocho compases e identificar una reentrada conjunta después de cada pausa.'),
    ],
    7: [
        ('Vamp con cuatro pulsos',
         'A = C7 sostenido durante cuatro compases. La izquierda toca C en tiempos musicales uno y tres; la derecha hace cuatro stabs breves, uno por negra. Cuenta los huecos entre ataques y no llenes cada subdivisión.',
         'Base de un solo acorde C7: bajo espaciado y cuatro bloques derechos breves por compás.',
         'Mantengo el vamp C7 y puedo contar el espacio entre los cuatro ataques derechos.'),
        ('Agrupar semicorcheas con huecos',
         'Compara A (etapa 01) con B: conserva cuatro stabs derechos por compás, pero agrúpalos en dos parejas de semicorcheas, offsets locales 0/0.25 y 2/2.25. Los huecos restantes son parte de la célula; no se agregan ataques.',
         'Mismo número de ataques; dos pares de stabs pasan a una célula de semicorcheas en beats locales 0 y 2, dejando huecos entre pares.',
         'Toco la célula de cuatro ataques sin añadir notas y mantengo la izquierda en sus dos negras espaciadas.'),
        ('Desplazar una pareja',
         'Compara A (etapa 02) con B: conserva cuatro ataques y desplaza la pareja del tercer tiempo un cuarto de negra: de offsets 2/2.25 a 2.25/2.5. La primera pareja y el bajo no cambian.',
         'Solo la segunda pareja se retrasa 0.25 beat; alturas, cantidad de ataques, C7 y bajo permanecen iguales.',
         'Puedo oír el desplazamiento de una semicorchea sin comprimir el pulso ni aumentar la densidad.'),
        ('Elegir qué pareja mover',
         'A referencia = etapa 02. B de referencia conserva la pareja desplazada de etapa 03 y mueve también la primera pareja de 0/0.25 a 0.25/0.5. Elige una sola pareja o ataque que quieras desplazar; mantén cuatro ataques por compás y los huecos.',
         'Autonomía: el ejemplo conserva el movimiento de la pareja del tercer tiempo y desplaza además la primera pareja 0.25 beat; se mantiene el total de cuatro ataques.',
         'Elijo qué ataque desplazar una semicorchea y conservo el vamp, los huecos y la misma densidad.'),
    ],
}

# Chord map and playable note material for the three lesson plans.
progression_chords = {
    5: [
        ('Dm7', 'ii7', 0, 4, 38, 69),
        ('G7', 'V7', 4, 4, 43, 65),
        ('Cmaj7', 'Imaj7', 8, 4, 48, 64),
        ('Cmaj7', 'Imaj7', 12, 4, 48, 67),
    ],
    6: [
        ('C', 'I', 0, 4, 48, [60, 64, 67]),
        ('G', 'V', 4, 4, 43, [59, 62, 67]),
        ('Am', 'vi', 8, 4, 45, [57, 60, 64]),
        ('F', 'IV', 12, 4, 41, [57, 60, 65]),
        ('C', 'I', 16, 4, 48, [60, 64, 67]),
        ('G', 'V', 20, 4, 43, [59, 62, 67]),
        ('Am', 'vi', 24, 4, 45, [57, 60, 64]),
        ('F', 'IV', 28, 4, 41, [57, 60, 65]),
    ],
    7: [('C7', 'I7', 0, 16, 48, [60, 64, 67, 70])],
}

new_stages = []
new_progressions = []
new_chords = []
new_notes = []
for lesson_order in (5, 6, 7):
    lesson_id = f'lesson-rhythm-{lesson_order:03d}'
    lesson = design_lessons[lesson_id]
    bars = 8 if lesson_order == 6 else 4
    bpm = 100 if lesson_order == 5 else (80 if lesson_order == 6 else 90)
    style = 'jazz' if lesson_order == 5 else ('pop' if lesson_order == 6 else 'funk')

    for stage_order, (title, explanation, change, criterion) in enumerate(stage_plans[lesson_order], 1):
        stage_id = f'stage-rhythm-{lesson_order:03d}-{stage_order:02d}'
        progression_id = f'prog-rhythm-{lesson_order:03d}-{stage_order:02d}-primary'
        new_stages.append({
            'id': stage_id, 'lessonId': lesson_id, 'order': stage_order,
            'title': title, 'explanationMd': explanation,
            'task': f'Toca {bars} compases a {bpm} BPM con el material de esta etapa; cuenta los pulsos y respeta los silencios indicados.',
            'changeFromPrevious': change, 'successCriteria': [criterion],
            'simplifyHint': 'Baja el tempo y practica primero la mano izquierda, luego la derecha.',
            'extendHint': 'Repite el ciclo manteniendo el mismo pulso y variando solo el lugar del silencio o desplazamiento.',
        })
        new_progressions.append({
            'id': progression_id, 'stageId': stage_id, 'kind': 'primary', 'order': 1,
            'title': title, 'keyTonic': 'C', 'keyMode': 'major', 'style': style,
            'bpm': bpm, 'timeSignature': {'numerator': 4, 'denominator': 4},
            'totalBars': bars,
            'description': f'{lesson["title"]}: referencia ejecutable específica de la etapa {stage_order}, no solución única.',
            'loopable': True,
        })
        for event_order, chord in enumerate(progression_chords[lesson_order], 1):
            symbol, function, start, duration = chord[:4]
            new_chords.append({
                'id': f'chord-rhythm-{lesson_order:03d}-{stage_order:02d}-primary-{event_order:03d}',
                'progressionId': progression_id, 'order': event_order,
                'symbol': symbol, 'function': function,
                'startBeat': start, 'durationBeats': duration,
            })

        for bar in range(bars):
            bar_start = bar * 4
            chord_index = bar if lesson_order == 6 else (bar // 2 if lesson_order == 5 else 0)
            chord = progression_chords[lesson_order][chord_index]
            bass = chord[4]

            if lesson_order == 5:
                # Two attacks per beat: straight eighths or an explicit 2/3 + 1/3 reference.
                melody_pitch = chord[5]
                for beat in range(4):
                    global_beat = bar_start + beat
                    if stage_order == 1:
                        positions = [(0, 0.5), (0.5, 0.5)]
                    else:
                        positions = [(0, 2 / 3), (2 / 3, 1 / 3)]
                    for attack_index, (offset, duration) in enumerate(positions):
                        if stage_order == 3 and bar == 3 and beat == 3 and attack_index == 1:
                            continue
                        if stage_order == 4 and bar == 1 and beat == 1 and attack_index == 0:
                            continue
                        add_note(new_notes, lesson_order, stage_order, progression_id,
                                 melody_pitch, global_beat + offset, duration,
                                 'melody', 'right', 62)
                for beat in (0, 2):
                    add_note(new_notes, lesson_order, stage_order, progression_id,
                             bass, bar_start + beat, 2, 'bass', 'left', 70)

            elif lesson_order == 6:
                for beat in range(4):
                    if stage_order >= 3 and bar == 5 and beat in (1, 2):
                        continue
                    add_note(new_notes, lesson_order, stage_order, progression_id,
                             bass, bar_start + beat, 0.5, 'bass', 'left', 70)
                right_silent_bar = 3 if stage_order in (2, 3) else (1 if stage_order == 4 else None)
                for beat in (0, 2):
                    if bar == right_silent_bar:
                        continue
                    for pitch in chord[5]:
                        add_note(new_notes, lesson_order, stage_order, progression_id,
                                 pitch, bar_start + beat, 0.5, 'harmony', 'right', 62)

            else:
                for beat in (0, 2):
                    add_note(new_notes, lesson_order, stage_order, progression_id,
                             bass, bar_start + beat, 0.5, 'bass', 'left', 70)
                if stage_order == 1:
                    offsets = [0, 1, 2, 3]
                elif stage_order == 2:
                    offsets = [0, 0.25, 2, 2.25]
                elif stage_order == 3:
                    offsets = [0, 0.25, 2.25, 2.5]
                else:
                    offsets = [0.25, 0.5, 2.25, 2.5]
                for offset in offsets:
                    for pitch in chord[5]:
                        add_note(new_notes, lesson_order, stage_order, progression_id,
                                 pitch, bar_start + offset, 0.25, 'harmony', 'right', 60)

# Verify the existing lesson data is still exactly the approved subset before appending.
existing_lessons = read('lessons')
expected_existing = [design_lessons[f'lesson-rhythm-{order:03d}'] for order in (1, 2, 3, 4)]
assert [row for row in existing_lessons if row['id'] in {x['id'] for x in expected_existing}] == expected_existing

for name, additions in (
    ('stages', new_stages), ('progressions', new_progressions),
    ('chord-events', new_chords), ('note-events', new_notes),
):
    existing = read(name)
    original_ids = {row['id'] for row in existing}
    assert not original_ids.intersection(row['id'] for row in additions), f'{name}: ID collision'
    write(name, existing + additions)

write('lessons', existing_lessons + new_lessons)
