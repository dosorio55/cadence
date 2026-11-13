approved

# Independencia, lote02 — revisión del maestro

Inspeccionadas15etapas,60acordes y299notas nuevas, completos por grupos de ataque/duración/mano/rol/velocity. Sin subagentes revisores.

|Lección|Cinco etapas y contraste|
|---|---|
|004|Raíces repetidas; tercera en2; quinta en3; aproximación diatónica en4; vecino superior elegido. RH tercera/séptima permanece cuatro pulsos. VuelveE2→D2, sin cromatismo.|
|005|RH coincide con blancas; segunda respuesta pasa de3 a4; primera nota dura2; se invierten alturas; se omite una respuesta. LH raíz/quinta idéntica en todas.|
|006|Ataque conjunto breve; entrada2&; sostén dosnegras; otra nota acordal; elección1& frente2&. LH16negras intactas, sin imitación.|

Shells004: F4/C5 sobreDm7, B3/F4 sobreG7,E4/B4 sobreCmaj7. Las melodías005/006 usan notas de Cmaj7/Am7/Fmaj7/G7 y solo dos manos. Correcciones anteriores completadas por maestro. Validación batch, métricas sin hallazgos y15MIDI completos coincidentes; huella001–003 intacta. Sin escucha ni prueba física.

```json
[
  {
    "issueId": "I-B02-001",
    "severity": "major",
    "entityType": "stage",
    "entityId": "stage-independence-006-03",
    "location": "Duración RH en006-03..05",
    "expected": "RH debe sostenerse durante los ataques izquierdos en tiempos3 y4.",
    "observed": "La nota terminaba en offset3: se liberaba al comenzar tiempo4, pese al criterio de sostener durante ambos ataques.",
    "correction": "Duración2 desde1.5 hasta3.5(4&), criterio y explicación ajustados; LH sin cambios.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "I-B02-002",
    "severity": "major",
    "entityType": "stage",
    "entityId": "stage-independence-006-05",
    "location": "Aplicación autónoma frente aintro/goal",
    "expected": "Elegir un segundo contratiempo, no solo omitir un compás.",
    "observed": "La referencia final solo omitía RH en compás2, sin ilustrar otro contratiempo.",
    "correction": "Se conserva todo004 y se mueve solo entrada del compás1 de2& a1&. Ambas opciones duran2 y caben en el compás; se restituye respuesta del compás2.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "I-B02-003",
    "severity": "minor",
    "entityType": "lesson",
    "entityId": "lesson-independence-004",
    "location": "004-03..05,quinta del último compás ydirección en005",
    "expected": "Aproximación diatónica cómoda al volver aD2 y descripción verdadera.",
    "observed": "G3→E2 era un salto de15semitonos;005 decía ascender desde notas que descienden a sus destinos.",
    "correction": "Quinta finalG2 en03..05 paraevitar salto mayor deoctava;005 dice descender. Raíz/tercera/quinta y aproximaciones siguen diatónicas.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "I-B02-004",
    "severity": "minor",
    "entityType": "lesson",
    "entityId": "lesson-independence-005",
    "location": "Hints de004/005/006 ytask005-01",
    "expected": "Simplificar sin eliminar el recurso actual ni anticipar falsamente una etapa.",
    "observed": "Hints uniformes borraban terceras/quintas o respuestas desplazadas;006-01 proponía2& aún no presente;005-01 prohibía coincidencia aunquebasecoincide.",
    "correction": "Hints ahora preservan patrón, sostén y entradas del nivel; práctica parcial se reintegra en ciclo completo. Base005-01 reconoce coincidencia A;04-01/02/03 extensions presentan transformaciones como nuevas, no ya existentes.",
    "owner": "master",
    "status": "resolved"
  }
]
```
