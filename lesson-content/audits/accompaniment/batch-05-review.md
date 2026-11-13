approved

# Acompañamiento, lote 05 — revisión del maestro

15 etapas, 16 progresiones/MIDI, 128 acordes y 843 notas. 013 conserva la voz superior integrada, sin tercera mano: cada arpegio abarca como máximo nueve semitonos, despeje sin borrar llegadas y cima larga donde se indica. 014 separa registro de densidad y conserva velocities MIDI, sin afirmar igualdad acústica. 015 usa reducción de bossa de dos compases, bajo raíz–quinta fijo y guía alternativa solo melódica. Los shells conservan tercera y séptima; el único G9 añade A3 como novena.

Validación batch aprobada; métricas sin findings y los16MIDI cotejados íntegros. Aviso de registro: B2 (MIDI47) aparece15veces en la derecha de015/03–05; es intencional, está encima del bajo G2/D2, cabe en la mano y deja libre la guía. No hay colisión de teclas ni cruce real entre manos. Huellas previas intactas. Sin escucha ni ejecución física.

```json
[
  {
    "issueId": "A-B05-001",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-accompaniment-013",
    "location": "Voz superior, registro y delta musical",
    "expected": "Preservar líneas, bajo y transformaciones expresamente anunciadas.",
    "observed": "Las reducciones retiraban offsets1/1.5 en lugar de2/2.5 y borraban la voz superior que debían conservar; el consejo de03 silenciaba el pulso que contiene la cima.",
    "correction": "Reconstruidas02–05 desde01: todas las16llegadas superiores intactas; omisiones2/2.5/3.5 y duración1en3 según fase. Autonomía mueve despeje7→6 restaurando7.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "A-B05-002",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-accompaniment-014",
    "location": "Voz superior, registro y delta musical",
    "expected": "Preservar líneas, bajo y transformaciones expresamente anunciadas.",
    "observed": "03 ya bajaba el último shell, anulando el cambio04;05 no recuperaba G7en7. La entrega inicial también tenía duración4.01.",
    "correction": "Duraciones4.0 exactas.03 mantiene shells altos hasta8;04 baja solo8 y05 baja también7. Se conservan densidad, velocities y bajo entre los cambios de registro.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "A-B05-003",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-accompaniment-015",
    "location": "Voz superior, registro y delta musical",
    "expected": "Preservar líneas, bajo y transformaciones expresamente anunciadas.",
    "observed": "02 se describía como bloques completos aunque eran guías; los criterios exigían registro bajo antes de introducirlo.05 restauraba las pausas y seguía etiquetando G7 el acorde coloreado.",
    "correction": "Texto por fase, registro corregido desde03.05 conserva exactamente04 y añade A3en24/25.5/27, con símboloG9solo24–28. Guía alternativa aislada y no simultánea.",
    "owner": "master",
    "status": "resolved"
  }
]
```
