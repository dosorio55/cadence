#!/usr/bin/env python3
"""Aplica las correcciones R-B02-001–003 sin alterar otros lotes."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / 'drafts' / 'rhythm'


def load(name):
    return json.loads((WORK / f'{name}.json').read_text(encoding='utf-8'))


def save(name, rows):
    (WORK / f'{name}.json').write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8'
    )

notes = load('note-events')
stages = load('stages')
progressions = load('progressions')
original_005_rhythm = {
    (row['id'], row['startBeat'], row['durationBeats'])
    for row in notes if row['progressionId'].startswith('prog-rhythm-005-')
}
original_007_ids_durations = {
    (row['id'], row['durationBeats'])
    for row in notes if row['progressionId'].startswith('prog-rhythm-007-')
}
protected_notes = [row.copy() for row in notes
                   if not row['progressionId'].startswith(('prog-rhythm-005-', 'prog-rhythm-007-'))]
protected_stages = [row.copy() for row in stages if not row['id'].startswith('stage-rhythm-007-')]
protected_progressions = [row.copy() for row in progressions
                          if not row['id'].startswith('prog-rhythm-007-')]

# Correct the bass roots and melodic resolution while preserving every rhythm event.
for note in notes:
    pid = note['progressionId']
    if not pid.startswith('prog-rhythm-005-'):
        continue

    bar = int(note['startBeat'] // 4)
    if note['hand'] == 'left' and note['role'] == 'bass':
        note['midi'] = (38, 43, 48, 48)[bar]
    elif note['hand'] == 'right' and note['role'] == 'melody':
        note['midi'] = (69, 65, 64, 64)[bar]

# 007 patterns contain four chord attacks per bar in every stage.
patterns = {
    1: (0, 0.5, 2, 2.5),
    2: (0, 0.25, 2, 2.25),
    3: (0, 0.25, 2, 2.5),
    4: (0, 0.5, 2, 2.25),
}
for stage_order, offsets in patterns.items():
    pid = f'prog-rhythm-007-{stage_order:02d}-primary'
    right_events = [row for row in notes if row['progressionId'] == pid and row['hand'] == 'right']
    for bar in range(4):
        bar_start = bar * 4
        attacks = sorted({round(row['startBeat'] - bar_start, 8) for row in right_events
                          if bar_start <= row['startBeat'] < bar_start + 4})
        assert len(attacks) == 4, (pid, bar, attacks)
        assert len(offsets) == 4
        for old_offset, new_offset in zip(attacks, offsets):
            for row in right_events:
                if abs(row['startBeat'] - (bar_start + old_offset)) < 1e-8:
                    row['startBeat'] = bar_start + new_offset

stage_edits = {
    'stage-rhythm-007-01': {
        'title': 'Corcheas seleccionadas con huecos',
        'explanationMd': 'A = base de C7: cuatro stabs derechos por compás en corcheas seleccionadas, offsets locales 0, 0.5, 2 y 2.5 (tiempos musicales 1, 1&, 3 y 3&). Bajo y voicing permanecen iguales; hay huecos entre las parejas.',
        'changeFromPrevious': 'Base comparativa: se seleccionan cuatro ataques derechos de corchea por compás (offsets 0/0.5 y 2/2.5), con el mismo C7, voicing y bajo que las etapas siguientes.',
        'successCriteria': ['Reconozco las dos parejas de corcheas y cuento los huecos sin añadir ataques.'],
    },
    'stage-rhythm-007-02': {
        'title': 'Agrupar semicorcheas con huecos',
        'explanationMd': 'A = etapa 01, offsets derechos 0, 0.5, 2 y 2.5. B = esta etapa, offsets 0, 0.25, 2 y 2.25: solo se adelantan 0.25 beat los segundos ataques de cada pareja. Conserva cuatro ataques por compás, voicing C7 y bajo.',
        'changeFromPrevious': 'Con el mismo número de ataques, las posiciones 0.5 y 2.5 pasan a 0.25 y 2.25; bajo, alturas, duración 0.25 y armonía no cambian.',
        'successCriteria': ['Toco las dos parejas de semicorcheas con cuatro ataques por compás y sin rellenar los huecos.'],
    },
    'stage-rhythm-007-03': {
        'title': 'Desplazar un ataque',
        'explanationMd': 'A = etapa 02, offsets locales derechos 0, 0.25, 2 y 2.25. B = esta etapa: solo el ataque en 2.25 pasa a 2.5; 0, 0.25 y 2, además del bajo y voicing, quedan idénticos.',
        'changeFromPrevious': 'Se mueve un único bloque de la derecha 0.25 beat: offset 2.25→2.5 en cada compás. Los otros tres ataques, bajo, voicing y cuatro ataques totales permanecen iguales.',
        'successCriteria': ['Oigo el desplazamiento de un ataque de 2.25 a 2.5 sin mover los otros ni sumar notas.'],
    },
    'stage-rhythm-007-04': {
        'title': 'Elegir otro ataque',
        'explanationMd': 'A = etapa 02, no la etapa 03: restablece primero sus offsets 0, 0.25, 2 y 2.25. B de referencia = 0, 0.5, 2 y 2.25: elige mover solo el ataque 0.25→0.5. Puedes elegir otro ataque único; no combines desplazamientos.',
        'changeFromPrevious': 'Se reinicia explícitamente desde A=etapa 02. Frente a esa A, B mueve solo un ataque 0.25→0.5; offsets 0, 2 y 2.25 quedan iguales. No conserva el cambio de 03 ni desplaza ambas parejas.',
        'successCriteria': ['Elijo un único ataque distinto para desplazar 0.25 beat y mantengo los otros tres, el voicing y la densidad.'],
    },
}
for row in stages:
    edit = stage_edits.get(row['id'])
    if edit:
        row.update(edit)

for row in progressions:
    progression_id = row['id']
    stage_order = next((order for order in (1, 2, 3, 4)
                        if progression_id == f'prog-rhythm-007-{order:02d}-primary'), None)
    if stage_order is not None:
        row['title'] = stage_edits[f'stage-rhythm-007-{stage_order:02d}']['title']
        row['description'] = stage_edits[f'stage-rhythm-007-{stage_order:02d}']['changeFromPrevious']

assert original_005_rhythm == {
    (row['id'], row['startBeat'], row['durationBeats'])
    for row in notes if row['progressionId'].startswith('prog-rhythm-005-')
}, 'La corrección cambió onset o duración de 005.'
assert original_007_ids_durations == {
    (row['id'], row['durationBeats'])
    for row in notes if row['progressionId'].startswith('prog-rhythm-007-')
}, 'La corrección cambió IDs o duraciones de 007.'
assert protected_notes == [row for row in notes
                           if not row['progressionId'].startswith(('prog-rhythm-005-', 'prog-rhythm-007-'))]
assert protected_stages == [row for row in stages if not row['id'].startswith('stage-rhythm-007-')]
assert protected_progressions == [row for row in progressions
                                  if not row['id'].startswith('prog-rhythm-007-')]

save('note-events', notes)
save('stages', stages)
save('progressions', progressions)
