approved

# Armonía, lote 03 — revisión del maestro

Se inspeccionaron las 12 etapas, 51 acordes y 209 notas nuevas completas. Se corrigieron realizaciones que pasaban validación técnica pero no cumplían la armonía o su explicación.

|Lección|Cuatro etapas y evidencia|
|---|---|
|007|Distribución regular; prolongación de I; IV2/V6; elección IV6/V2. Todo suma32negras y conserva I inicial16enB, tempo72 y voicings.|
|008|Em conGnatural; E7 conG#/D; sensible superior G#4→A4; elección Em/E7. Am existe en las cuatro realizaciones y C sigue como centro.|
|009|I–ii directo; disminuido2; otra conducción de tres semitonos; elección de paso1/2. BajoC3–C#3–D3 real ydimC#/E/G/Bb completo.|

Se cotejaron las notas por acorde, los destinos y deltas. Dos manos, alcance máximo9semitonos/4notas RH, sin tecla duplicada sostenida. Batch válido, métricas0 y12MIDI coincidentes.001–006 siguen con huellas intactas. Sin escucha ni prueba física.

```json
[
  {
    "issueId": "H-B03-001",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-harmony-008",
    "location": "Am real, sensible y contraste A/B",
    "expected": "C–Em/E7–Am–G, G#→A audible y solo las variaciones anunciadas.",
    "observed": "Am estaba realizado comoCenlas4etapas, sinbajoA ni destinoA; E7cambiaba registros noanunciados.",
    "correction": "Am tieneA2yA/C/E real; EmG3/B3/E4 cambia aE7G#3/B3/D4/E4, con sensibleA3.03solo subeG#yAunaoctava;004vuelveAbase explícita.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "H-B03-002",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-harmony-009",
    "location": "Bajo cromático y resolución de disminuido",
    "expected": "C3–C#3–D3 y resoluciones en el registro que suena.",
    "observed": "El bajo pasabaC3/C#3aD2poroctava;003prometíaF5/A5ausentes tras subir disminuido unaoctava.",
    "correction": "Bajo48/49/50;002dim61/64/67/70resuelveaDm62/65/69;003dim64/67/70/73resuelveDm65/69/74, tres semitonos reales yG4omitido sin duplicar teclas.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "H-B03-003",
    "severity": "minor",
    "entityType": "lesson",
    "entityId": "lesson-harmony-007",
    "location": "Primaria ritmo armónico, elección en respuesta",
    "expected": "Cuatro compases de prolongación y otros cuatro de respuesta; variar duraciones, no inversiones nuevas.",
    "observed": "003introducíaG/Dajenoalobjetivo;004acortabapro longació n3compases sin decirlo ycriterios genéricos.",
    "correction": "007usa8+8+8+8,16+4+4+8,16+2+6+8,16+6+2+8. Primeros4compasesprolongadosseconservanenB yautonomía; no cambian bajos/voicings niBPM.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "H-B03-004",
    "severity": "minor",
    "entityType": "lesson",
    "entityId": "lesson-harmony-009",
    "location": "Aplicación libre y criterios",
    "expected": "Decidir duración breve del paso con un destino claro.",
    "observed": "La referencia final solo quitaba el paso y los12criterios eran genéricos, no comprobaban recursos propios.",
    "correction": "004resetea voicing002yusaC4–dim1–Dm3–G7(4)–C(4), permite1/2negras ajustandoDm. Cadaetapa tiene criterio temporal/armónico específico.",
    "owner": "master",
    "status": "resolved"
  }
]
```
