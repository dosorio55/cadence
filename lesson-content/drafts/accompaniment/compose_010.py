import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
out = root / 'drafts/accompaniment/pending-010'
out.mkdir(parents=True, exist_ok=True)
for name in ('categories', 'skills'):
    (out / f'{name}.json').write_text((root / 'approved' / f'{name}.json').read_text())
lesson = next(x for x in json.loads((root / 'approved/lessons.json').read_text()) if x['id'] == 'lesson-accompaniment-010')
(out / 'lessons.json').write_text(json.dumps([lesson], ensure_ascii=False, indent=2) + '\n')

chords = [
    ('Cmaj7', 'Imaj7', 36, 43, [60, 64, 67, 71]),
    ('Am7', 'vi7', 33, 40, [57, 60, 64, 67]),
    ('Dm7', 'ii7', 38, 45, [53, 57, 60, 62]),
    ('G7', 'V7', 31, 38, [59, 62, 65, 67]),
]
rh = {
    1: [[60, 64, 67, 71], [57, 60, 64, 67], [53, 57, 60, 62], [59, 62, 65, 67]],
    2: [[64, 71], [60, 67], [53, 60], [59, 65]],
    3: [[64, 71], [60, 67], [53, 60, 64], [59, 65]],
    4: [[64, 71], [60, 67], [53, 60], [59, 65, 69]],
    5: [[64, 71, 74], [60, 67], [53, 60], [59, 65]],
}
patterns = {1: (0, 1.5, 3), 2: (1, 2.5)}
stages, progressions, events, notes = [], [], [], []
titles = ['Voicings densos', 'Reducir a shells', 'Una novena en Dm9', 'Color puntual en G9', 'Elegir un color']
explanations = [
    'Base A: célula fija de dos compases de bossa, repetida dos veces. La derecha presenta voicings densos de cuatro notas.',
    'Frente a A (01), solo cambia la densidad derecha: shells con tercera y séptima; bajo y célula rítmica permanecen idénticos.',
    'Frente a A (02), solo Dm7 recibe E4 como novena y pasa a Dm9; los otros shells, el bajo y todos los ataques siguen iguales.',
    'Reinicio A (02): se retira E4 de Dm y vuelve Dm7 shell simple. Novedad única: G7 recibe A4 como novena y pasa a G9.',
    'Reinicio A (02): se quita la novena de G y Dm sigue simple. Novedad: Cmaj7 recibe D5 como novena, Cmaj9. Elige densidad/color, sin alterar la célula ni añadir melodía.',
]
for stage_no in range(1, 6):
    sid = f'stage-accompaniment-010-{stage_no:02}'
    pid = f'prog-accompaniment-010-{stage_no:02}-primary'
    stages.append({'id': sid, 'lessonId': 'lesson-accompaniment-010', 'order': stage_no, 'title': titles[stage_no-1], 'explanationMd': explanations[stage_no-1], 'task': 'Toca los cuatro compases con la mano izquierda en raíz y quinta en los tiempos 1 y 3; conserva exactamente los ataques de la célula derecha.', 'changeFromPrevious': explanations[stage_no-1], 'successCriteria': ['Mantengo sin cambios los ataques derechos: compases 1 y 3 en 1, 2&, 4; compases 2 y 4 en 2, 3&.', 'Toco en la izquierda raíz y quinta en los tiempos 1 y 3, cada nota durante dos pulsos.', 'Conservo tercera y séptima en cada voicing; no agrego una melodía ni cambio el ritmo.'], 'simplifyHint': 'Practica primero la izquierda; luego toca solo el shell derecho en sus ataques escritos, sin cambiar sus silencios.', 'extendHint': 'Elige dónde conservar shells y dónde usar la novena permitida, comparando densidad y color sin desplazar ningún ataque.'})
    progressions.append({'id': pid, 'stageId': sid, 'kind': 'primary', 'order': 1, 'title': titles[stage_no-1], 'keyTonic': 'C', 'keyMode': 'major', 'style': 'bossa', 'bpm': 100, 'timeSignature': {'numerator': 4, 'denominator': 4}, 'totalBars': 4, 'description': 'Reducción de bossa de dos compases repetida: bajo en 1 y 3; acordes breves en la célula derecha 1/2&/4 y 2/3&. No representa por sí sola todo el género.', 'loopable': False})
    for i, (symbol, function, bass_root, bass_fifth, dense) in enumerate(chords):
        start = i * 4
        chord_symbol = symbol
        if stage_no == 3 and i == 2: chord_symbol = 'Dm9'
        if stage_no == 4 and i == 3: chord_symbol = 'G9'
        if stage_no == 5 and i == 0: chord_symbol = 'Cmaj9'
        events.append({'id': f'chord-accompaniment-010-{stage_no:02}-{i+1:03}', 'progressionId': pid, 'order': i+1, 'symbol': chord_symbol, 'function': function, 'startBeat': start, 'durationBeats': 4})
        for beat, pitch in ((0, bass_root), (2, bass_fifth)):
            notes.append({'id': f'note-accompaniment-010-{stage_no:02}-{i+1:03}-bass-{beat}', 'progressionId': pid, 'midi': pitch, 'startBeat': start+beat, 'durationBeats': 2, 'velocity': 60, 'role': 'bass', 'hand': 'left'})
        pitches = dense if stage_no == 1 else rh[stage_no][i]
        for beat in patterns[1 if i % 2 == 0 else 2]:
            for pitch in pitches:
                notes.append({'id': f'note-accompaniment-010-{stage_no:02}-{i+1:03}-rh-{int(beat*10):02}-{pitch}', 'progressionId': pid, 'midi': pitch, 'startBeat': start+beat, 'durationBeats': 0.5, 'velocity': 64, 'role': 'harmony', 'hand': 'right'})
for filename, data in [('stages', stages), ('progressions', progressions), ('chord-events', events), ('note-events', notes)]:
    (out / f'{filename}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
