approved

# Ritmo, lote 05 — revisión del maestro

10 etapas y MIDI, 80 acordes y 371 notas. 014 reutiliza exactamente el guajeo013/02 y altera una sola llegada aF: frontera armónica y bajo se adelantan media negra; F4 sustituye el ataque débil y cruza el uno sin reataque. Orientación2–3 y duración de32negras intactas; la única ampliación posterior es0.75→1.5 y la autonomía mueve su ubicación. 015 usa parejas2:1 explícitas, respuesta desplazada, una omisión sobreAm7 y llegada larga no swingada; bajo de16blancas constante y primera frase idéntica.

Todas las notas se compararon con transformaciones esperadas independientes del generador. Validación batch, métricas sin findings y cotejo binario de10MIDI aprobados. Huellas anteriores intactas. Sin escucha ni ejecución física.

```json
[
  {
    "issueId": "R-B05-001",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-rhythm-014",
    "location": "Frontera, onset y autonomía",
    "expected": "Texto fiel a ataques, función y decisiones rítmicas.",
    "observed": "La tarea y el consejo genéricos hablaban de un uno anticipado incluso en la referencia sin anticipación; la autonomía no pedía elegir frontera.",
    "correction": "Tareas y criterios específicos por fase. Referencia intacta de013/02; una sola anticipación conjunta, sostenida sin reataque. Autonomía elige frontera4o20, con duración1.5 y la otra restaurada.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "R-B05-002",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-rhythm-015",
    "location": "Frontera, onset y autonomía",
    "expected": "Texto fiel a ataques, función y decisiones rítmicas.",
    "observed": "La instrucción heredada situaba Am7 y su silencio en21/21⅔ aunque Am7ocupa16–20; también decía F4@26, que es B4. La frase inicial no repetía alturas ni acordes, solo ritmo.",
    "correction": "Textos corregidos: C5@17, omisiónG4@17⅔, Dm7@21/21⅔ intacto; B4@26/F4@26⅔ y E4@29. Tareas y autonomía distinguen referencia de elección, sin modificar notas correctas.",
    "owner": "master",
    "status": "resolved"
  }
]
```
