approved

# Independencia, lote04 — maestro

Revisadas14etapas,96acordes y521notas nuevas, cuatro compases en010 y ocho en011/012. Se cotejaron todos los eventos base y cada transformación descrita.

|Lección|Etapas|
|---|---|
|010(4)|Resolución inmediata;ligadura sobrefrontera8;resolución9.5;elección9.25. LHraíz/quinta intacta, no cruce físico.|
|011(5)|Fraserepetida;respuesta desplazada;omisión23;sosténF4;eleccióndeotraomisión19. LH32negras sinwalking ni imitación.|
|012(5)|LHparcial16blancas;añadebossa2compases;RHbreve;omisión14.5;otraomisión6.5. Shells3/7correctos ymapafijo.|

Las manos son independientes sin tercera parte ni tecla sostenida compartida. Rango y ritmo cómodos; batchválido,métricas0 y14MIDI completos coincidentes.001–009intactas. Sin escucha ni ejecución física.

```json
[
  {
    "issueId": "I-B04-001",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-independence-011",
    "location": "Deltas y notas de respuesta",
    "expected": "Primera frase idéntica, omisión de respuesta correcta y sostén real mientras LHsigue.",
    "observed": "002movía ataques también de primera frase;003quitaba primera nota20envezrespuesta23;004alargabaG4@23noprometidoD4;roleLHrootinválido.",
    "correction": "Se conserva frasebase literal, solo segundosataques2dafrase2→3;omisión23;04sostieneF4@24de1a2;005mueveomisión23→19. LH32raícesrolemarcadobassidénticas.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "I-B04-002",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-independence-010",
    "location": "Referencia importable, notas y semántica armónica",
    "expected": "Cuatro etapas con ligadura y llegada enCmaj7 sin esperar elbajo.",
    "observed": "Archivos quedaron enchecksnointegrables/metadatafaltante;notassolo45vs48delplan;B4se llamabaséptimadelacorde deorigenG7y004citabaAm7cuando llegabaaCmaj7.",
    "correction": "Ficha recuperadaexactadecanónica yrealización48notas.01B6–8/C8–10;02B6–9/C9–10;03B6–9.5/C9.5–10;04B6–9.25/C9.25–10. B es3deG7 y7deCmaj7, C5raízdelallegada;LH8blancasconstantes.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "I-B04-003",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-independence-012-05",
    "location": "Referencia de omisión y autonomía",
    "expected": "Comparar004/005 y escoger otra única omisión sin acumularlas.",
    "observed": "Se decíaRespecto03moveromisiónaunque03nola tenía;taskfinalnollegabaaproponerdecisiónlibre.",
    "correction": "Se compara04, restaura14.5yomite6.5;después se vuelve alcompleto03para elegirunúnicohueco.004hintidentifica compás4delaprimera vuelta,noúltimode8.",
    "owner": "master",
    "status": "resolved"
  }
]
```
