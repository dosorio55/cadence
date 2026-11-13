import json
import struct
from pathlib import Path

root = Path(__file__).parent
checks = root / "checks"
checks.mkdir(parents=True, exist_ok=True)
design = json.loads((root.parent.parent.parent / "approved/lessons.json").read_text())
lesson = next(row for row in design if row["id"] == "lesson-harmony-013")
(root / "lessons.json").write_text(json.dumps([lesson], ensure_ascii=False, indent=2) + "\n")

bars = [
    ("Cmaj7", "Imaj7", 48, [64, 71]),
    ("Em7", "iii7", 52, [67, 74]),
    ("Am", "vi", 45, [69, 72]),
    ("Dm7", "ii7", 50, [65, 72]),
    ("Dm7", "ii7", 50, [65, 72]),
    ("G", "V", 43, [67, 71]),
    ("Cmaj7", "Imaj7", 48, [64, 71]),
    ("C", "I", 48, [60, 64, 67]),
]
variants = [
    {"title": "Referencia diatónica", "e7": False, "d7": False},
    {"title": "Tonicizar vi", "e7": True, "d7": False},
    {"title": "Dos destinos encadenados", "e7": True, "d7": True},
    {"title": "Conservar solo V/V", "e7": False, "d7": True},
]
stages, progressions, chord_events, note_events = [], [], [], []

for index, variant in enumerate(variants, 1):
    suffix = f"{index:02}"
    stage_id = f"stage-harmony-013-{suffix}"
    progression_id = f"prog-harmony-013-{suffix}-primary"
    delta = ["Referencia de ocho compases; establece armonía diatónica y voicings reducidos.",
             "Solo cambia el compás 2: Em7 pasa a E7 y G4 a G#4; en Am del compás 3, G#4 resuelve a A4 y D5 baja a C5.",
             "Se conserva íntegra la etapa 02; solo cambia el compás 5 a D7 y F4 a F#4. En G del compás 6, F#4 resuelve a G4 y C5 baja a B4.",
             "Desde la etapa 03, solo se restaura Em7 y G4 en el compás 2. Se conserva D7 del compás 5; no se mantienen ambas dominantes."][index - 1]
    stage_titles = ["Referencia diatónica", "V/vi → vi", "V/V → V", "Elegir una preparación"][index - 1]
    stages.append({"id": stage_id, "lessonId": lesson["id"], "order": index, "title": stage_titles,
        "explanationMd": delta + " Cada acorde dura un compás; bajo a 60 y voces derechas a 64, con ataques en cada inicio de compás. Los shells de Em7 y Dm7 conservan tercera y séptima sin quinta; Am conserva raíz y tercera, sin quinta. Cmaj7 usa tercera y séptima; el último C es tríada completa. Así se reconoce calidad mayor/menor sin fingir acordes completos en los shells. E7 cumple V/vi → vi y D7 cumple V/V → V: G# y F# no son diatónicos en do mayor, pero tonicizan destinos locales, no establecen una modulación.", 
        "task": ["Toca ocho compases a 72 BPM, una armonía por compás.", "Compara Em7 con E7; oye G# que resuelve a A y D que baja a C en Am.", "Añade D7 en el compás 5; oye F# que resuelve a G y C que baja a B en G.", "Compara la preparación E7 sola con D7 sola; esta versión conserva D7 y restaura Em7."][index - 1],
        "changeFromPrevious": "Presentación de la base." if index == 1 else delta,
        "successCriteria": ["El bajo sostiene una fundamental por compás a velocidad 60.", "La derecha toca el voicing indicado a velocidad 64.", "Identifico el destino armónico y la resolución de las notas alteradas.", "G# y F# son cromáticas respecto a do mayor; son dominantes secundarias locales, no modulación estable."] if index == 1 else ["Solo cambia la tercera indicada; ataques, duración, velocidad y demás notas permanecen iguales.", "Oigo la resolución al acorde de destino en el compás siguiente."],
        "simplifyHint": "Practica primero solo el bajo y luego las dos manos.", "extendHint": "Canta las notas alteradas y sus resoluciones mientras mantienes el pulso."})
    progressions.append({"id": progression_id, "stageId": stage_id, "kind": "primary", "order": 1,
        "title": variant["title"], "keyTonic": "C", "keyMode": "major", "style": "jazz", "bpm": 72,
        "timeSignature": {"numerator": 4, "denominator": 4}, "totalBars": 8,
        "description": "Ocho compases, 32 negras; una armonía por compás. Voicings deliberadamente reducidos.", "loopable": True})

    for bar_index, (symbol, function, bass, right) in enumerate(bars):
        if bar_index == 1 and variant["e7"]:
            symbol, function, right = "E7", "V/vi", [68, 74]
        if bar_index == 4 and variant["d7"]:
            symbol, function, right = "D7", "V/V", [66, 72]
        if bar_index == 2 and variant["e7"]:
            right = [69, 72]
        if bar_index == 5 and variant["d7"]:
            right = [67, 71]
        start = bar_index * 4
        chord_events.append({"id": f"chord-harmony-013-{suffix}-{bar_index + 1:02}", "progressionId": progression_id,
            "order": bar_index + 1, "symbol": symbol, "function": function, "startBeat": start, "durationBeats": 4})
        note_events.append({"id": f"note-harmony-013-{suffix}-{bar_index + 1:02}-bass", "progressionId": progression_id,
            "midi": bass, "startBeat": start, "durationBeats": 4, "velocity": 60, "role": "bass", "hand": "left"})
        for voice, pitch in enumerate(right, 1):
            note_events.append({"id": f"note-harmony-013-{suffix}-{bar_index + 1:02}-right-{voice}", "progressionId": progression_id,
                "midi": pitch, "startBeat": start, "durationBeats": 4, "velocity": 64, "role": "harmony", "hand": "right"})

for name, rows in (("stages", stages), ("progressions", progressions), ("chord-events", chord_events), ("note-events", note_events)):
    (root / f"{name}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")

source = root.parent / "pending-012" / "checks"
for name in ("categories", "skills", "lessons"):
    rows = json.loads((source / f"{name}.json").read_text())
    if name == "lessons":
        rows = [row for row in rows if row["id"] != lesson["id"]] + [lesson]
    (checks / f"{name}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")
for name, rows in (("stages", stages), ("progressions", progressions), ("chord-events", chord_events), ("note-events", note_events)):
    all_rows = json.loads((source / f"{name}.json").read_text())
    ids = {row["id"] for row in rows}
    all_rows = [row for row in all_rows if row["id"] not in ids and row.get("lessonId") != lesson["id"]]
    if name == "progressions":
        all_rows = [row for row in all_rows if row["stageId"] not in {stage["id"] for stage in stages}]
    if name in ("chord-events", "note-events"):
        all_rows = [row for row in all_rows if row["progressionId"] not in {progression["id"] for progression in progressions}]
    (checks / f"{name}.json").write_text(json.dumps(all_rows + rows, ensure_ascii=False, indent=2) + "\n")

# Independent MIDI writer: format 0, one track, PPQ 960.
def vlq(value):
    out = [value & 127]
    value >>= 7
    while value:
        out.insert(0, (value & 127) | 128)
        value >>= 7
    return bytes(out)

for progression in progressions:
    pid = progression["id"]
    events = [(0, bytes([255, 81, 3, 0x0C, 0xB7, 0x35])), (0, bytes([255, 88, 4, 4, 2, 24, 8]))]
    for note in (row for row in note_events if row["progressionId"] == pid):
        on = note["startBeat"] * 960
        off = (note["startBeat"] + note["durationBeats"]) * 960
        events.extend([(on, bytes([144, note["midi"], note["velocity"]])), (off, bytes([128, note["midi"], 0]))])
    events.append((32 * 960, bytes([255, 47, 0])))
    track, previous = bytearray(), 0
    for tick, message in sorted(events, key=lambda event: (event[0], event[1][0] == 144)):
        track.extend(vlq(tick - previous) + message)
        previous = tick
    payload = b"MThd" + struct.pack(">IHHH", 6, 0, 1, 960) + b"MTrk" + struct.pack(">I", len(track)) + track
    (root / f"{pid}.mid").write_bytes(payload)
