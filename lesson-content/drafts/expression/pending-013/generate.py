import json
import struct
from pathlib import Path

root = Path(__file__).parent
source = root.parent / "pending-012" / "checks"
out = root
lesson_id = "lesson-expression-013"

design_lessons = json.loads((source / "lessons.json").read_text())
canonical_lesson = next(x for x in design_lessons if x["id"] == lesson_id)
(out / "lessons.json").write_text(json.dumps([canonical_lesson], ensure_ascii=False, indent=2) + "\n")

chords_by_bar = ["Cmaj7", "Am7", "Dm7", "G7", "Cmaj7", "Am7", "G7", "Cmaj7"]
functions = ["I", "vi", "ii", "V", "I", "vi", "V", "I"]
lhs = [[48, 52, 59], [45, 48, 55], [50, 53, 60], [43, 47, 53], [48, 52, 59], [45, 48, 55], [43, 47, 53], [48, 52, 59]]
rhs = [[64, 67, 64, 67], [64, 67, 64, 67], [65, 69, 65, 69], [71, 65, 71, 65], [64, 67, 64, 67], [64, 67, 64, 67], [71, 65, 71, 65], [64, 72, 64, 72]]
titles = ["Frase llena", "Respirar en la dominante", "Restablecer y respirar", "Elegir una llegada"]
explanations = [
    "Versión de referencia completa: la izquierda toca bloques de tres notas durante cuatro pulsos; la derecha frasea cuatro ataques swung por compás. Tempo estable de 72 BPM.",
    "Se restablece la versión 01 y la derecha calla en los ataques de 15 y 15⅔, creando silencio [13,16); la izquierda mantiene el bloque de G7 en el compás 4.",
    "Se restablece la versión 01 y la derecha calla en los ataques de 27 y 27⅔, creando silencio [25,28); la izquierda mantiene el bloque de G7 en el compás 7. No se acumula el silencio de la etapa 02.",
    "Conserva la reducción y el silencio [25,28) de la etapa 03. La llegada en el compás 8, beat 28, pasa de velocity 72 a 84; se conserva el par swing precedente y la izquierda sigue sin cambio. No es silencio total ni cambio de tempo."
]
tasks = [
    "Toca ambas manos durante ocho compases a 72 BPM: bloques izquierdos y línea derecha en pares swung; mantén el pulso y distingue melodía de acompañamiento.",
    "Repite exactamente la versión llena de la etapa 01 salvo los dos ataques derechos de 15 y 15⅔, que se omiten. Cuenta el hueco [13,16) mientras la izquierda sostiene su bloque normal.",
    "Vuelve a la versión 01 y omite únicamente los ataques derechos de 27 y 27⅔. El silencio [25,28) reemplaza, no suma, al hueco del compás 4; la izquierda continúa.",
    "Mantén el arreglo y la pausa de la etapa 03. Haz audible la llegada de la derecha en beat 28 con velocity 84 (antes 72); conserva el swing de los pares cercanos y toca siempre los bloques izquierdos."
]
criteria = [
    ["Hay cuatro ataques derechos por compás en los beats 0, ⅔, 2, 2⅔ relativos; duran ⅔, ⅓, ⅔, ⅓ y tienen velocity 72.", "La izquierda toca el bloque indicado al inicio de cada compás durante cuatro pulsos, velocity 55; ambas manos sostienen ocho compases a 72 BPM."],
    ["Se omiten solo los ataques derechos en beats globales 15 y 15⅔; el resto de la versión 01 permanece idéntico.", "La derecha queda en silencio de beat 13 a 16 y la izquierda mantiene normalmente el bloque del compás 4."],
    ["La etapa vuelve a la versión llena y omite solo los ataques derechos en beats 27 y 27⅔, no los del compás 4.", "La derecha calla de beat 25 a 28 mientras la izquierda conserva el bloque del compás 7."],
    ["La reducción y el silencio [25,28) de la etapa 03 se conservan; la única alteración nueva es velocity 84 en la llegada derecha de beat 28.", "La izquierda permanece intacta; no hay tercera mano, silencio total ni cambio de BPM."]
]
stages, progressions, chord_events, note_events = [], [], [], []
for n in range(1, 5):
    sid = f"stage-expression-013-{n:02}"
    pid = f"prog-expression-013-{n:02}-primary"
    desc = explanations[n - 1]
    stages.append({"id": sid, "lessonId": lesson_id, "order": n, "title": titles[n - 1], "explanationMd": desc, "task": tasks[n - 1], "changeFromPrevious": "Versión llena de referencia; establece el patrón común de manos, armonía, tempo y swing." if n == 1 else desc, "successCriteria": criteria[n - 1], "simplifyHint": ["Practica cada mano por separado; subdivide cada pulso en tres y acentúa la primera corchea del par swung.", "Cuenta en voz alta 13–16; retira solo esos dos ataques derechos y sigue tocando la izquierda.", "Reinicia mentalmente desde la etapa 01; cuenta 25–28 y deja solo a la derecha en silencio.", "Practica primero la etapa 03; luego acentúa únicamente el ataque derecho de beat 28, sin modificar el bajo."][n - 1], "extendHint": ["Canta la línea derecha mientras tocas el bloque izquierdo; no añadas otra parte.", "Toca el hueco de la derecha imaginando su subdivisión, sin rellenarlo y con la izquierda presente.", "Cuenta el silencio derecho y prepara la llegada del compás 8 sobre el bloque izquierdo continuo.", "Elige si la llegada destacada debe ser en beat 16 o 28; aquí se elige beat 28 y se conserva su par swung previo."][n - 1]})
    progressions.append({"id": pid, "stageId": sid, "kind": "primary", "order": 1, "title": titles[n - 1], "keyTonic": "C", "keyMode": "major", "style": "jazz", "bpm": 72, "timeSignature": {"numerator": 4, "denominator": 4}, "totalBars": 8, "description": desc, "loopable": False})
    for bar, symbol in enumerate(chords_by_bar):
        start = bar * 4
        chord_events.append({"id": f"ce-expression-013-{n:02}-{bar + 1:02}", "progressionId": pid, "order": bar + 1, "symbol": symbol, "function": functions[bar], "startBeat": start, "durationBeats": 4})
        for j, pitch in enumerate(lhs[bar]):
            note_events.append({"id": f"ne-expression-013-{n:02}-{bar + 1:02}-left-{j + 1}", "progressionId": pid, "midi": pitch, "startBeat": start, "durationBeats": 4, "velocity": 55, "role": "harmony", "hand": "left"})
        for j, pitch in enumerate(rhs[bar]):
            beat = start + [0, 2 / 3, 2, 8 / 3][j]
            if (n == 2 and bar == 3 and j >= 2) or (n in (3, 4) and bar == 6 and j >= 2):
                continue
            velocity = 84 if n == 4 and bar == 7 and j == 0 else 72
            note_events.append({"id": f"ne-expression-013-{n:02}-{bar + 1:02}-right-{j + 1}", "progressionId": pid, "midi": pitch, "startBeat": beat, "durationBeats": [2 / 3, 1 / 3, 2 / 3, 1 / 3][j], "velocity": velocity, "role": "melody", "hand": "right"})

for name, data in (("stages", stages), ("progressions", progressions), ("chord-events", chord_events), ("note-events", note_events)):
    (out / f"{name}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

checks = out / "checks"
checks.mkdir(exist_ok=True)
for name in ("categories", "skills", "lessons", "stages", "progressions", "chord-events", "note-events"):
    data = json.loads((source / f"{name}.json").read_text())
    if name == "stages":
        data = [x for x in data if x["lessonId"] != lesson_id] + stages
    elif name == "progressions":
        data = [x for x in data if not x["id"].startswith("prog-expression-013-")] + progressions
    elif name == "chord-events":
        data = [x for x in data if not x["progressionId"].startswith("prog-expression-013-")] + chord_events
    elif name == "note-events":
        data = [x for x in data if not x["progressionId"].startswith("prog-expression-013-")] + note_events
    (checks / f"{name}.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")

# Minimal Standard MIDI format 0 writer for a single track.
def vlq(value):
    result = [value & 0x7f]
    value >>= 7
    while value:
        result.insert(0, (value & 0x7f) | 0x80)
        value >>= 7
    return bytes(result)

for n in range(1, 5):
    pid = f"prog-expression-013-{n:02}-primary"
    track = bytearray()
    events = [(0, bytes([0xff, 0x51, 3, 0x0c, 0xb7, 0x35])), (0, bytes([0xff, 0x58, 4, 4, 2, 24, 8]))]
    selected = [e for e in note_events if e["progressionId"] == pid]
    for e in selected:
        on = round(e["startBeat"] * 960)
        off = round((e["startBeat"] + e["durationBeats"]) * 960)
        events.extend([(on, bytes([0x90, e["midi"], e["velocity"]])), (off, bytes([0x80, e["midi"], 0]))])
    events.append((8 * 4 * 960, bytes([0xff, 0x2f, 0])) )
    last = 0
    for tick, msg in sorted(events, key=lambda x: (x[0], x[1][0] == 0x90)):
        track.extend(vlq(tick - last) + msg)
        last = tick
    midi = b"MThd" + struct.pack(">IHHH", 6, 0, 1, 960) + b"MTrk" + struct.pack(">I", len(track)) + track
    (out / f"prog-expression-013-{n:02}-primary.mid").write_bytes(midi)
