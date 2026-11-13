approved

# Expresión, lote 05 — revisión del maestro

14 etapas y MIDI, 112 acordes y 485 notas. Se revisaron todas las duraciones, ataques, alturas, silencios y perfiles de velocity, no solo la validación estructural. 013 conserva swing 2:1 y separa silencio melódico de acompañamiento sostenido. 014 distingue tensión de cuarta sobre G7, resolución a su tercera y posterior tónica; una cumbre principal de intensidad, sin añadir densidad. 015 cumple forma 1+3+3+1, entrada izquierda sola y final conjunto silencioso.

Batch válido, métricas sin findings, diferencias completas comprobadas mediante aserciones y 14 MIDI binarios coincidentes. Huellas anteriores intactas. 4/4 en 015 es coherente con la ficha y especificación: no se ha aceptado la explicación del productor sobre un supuesto requisito 6/8. Sin escucha ni ejecución física.

```json
[
  {
    "issueId": "E-B05-001",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-expression-013",
    "location": "Cronología, duración y descripción",
    "expected": "Una transformación rastreable por fase, pausas y resolución reales.",
    "observed": "La primera reducción no retiraba notas; sus instrucciones nombraban 15 y 15⅔ en vez de los ataques existentes 14 y 14⅔. También 03 nombraba 27 en vez de 26.",
    "correction": "02 retira exactamente 14/14⅔, 03 retira 26/26⅔ tras reiniciar 01. Pausas 13–16 y 25–28 reales; 04 permite elegir una llegada y su reducción, sin acumularlas.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "E-B05-002",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-expression-014",
    "location": "Cronología, duración y descripción",
    "expected": "Una transformación rastreable por fase, pausas y resolución reales.",
    "observed": "04 restauraba duraciones anteriores en lugar de conservar 03; 05 restauraba la izquierda a 55. Se decía que 1→1.5 era acortar y que C5 atravesaba un cambio armónico inexistente.",
    "correction": "Conservadas las duraciones 1.5/2.5 y ataque B4@25.5 en 04/05, con LH45 en segunda frase. Se explica apoyatura reatacada dentro de G7, no retardo preparado ni ligadura a través del cambio.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "E-B05-003",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-expression-015",
    "location": "Cronología, duración y descripción",
    "expected": "Una transformación rastreable por fase, pausas y resolución reales.",
    "observed": "Texto reclamaba subdivisión ternaria sin eventos ternarios; fases describían transformaciones ajenas. 04 reintroducía F4@14 y 05 sostenía C5 hasta32 negando el silencio final.",
    "correction": "Se conserva 4/4, sin fingir 6/8. 02 perfil dinámico, 03 omisión14, 04 cierre de dos negras y 05 suavizado final, cada delta cotejado. F4@14 ausente en 03–05, ambas manos callan30–32 en04/05.",
    "owner": "master",
    "status": "resolved"
  }
]
```
