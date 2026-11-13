approved

# Melodía, lote 05 — revisión del maestro

14 etapas y MIDI, 96 acordes y 360 notas. Revisados todos los eventos y textos de 013–015: ornamentación selectiva con cima B4, cerco diatónico/cromático y respuesta propia sobre pregunta fija. Raíces/bloques izquierdos invariantes y ninguna tecla duplicada sostenida entre manos. Los shells conservan tercera y séptima; las líneas sobre raíces se describen como armonía parcial.

Validación batch y cotejo binario completo de los 14 MIDI aprobados. Huellas anteriores intactas. La coincidencia de 013/02 y 013/05 es deliberada: esta última vuelve desde 03 a retirar solo el paso, y compara esa elección con retirar la bordadura en 04. No se presenta como un ejemplo musical nuevo por transposición. Sin escucha ni ejecución física.

```json
[
  {
    "issueId": "M-B05-001",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-melody-013",
    "location": "Etapas, eventos y criterios",
    "expected": "Texto, armonía, objetivos y diferencias coinciden; autonomía explícita.",
    "observed": "La etapa 03 situaba F–E–D en G7 aunque sus eventos 8–10 pertenecen a Fmaj7; la autonomía imponía una retirada única.",
    "correction": "Corregida la armonía del gesto y ofrecida elección real entre retirar paso o bordadura, conservando la cima B4@24/88.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "M-B05-002",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-melody-014",
    "location": "Etapas, eventos y criterios",
    "expected": "Texto, armonía, objetivos y diferencias coinciden; autonomía explícita.",
    "observed": "El F4 del cerco estaba en 6.5 frente al 7 anunciado; el silencio [1,7.5) ignoraba B4@4. La explicación prohibía B3 con una razón incorrecta.",
    "correction": "F4 colocado en 7; pausas [1,4) y [5,7.5). Se explica que sería C4 del cerco inferior, no B3, la tecla ocupada. Criterio de autonomía distingue referencia y elección.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "M-B05-003",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-melody-015",
    "location": "Etapas, eventos y criterios",
    "expected": "Texto, armonía, objetivos y diferencias coinciden; autonomía explícita.",
    "observed": "La etapa 04 borraba también la aproximación que decía conservar; 05 llamaba C5@24 tercera de Am7 cuando G7 empieza en 24 y la nota estaba en 25.",
    "correction": "Restituido A#4@23.5 en 04. Autonomía reinicia 02 y cambia solo G4@16 a C5@16, tercera de Am7; se conserva F4@25→E4@28 y final C5@29.",
    "owner": "master",
    "status": "resolved"
  }
]
```
