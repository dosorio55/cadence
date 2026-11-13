import json
from pathlib import Path

root = Path(__file__).parent

def load(name):
    return json.loads((root / f'{name}.json').read_text())
def save(name, data):
    (root / f'{name}.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

stages, lessons = load('stages'), load('lessons')
progressions, notes = load('progressions'), load('note-events')
S = {x['id']: x for x in stages}
L = {x['id']: x for x in lessons}
P = {x['id']: x for x in progressions}
N = {x['id']: [] for x in progressions}
for n in notes:
    N[n['progressionId']].append(n)

def stage(num, order):
    return S[f'stage-expression-{num}-{order:02d}']
def prog(num, order):
    return P[f'prog-expression-{num}-{order:02d}-primary']
def subset(num, order):
    return N[f'prog-expression-{num}-{order:02d}-primary']
def rewrite(num, order, **fields):
    stage(num, order).update(fields)

# 007: offset RH by 1.5 in all parts; durations differ only in hands.
for order, duration in enumerate((0.5, 0.5, 0.25, 0.5), 1):
    rows = subset('007', order)
    for n in rows:
        bar = int(n['startBeat'] // 4)
        within = n['startBeat'] - bar * 4
        if n['hand'] == 'left':
            n['startBeat'] = bar * 4 + (0 if within < 1 else 2)
            n['durationBeats'] = 2
        else:
            n['startBeat'] = bar * 4 + ({1: 1, 2.5: 1.5, 3: 3}[within])
            n['durationBeats'] = duration
            if bar == 3 and n['midi'] == 67:
                n['midi'] = 65

text007 = [
('Pulso compartido', 'Referencia de bolero en cuatro compases: LH en 1 y 3; RH responde en 2, 2& y 4.', 'Toca los ataques escritos; la RH entra en 2, 2& y 4, con un desplazamiento de 1.5 beats respecto a la LH.', 'Presentación: LH beats 0 y 2; RH beats 1, 1.5 y 3 en cada compás. Todas las notas duran 0.5 beats.', ['LH ataca en 0/2 y RH en 1/1.5/3 en cada compás; todas las notas duran 0.5 beats.', 'Mantengo alturas y velocities constantes y puedo explicar la diferencia de ataques.'], 'Cuenta 1-2-3-4; la derecha entra en 2, 2& y 4.', 'Conserva ataques y compara el toque parejo de ambas manos.'),
('Respuesta breve', 'Los ataques y alturas coinciden con la etapa 1; ahora solo la LH sostiene dos beats y la RH dura medio beat.', 'Mantén las notas izquierdas durante dos beats y suelta cada respuesta derecha tras medio beat.', 'Solo cambia duración LH: 0.5→2 beats. RH permanece en 0.5; alturas, ataques y velocities quedan idénticos.', ['Cada nota LH dura 2 beats y RH 0.5; los ataques no se mueven.', 'Conservo pitches y velocities y oigo la diferencia real de duración entre manos.'], 'Cuenta dos beats para cada nota LH y medio beat para RH.', 'Compara ambas duraciones manteniendo los mismos ataques.'),
('Respuestas muy breves', 'La RH se separa aún más: dura un cuarto de beat; la LH mantiene sus dos beats.', 'Sostén LH dos beats y suelta RH tras un cuarto de beat, sin cambiar ataques.', 'Solo RH cambia 0.5→0.25 beats. LH queda en 2; pitches, ataques y velocities son idénticos.', ['RH dura 0.25 beats y LH 2; ningún ataque se desplaza.', 'Las alturas y velocities permanecen constantes.'], 'Suelta cada respuesta RH tras un cuarto de pulso; sostén LH dos beats.', 'Compara 0.25 de RH con LH 2 sin variar las demás notas.'),
('Elige el rebote', 'Referencia abierta: LH dura 2 beats; puedes elegir para cada respuesta RH entre 0.25 y 0.5, sin mover ataques.', 'Elige duraciones RH de 0.25 o 0.5 y conserva LH en 2; mantén alturas, velocities y ataques.', 'El ejemplo fija RH en 0.5 beats frente a 0.25 en etapa 3; LH sigue en 2 y todos los ataques y alturas quedan idénticos. La elección puede variar RH entre 0.25 y 0.5.', ['Conservo los ataques y pitches; LH dura 2 y elijo RH 0.25 o 0.5.', 'Las velocities no cambian entre las notas.'], 'Practica RH a 0.5, luego a 0.25; no muevas ningún inicio.', 'Elige entre 0.25 y 0.5 para cada respuesta sin mover ataques.')]
for i, (title, explanation, task, change, criteria, hint, extend) in enumerate(text007, 1):
    rewrite('007', i, title=title, explanationMd=explanation, task=task, changeFromPrevious=change, successCriteria=criteria, simplifyHint=hint, extendHint=extend)
    prog('007', i)['description'] = 'Bolero de cuatro compases; LH en 1/3 y RH en 2/2&/4 (desfase 1.5 beats). '

# 008: stage 1 is full silence, 2 adds only LH in bar 2; existing 3/4 patterns retained.
for order in (1, 2):
    pid = f'prog-expression-008-{order:02d}-primary'
    N[pid][:] = [n for n in N[pid] if not (4 <= n['startBeat'] < 8)]
    if order == 2:
        template = [n for n in subset('008', 3) if n['hand'] == 'left' and 4 <= n['startBeat'] < 8]
        for original in template:
            clone = dict(original)
            clone['id'] = clone['id'].replace('008-03-', '008-02-')
            clone['progressionId'] = pid
            N[pid].append(clone)
        N[pid].sort(key=lambda n: (n['startBeat'], n['hand'], n['midi']))

rewrite('008', 1, title='Pausa total', explanationMd='En cuatro compases, el segundo compás completo [4,8) queda en silencio: no toca ninguna mano. Los compases 1, 3 y 4 conservan la frase y el acompañamiento.', task='Toca los compases 1, 3 y 4; cuenta en silencio todo el segundo compás, sin dejar notas sostenidas.', changeFromPrevious='Presentación: se retiran únicamente todos los ataques LH y RH con inicio en [4,8); los demás eventos permanecen idénticos.', successCriteria=['Ninguna nota de ninguna mano suena durante [4,8); los compases 1, 3 y 4 no cambian.', 'Cuento cuatro compases y mantengo el pulso durante el silencio total.'], simplifyHint='Cuenta 1-2-3-4 durante [4,8) sin tocar ni sostener ninguna nota.', extendHint='Sostén el pulso interno durante el compás entero de silencio.')
rewrite('008', 2, title='La base vuelve primero', explanationMd='Frente a la pausa total de la etapa 1, en [4,8) vuelve solo la LH en beats 4 y 6; la RH sigue en silencio.', task='Durante el segundo compás toca solo LH en 1 y 3; deja ambas manos fuera antes y después de esos ataques.', changeFromPrevious='Se añaden únicamente dos notas LH en beats 4 y 6 respecto a la pausa total de etapa 1; RH permanece ausente en [4,8).', successCriteria=['En [4,8) solo ataca LH en beats 4 y 6; RH no toca y los otros compases son idénticos a etapa 1.', 'Mantengo el pulso durante los espacios entre esos dos ataques.'], simplifyHint='Aísla LH en beats 4 y 6; no agregues RH durante el segundo compás.', extendHint='Contrasta la pausa total de etapa 1 con la base LH sola de esta etapa.')
rewrite('008', 3, title='Prepara la respuesta', explanationMd='El hueco de ambas manos sigue siendo [4,8); la nota derecha de beat 8 destaca como reentrada.', task='Mantén el silencio total durante [4,8) y articula con claridad la vuelta derecha en 8.', changeFromPrevious='Solo la velocity de RH en beat 8 aumenta de 64 a 76; alturas, ataques, duraciones y LH quedan iguales.', successCriteria=['Ninguna mano toca durante [4,8); la primera nota tras el silencio entra en beat 8 con velocity 76.', 'Puedo identificar la diferencia concreta de esta etapa frente a la anterior.'], simplifyHint='Cuenta ambas manos en silencio en [4,8) y reentra con RH exactamente en 8.', extendHint='Compara la pausa total con la reentrada en 8 manteniendo el pulso.')
rewrite('008', 4, title='Diseña tu respiración', explanationMd='El ejemplo conserva el silencio total de ambas manos en [4,8); puedes elegir otro hueco y una reentrada sin alterar los demás compases.', task='Elige un espacio de respiración y conserva el pulso; en la referencia, ambas manos callan durante [4,8).', changeFromPrevious='La referencia reduce solo velocity de RH en beat 8 de 76 a 68. Puede mantenerse tal cual; si se elige otro hueco, los demás eventos se conservan.', successCriteria=['Puedo contar los cuatro compases y describir exactamente qué manos callan en la referencia.', 'No afirmo continuidad LH durante el compás de referencia [4,8).'], simplifyHint='Usa la referencia: ambas manos callan en [4,8), con ataques LH/RH intactos en los otros compases.', extendHint='Elige otro hueco melódico si quieres; especifica qué acompañamiento continúa, sin alterar otros eventos.')
for i in range(1, 5):
    prog('008', i)['description'] = ('Cuatro compases; la referencia deja silencio total de ambas manos en [4,8).' if i == 1 else 'Cuatro compases; en [4,8) solo LH toca en 4 y 6, RH calla.' if i == 2 else 'Cuatro compases; ambas manos callan en [4,8), con RH reentrada en 8.' if i == 3 else 'Cuatro compases; la referencia calla con ambas manos en [4,8); se puede elegir otro hueco.')

# 009: actual prepared C5 starts on beat 4 and sustains over G7.
for order in range(1, 5):
    rows = subset('009', order)
    melody = [n for n in rows if n['role'] == 'melody' and n['hand'] == 'right' and n['midi'] == 72]
    assert len(melody) == 1, (order, [(n['midi'], n['startBeat']) for n in melody])
    c5 = melody[0]
    c5.update(midi=72, startBeat=4, role='melody', hand='right', velocity=78 if order >= 3 else 68)
    if order == 1:
        c5['durationBeats'] = 8
    elif order in (2, 3):
        c5['durationBeats'] = 5
    else:
        c5['durationBeats'] = 5.5
    b4 = next((n for n in rows if n['midi'] == 59 and n['startBeat'] >= 8), None)
    if order == 1:
        if b4:
            rows.remove(b4)
    else:
        if b4 is None:
            b4 = dict(c5)
            b4['id'] = c5['id'].rsplit('-', 1)[0] + '-0002'
            b4['midi'] = 71
            rows.append(b4)
        b4.update(midi=71, startBeat=9.5 if order == 4 else 9, durationBeats=2.5 if order == 4 else 3, velocity=78 if order >= 3 else 68, role='melody', hand='right')
    rows.sort(key=lambda n: (n['startBeat'], n['hand'], n['midi']))

rewrite('009', 1, title='Prepara el retardo', explanationMd='C5 se prepara sobre Am7 desde beat 4 y queda sostenido cuando G7 entra en 8; la tensión aún no resuelve antes de Cmaj7 en 12.', task='Prepara C5 en beat 4 sobre Am7, sosténlo a través de G7 desde 8 y escucha Cmaj7 al llegar a 12.', changeFromPrevious='Presentación: C5 entra en beat 4, dura 8 beats hasta 12 y queda suspendido sobre G7 en [8,12).', successCriteria=['C5 empieza en 4, dura 8 y atraviesa G7 desde 8 hasta su llegada a Cmaj7 en 12.', 'G7 mantiene su tercera F4; no hay B4 antes del acorde final.'], simplifyHint='Prepara C5 en 4; siente el cambio armónico a G7 en 8 sin reatacar C5.', extendHint='Compara la suspensión que sigue sin resolver hasta I en 12.')
rewrite('009', 2, title='Introduce la resolución 4–3', explanationMd='C5 se prepara en beat 4 sobre Am7, se sostiene al entrar G7 en 8 y resuelve a B4 en 9, antes de Cmaj7 en 12.', task='Toca C5 desde 4, sostenlo sobre G7 desde 8, y cambia a B4 en 9 hasta la llegada de Cmaj7 en 12.', changeFromPrevious='Solo se divide la voz superior: C5 dura 5 beats (4–9) y B4 entra en 9 durante 3 beats; demás eventos no cambian.', successCriteria=['C5 inicia en 4 y sostiene sobre G7 desde 8; B4 inicia en 9 y termina en 12.', 'Oigo la resolución 4–3 antes de Cmaj7; G7 conserva F4.'], simplifyHint='Cuenta C5 en 4, G7 en 8, B4 en 9 y Cmaj7 en 12.', extendHint='Practica C5 preparado en 4 y su resolución a B4 en 9 sobre G7.')
rewrite('009', 3, title='Balancea el retardo', explanationMd='La resolución preparada C5→B4 permanece; destaca ambas notas de la voz superior frente al acompañamiento.', task='Mantén C5 desde 4, sostenlo sobre G7 desde 8 y destaca su resolución a B4 en 9.', changeFromPrevious='Solo suben velocity C5 y B4 de 68 a 78; C5 (4–9), B4 (9–12) y las demás notas no cambian.', successCriteria=['C5 preparada en 4 cruza G7 desde 8; B4 entra en 9 y termina en 12.', 'Solo C5/B4 llevan velocity 78; otras notas conservan su velocity.'], simplifyHint='Compara la voz C5→B4 con el voicing durante la llegada a G7.', extendHint='Balancea la voz superior sin cambiar sus ataques ni los del acompañamiento.')
rewrite('009', 4, title='Elige cuánto retener', explanationMd='La referencia prolonga C5 desde beat 4 hasta 9.5 sobre G7 y resuelve a B4 hasta beat 12; velocities permanecen en 78.', task='Prepara C5 en 4, sosténlo sobre G7 desde 8 y elige la resolución a B4 en 9.5, antes de Cmaj7 en 12.', changeFromPrevious='Solo se retrasa la resolución: C5 dura 5.5 beats (4–9.5) y B4 entra en 9.5 durante 2.5 beats. Velocities siguen en 78.', successCriteria=['C5 empieza en 4 y cruza G7 en 8; B4 empieza en 9.5 y termina justo en 12.', 'Velocities C5/B4 son 78; Cmaj7 ataca en 12 sin solapamiento de B4.'], simplifyHint='Compara B4 en 9.5 con la entrada en 9 de etapa 3; conserva el final en 12.', extendHint='Elige cuánto sostener C5 sobre G7; deja B4 concluir justo en 12 sin resetear velocities.')
for i in range(1, 5):
    prog('009', i)['description'] = 'C5 preparado desde beat 4 sobre Am7; se sostiene sobre G7 desde 8 y resuelve a B4 en ' + ('12' if i == 1 else '9' if i in (2, 3) else '9.5') + '. G7 conserva F4; Cmaj7 comienza en 12.'

# Update lesson-level framing for the actual contrasts.
L['lesson-expression-007']['goal'] = 'Mantener la célula de bolero con LH sostenida dos beats y elegir duraciones breves para RH sin mover ataques ni variar alturas o velocities.'
L['lesson-expression-007']['introMd'] = 'En cuatro compases de bolero, LH ataca en 1 y 3 y RH en 2, 2& y 4, desplazada 1.5 beats. Compara toques de igual duración con LH de dos beats y RH breve; conserva alturas, velocidades y ataques.'
L['lesson-expression-008']['introMd'] = 'En cuatro compases de balada, la referencia deja a ambas manos en silencio total durante el segundo compás [4,8). Luego compara con la etapa que añade solo LH en 1 y 3 de ese compás; cuenta el pulso y no confundas esta pausa con una respiración sobre base.'
L['lesson-expression-009']['goal'] = 'Preparar C5 sobre Am7 en beat 4, sostenerla sobre G7 desde 8 y resolver a B4 en 9 o 9.5 antes de Cmaj7 en 12, equilibrando la voz superior.'
L['lesson-expression-009']['introMd'] = 'En cuatro compases de jazz lento, prepara C5 en beat 4 sobre Am7; sostenla sobre G7 desde beat 8 y resuelve a B4 en 9 o 9.5 antes de Cmaj7 en 12. Compara el retardo sin resolver con 4–3; la tercera F4 de G7 permanece y no se añade otro acorde.'

save('stages', stages)
save('lessons', lessons)
save('progressions', progressions)
save('note-events', notes)
