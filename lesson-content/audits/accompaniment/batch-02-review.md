approved

# Acompañamiento, lote 02 — revisión del maestro

## Revisión inicial histórica — rechazada

Inspeccionadas las 15 etapas y sus realizaciones: 80 acordes y 357 notas nuevas. El lote no realiza varias transformaciones anunciadas y no está aprobado. La comprobación automática encuentra seis pares consecutivos idénticos. Corrección concreta enviada al compositor; 001–003 permanecen fuera del alcance. Sin escucha ni prueba física.

```json
[
  {
    "issueId": "A-B02-001",
    "severity": "major",
    "entityType": "stage",
    "entityId": "stage-accompaniment-004-02",
    "location": "004-01..05: voces RH y deltas",
    "expected": "Aislar octava, densidad de dos/tres voces y armonía C/G/Am/F.",
    "observed": "G en 02/03 contiene F en lugar de B; 02 y 03 son idénticas aunque 03 promete añadir una voz; el movimiento 01->02 no es solo octava.",
    "correction": "Realizar díadas base, subirlas exactamente una octava en02, añadir quintas en03, retirarlas en04 y elegir densidad en05; G conserva B. Tareas y criterios específicos. Maestro completó la corrección y verificó el plan completo con assert_004_006.py, métricas sin hallazgos y los 30 MIDI de ambos lotes.",
    "owner": "composer-accompaniment",
    "status": "resolved"
  },
  {
    "issueId": "A-B02-002",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-accompaniment-005",
    "location": "005-01..05: frase, comping, shells y huecos",
    "expected": "Guía audible y shells tercera/séptima solamente en silencios RH reales, con transformaciones rastreables.",
    "observed": "Texto promete shells en0/2 o3; eventos los sitúan3.75 y usan raíz/tercera sin séptima; 03 elimina todos los shells y04/05 son idénticas.",
    "correction": "Guía de dos negras por compás, pausa RH[2,4); shells F3/C4, F3/B3, E3/B3 en2/3; etapas retiran/desplazan/alternan ataques tal como se instruyó al compositor. Maestro completó la corrección y verificó el plan completo con assert_004_006.py, métricas sin hallazgos y los 30 MIDI de ambos lotes.",
    "owner": "composer-accompaniment",
    "status": "resolved"
  },
  {
    "issueId": "A-B02-003",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-accompaniment-006",
    "location": "006-01..05: alturas absolutas y voz superior",
    "expected": "Inversiones RH y rutas superiores diferentes, por pasos/unísonos, durante ocho compases.",
    "observed": "Las cinco realizaciones son idénticas; cimas reales no coinciden con las nombradas y no se realizan las inversiones anunciadas.",
    "correction": "Serializar voicings absolutos del plan del maestro: base, G invertido, ruta G/G/A/A, alternativa E/D/E/F y aplicación E/D/C/C/C/D/E/F. Bajo raíz constante; nombrar inversiones del bloque RH, no del acorde global. Maestro completó la corrección y verificó el plan completo con assert_004_006.py, métricas sin hallazgos y los 30 MIDI de ambos lotes.",
    "owner": "composer-accompaniment",
    "status": "resolved"
  },
  {
    "issueId": "A-B02-004",
    "severity": "blocker",
    "entityType": "partition",
    "entityId": "accompaniment",
    "location": "compose_004_006.py: escritura final de los cinco arrays",
    "expected": "Preservar exactamente los registros aprobados 001–003 al añadir004–006.",
    "observed": "El regenerador sustituyó los cinco arrays con el lote nuevo y eliminó los registros aprobados, también del snapshot checks. No se modificó el registro de aprobación.",
    "correction": "Maestro recuperó las tres tablas de metadatos desde toolResults completos persistidos y reprodujo los generadores/correcciones históricos en un directorio temporal para recuperar acordes y notas. La reconstrucción coincidió exactamente con SHA-256 cdc5978227507c7c132c1f12822534e092bcb1c532cc5a653a63efa894b6c127 (3 lecciones,15 etapas,15 progresiones,60 acordes,228 notas). Se restauró sin alterar su aprobación, se conservó004–006 y se respaldaron ambas partes. El regenerador ahora preserva IDs no reemplazados; dos ejecuciones producen archivos idénticos y mantienen las huellas de todos los aprobados.",
    "owner": "master",
    "status": "resolved"
  }
]
```

## Cierre del maestro — aprobado

El maestro corrigió el plan tras la devolución incompleta: 004 tiene díadas, traslado exacto de octava, quinta añadida/retirada y densidad autónoma;005 tiene guía RH de dos negras y pausa[2,4), shells 3/7 LH en2/3, retirada de2, desplazamiento3→2 y elección3/2/3/2;006 realiza las cinco rutas especificadas con alturas absolutas, cimas por pasos/unísonos en las últimas tres y bajos constantes. Se ajustaron tareas, criterios y deltas, incluido el error C5/G4 y los consejos de cuatro/ocho compases.

Las 15 etapas nuevas contienen80 acordes y326 notas. Se comprobaron todas las alturas, ataques y duraciones por compás con assertions y lectura de los30 MIDI de ambos lotes. Métricas sin hallazgos; validación batch correcta. La partición aprobada anterior fue recuperada y contrastada con su huella original, sin sustituirla. Sin escucha ni ejecución física.
