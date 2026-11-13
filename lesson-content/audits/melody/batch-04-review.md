approved

# Melodía, lote04 — maestro

Revisadas13etapas,104acordes y391notas nuevas completas, ocho compases por progresión.

|Lección|Etapas y resultado|
|---|---|
|010(4)|Repetición;contorno de respuesta;últimanotaC4;rasgo de pregunta conservado. Pregunta yritmo intactos.|
|011(4)|Objetivos3/7; conexiónD–C; conexiónG–A–B;elección previa deguíaFmaj7E4. LH3notascompactas, sinwalking ni tercerahand.|
|012(5)|Ideas inconexas;motivoEGA;variaciónrítmica;adaptaciónB4sobreG;retornooriginalelegido. No se rellena con escalas.|

Se cotejaron todas las notas y los deltas heredados. Manoizquierda máximo11semitonos/3notas; derecha monofónica. Batchválido,métricas0y13MIDI completos coincidentes, fin30720ticks.001–009 intactas. Sin escucha ni ejecución física.

```json
[
  {
    "issueId": "M-B04-001",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-melody-010",
    "location": "Alturas de pregunta/respuesta en02..04",
    "expected": "Pregunta inmutable y respuesta transformada solo como se describe.",
    "observed": "Mutaciones afectaban la pregunta, no cambiaban el contorno completo de la respuesta y el cierreC4noaparecíaen03.",
    "correction": "Las4preguntas sonexactamenteE/G/A/G/E/D/G/D. Respuesta02invertida,03soloúltimaC4,04solo recuperaprimera parejaE/G. Assertions cotejan cadaaltura/entrada/duración.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "M-B04-002",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-melody-012",
    "location": "Ritmo heredado04/05 y retorno",
    "expected": "Conservar variaciónrítmica al adaptar una altura; señal de regreso audible.",
    "observed": "004restauraba indebidamente todo ritmo básico y005era idéntica04; criterios eran genéricos.",
    "correction": "004conserva ritmo de03ymueveA4→B4soloG;005recupera ritmooriginalsoloúltimobar. Texto/task/criterio explícitosporpaso yarmoníaparcialconcolores diatónicos.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "M-B04-003",
    "severity": "minor",
    "entityType": "lesson",
    "entityId": "lesson-melody-011",
    "location": "Conexión yhint base",
    "expected": "Conexión G–A–B como dos tonos sucesivos, sin presumir notas futuras.",
    "observed": "Texto podía leerse como G→B deuntono yhint001hablabaconexiones aún ausentes.",
    "correction": "Se precisa secuencia G4–A4–B4; hint practica objetivos/conexiones realmente presentes. Se aclaran offsets0/1vs tiemposmusicales1/2enM010.",
    "owner": "master",
    "status": "resolved"
  }
]
```
