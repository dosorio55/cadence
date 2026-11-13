approved

# Melodía,lote03 — maestro

Revisión de las12etapas,48acordes y155notas completas mediante agrupación temporal.

|Lección|Cuatro etapas verificadas|
|---|---|
|007|MotivoE/G/A/G/E/D repetido;G retrasado yA alargado;huecosantesD;últimoD adelantado conautonomía deotro ritmo. Alturas ybajo se conservan.|
|008|ApoyosE/A/F/G largos;bordadura inferior;superior diatónica;mezcla elegida. Todas retornan al apoyo original.|
|009|ObjetivosF/B/E/E eniiVI;A→B tono;A#→B semitono;reset yúnicaD#→E escogidaen8. BajoD/G/C/C largo.|

Textura de bajo ymelodía, armonía parcial explícita, sin acordes completos fingidos. Dos manos monofónicas, notas sin solapamientos. Validación batch, métricas sin hallazgos y12MIDI coincidentes. Aprobados001–006 intactos. Sin escucha ni prueba física.

```json
[
  {
    "issueId": "M-B03-001",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-melody-009",
    "location": "Progresión, notas objetivo y contraste diatónico/cromático",
    "expected": "ii–V–I–I y aproximación cromática débil a una guía; autonomía de una sola llegada.",
    "observed": "El borrador usabaCAmFG en vez deiiVI, llamaba cromáticoB–Cdiatónico y terminaba añadiendo cuatro aproximaciones sin elección autónoma.",
    "correction": "Recompuesta009conDm7/G7/Cmaj7/Cmaj7yobjetivosF/B/E/E.02A3→B3diatónica,03A#3→B3cromática,04resetea01yeligeúnicaD#4→E4en8. Assertions cubren todos los pitches/onsets/duraciones; texto cuenta3.5como4& yno llamaD#diatónico.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "M-B03-002",
    "severity": "major",
    "entityType": "stage",
    "entityId": "stage-melody-008-03",
    "location": "Vecina superior deE4",
    "expected": "Vecina diatónicaF4 yretornoE4–F4–E4.",
    "observed": "El MIDI usabaF#4 y el texto F–E–F, dirección y punto de apoyo incorrectos.",
    "correction": "F#4→F4; explicación yhintE–F–E/A–B–A/F–G–F/G–A–G. Todas las notas008 pertenecen a do mayor, siempre retorno al mismo apoyo.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "M-B03-003",
    "severity": "minor",
    "entityType": "lesson",
    "entityId": "lesson-melody-007",
    "location": "Deltas temporales/hints007-02..04 y008-01/02",
    "expected": "Instrucciones fieles a las pausas, orden y alturas completas.",
    "observed": "007-02 decía adelantarG aunque pasa1→1.5;hintA@2–G@1.5retrocedía;03describía mal pausaantesD y04permitía eliminar alturas.",
    "correction": "Textos indicanG retrasado, A prolongado, nuevos huecosantesD yúltimoDadelantadoen14; hints conservan contorno completo.008-01sostiene2/descansa2 y008-02practica figura completa de tres notas.",
    "owner": "master",
    "status": "resolved"
  }
]
```
