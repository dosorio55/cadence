import json
from pathlib import Path

out = Path(__file__).parent
lesson = next(x for x in json.load(open(out.parents[2] / 'approved/lessons.json')) if x['id'] == 'lesson-rhythm-015')
json.dump([lesson], open(out / 'lessons.json', 'w'), ensure_ascii=False, indent=2)

chords = ['Dm7', 'G7', 'Cmaj7', 'Cmaj7', 'Am7', 'Dm7', 'G7', 'Cmaj7']
functions = ['ii7', 'V7', 'Imaj7', 'Imaj7', 'vi7', 'ii7', 'V7', 'Imaj7']
roots = [50, 43, 48, 48, 45, 50, 43, 48]
pairs = [(65, 69), (71, 65), (64, 67), (64, 71), (72, 67), (65, 69), (71, 65), (64, 72)]
progressions, stages, chord_events, notes = [], [], [], []
for stage in range(1, 6):
    pid = f'prog-rhythm-015-{stage:02}-primary'
    sid = f'stage-rhythm-015-{stage:02}'
    progressions.append(dict(id=pid, stageId=sid, kind='primary', order=1,
        title=['Frase pareja de referencia', 'Desplazar la respuesta', 'Respirar en Am', 'Llegada larga', 'Autonomía: retrasar G7'][stage-1],
        keyTonic='C', keyMode='major', style='jazz', bpm=80,
        timeSignature=dict(numerator=4, denominator=4), totalBars=8,
        description='32 negras constantes, Dm7–G7–Cmaj7–Cmaj7–Am7–Dm7–G7–Cmaj7. La izquierda es solo línea de raíces en blancas, no voicings completos. La derecha es línea monofónica; ataques, duraciones y silencios explícitos. Las parejas regulares usan proporción 2:1 (2/3:1/3); no se impone swing a cada nota.', loopable=True))
    explanations = [
      'Dos frases iguales; cada pareja comienza en offset 0 y 2/3, con duraciones 2/3 y 1/3; el resto queda libre.',
      'La primera frase permanece idéntica. En compases 5–8 desplaza la pareja completa una negra: offsets 1 y 1+2/3.',
      'Como 02, pero omite solo G4 (67) de Am7 en beat 21+2/3. C5 en 21 dura 2/3; luego hay aire hasta la pareja del compás 6.',
      'Conserva 03 y transforma solo el final: E4 entra en beat 29 y dura 2 beats hasta 31; elimina C5 en 29+2/3. Esta blanca larga no lleva swing forzado.',
      'Como 04, salvo la pareja G7 del compás 7: pasa de 25/25+2/3 a 26/26+2/3. F4 en 26 conduce por semitono real a E4 en 29; el acorde Cmaj7 llega en 28, antes de la llegada melódica. No anticipes E4.'
    ]
    changes = [
      'Referencia: ocho parejas con duraciones explícitas 2/3 y 1/3, más silencios hasta la siguiente entrada.',
      'Solo segunda frase +1 beat; mismos pitches y duraciones. Bajo y primera frase no cambian.',
      'Un único silencio añadido: se retira la segunda nota de Am7; se conserva su primera llegada y todo lo demás.',
      'La pareja final se sustituye por E4 largo de 2 beats; conserva omisión en Am7 y los demás eventos.',
      'Autonomía: desplaza la pareja de G7 una negra más tarde; conserva omisión de Am7, cierre largo y bajo.'
    ]
    title = ['Frase de referencia', 'Mover la segunda frase', 'Un silencio dentro de Am7', 'Cerrar con una nota larga', 'Autonomía: respirar antes de G7'][stage-1]
    stages.append(dict(id=sid, lessonId='lesson-rhythm-015', order=stage, title=title,
        explanationMd=explanations[stage-1], task='Toca los ocho compases a 80 BPM contando 1–2–3–4; conserva los 32 beats aunque la derecha calle.',
        changeFromPrevious=changes[stage-1], successCriteria=['La izquierda conserva sus 16 ataques de blancas y el ciclo dura 32 beats.', 'Identifico cada entrada derecha, duración y silencio sin rellenarlo.'],
        simplifyHint='Practica primero cada mano por separado y cuenta las negras en voz alta; las pausas derechas no detienen el pulso.',
        extendHint='Toca de memoria a 80 BPM y compara la respiración elegida con la referencia sin aumentar la cantidad de notas.'))
    for bar, (symbol, function, root, pair) in enumerate(zip(chords, functions, roots, pairs)):
        start = bar * 4
        chord_events.append(dict(id=f'cr015-{stage}-{bar+1}', progressionId=pid, order=bar+1, symbol=symbol, function=function, startBeat=start, durationBeats=4))
        for i, offset in enumerate((0, 2)):
            notes.append(dict(id=f'nr015-{stage}-{bar+1}-lh-{i+1}', progressionId=pid, midi=root, startBeat=start+offset, durationBeats=2, velocity=60, role='bass', hand='left'))
        offsets = [0, 2/3]
        if stage >= 2 and bar >= 4:
            offsets = [1, 5/3]
        if stage == 5 and bar == 6:
            offsets = [2, 8/3]
        for i, (pitch, offset, duration) in enumerate(((pair[0], offsets[0], 2/3), (pair[1], offsets[1], 1/3))):
            if stage >= 3 and bar == 4 and i == 1:
                continue
            if stage >= 4 and bar == 7:
                if i == 0:
                    notes.append(dict(id=f'nr015-{stage}-{bar+1}-rh-1', progressionId=pid, midi=64, startBeat=29, durationBeats=2, velocity=72, role='melody', hand='right'))
                continue
            notes.append(dict(id=f'nr015-{stage}-{bar+1}-rh-{i+1}', progressionId=pid, midi=pitch, startBeat=start+offset, durationBeats=duration, velocity=72, role='melody', hand='right'))
for name, data in [('progressions', progressions), ('stages', stages), ('chord-events', chord_events), ('note-events', notes)]:
    json.dump(data, open(out / f'{name}.json', 'w'), ensure_ascii=False, indent=2)
