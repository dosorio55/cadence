approved

# Expresión, lote04 — maestro

Revisadas14etapas,96acordes y347notas nuevas. Inspección completa de las texturas base y verificación de cada diferencia; no se usaron checks antiguos de los compositores como prueba de esta entrega.

|Lección|Etapas|
|---|---|
|010(5)|Retorno enG7;cadenciaG7/C;silenciofinal2;retornoRHcorto/LHlargo;elección cierre1o retorno. Prefijoseiscompases idéntico.|
|011(5)|Dinámicaplana;contraste62/76;cumbre24;LHsegundoplano45;cumbreelegida20. Solo cambiavelocity, melodía16notas yLH8díadas constantes.|
|012(4)|Articulaciónuniforme;LHbreve;RHligada;elección1.75/2. Ambasmanosmonofónicas, sin pedal obligatorio.|

Las cifras de duración, señales formales y planos corresponden a eventos reales. Dos manos cómodas, sin teclas sostenidas solapadas. Batchválido,métricas0 y14MIDI completos coincidentes;001–009 intactas. Sin escucha ni ejecución física.

```json
[
  {
    "issueId": "E-B04-001",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-expression-010",
    "location": "Cadencia final y descripción",
    "expected": "Símbolos y notas de la tónica coinciden; dos últimos compases G7–I con silencios reales.",
    "observed": "005rotulabaCmaj7perosonabaCtriada;002describíaDm7en7/G7Cen8aunqueMIDIeraG7/I.",
    "correction": "Los finalesB02/03/05realizantriadaCconfunciónI, y se corrigen textos/mapas. Silencios30–32/29–32 yprefijoseiscompases verificados; A01/04siguenVretorno.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "E-B04-002",
    "severity": "minor",
    "entityType": "lesson",
    "entityId": "lesson-expression-011",
    "location": "LH yubicación de cumbre",
    "expected": "Describir ataques del acompañamiento y único pico real.",
    "observed": "La descripción decíaLH0/2aunqueeraunadíadaen0;003llamabapicobeat20/compás6 al máximo88queestabaen24/compás7.",
    "correction": "Se conserva la textura escasa válida yse describeunLHbloqueporcompás;003pico24,005pico20. Las cinco etapas solo cambianvelocity.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "E-B04-003",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-expression-012",
    "location": "Role/delta y autonomía",
    "expected": "Role válido y articulaciones independientes con elección de conexión.",
    "observed": "LHroleaccompanimentfueraenum;002decíacambiarRHaunqueacortabaLH;004noofrecíaelecciónexplícita.",
    "correction": "LHroleharmony;sondosnotasalternadasporacorde,no díada.01.5/.5,02.25/.5,03.25/2,04eligeRH1.75/2conLH.25. Mismasnotas/entradas/vel;legatosinpedal.",
    "owner": "master",
    "status": "resolved"
  }
]
```
