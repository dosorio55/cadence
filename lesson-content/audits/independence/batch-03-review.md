approved

# Independencia,lote03 — maestro

Revisadas15etapas,45acordes y353notas nuevas completos con todas las manos y notas sostenidas.

|Lección|Cinco etapas verificadas|
|---|---|
|007|LHparcial.5;añadeRHbolero1/1.5/3;LH2;RH.25;únicaomisión5.5 con elección. Shells3/7 reales.|
|008|OstinatoLH0/.5/2/2.5;RHacoplada0;desplazada1.5;sostenidahasta2.5;Bb4séptimaC7;pausaúnicaelegida.|
|009|Walking004-04exacto conRH0/dur1/3;onset2/3;dur2/3cruzasiguientenegr a;inversiónsoloii;elección2/3o5/3porbar.|

Se leyó cada etapa/progresión/chord y grupo temporal de notas. Los procesos y deltas concuerdan, hay dos manos, sin extensión superior a octava ni tecla compartida sostenida.001–006intactas, batchválido,métricas0 y15MIDI completos coincidentes; cloning walking cotejado evento por evento. Sin escucha ni interpretación física.

```json
[
  {
    "issueId": "I-B03-001",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-independence-009",
    "location": "RH alcance/solapamientos",
    "expected": "Shells terceras/séptimas cómodos y walking izquierdo separado.",
    "observed": "El borrador alcanzaba31semitonos RH y solapabaMIDI47 entrepartes.",
    "correction": "Recompuesta009conLHclonadoexacto004-04 filtradohandleft/bass yRHshells65/72,59/65,64/71. En04inversiónprimerii60/65; máximo7semitonosRH,sincollisiones.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "I-B03-002",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-independence-007",
    "location": "Deltas007/008 yautonomía",
    "expected": "Cada etapa realiza su novedad audible.",
    "observed": "Múltiples pares consecutivos MIDIidénticos pese a promesas de combinación, altura uomisión.",
    "correction": "007LHsolo,añadeRH,LHlarga,RHbreve,omiteúnico5.5;008acoplado,desplazado,ligado,otrapitch,omisión. Las15etapas carecen de duplicados consecutivos injustificados.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "I-B03-003",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-independence-009",
    "location": "Entrada ternaria",
    "expected": "Onset fraccionario2/3 y respuestaúnicaporcompás.",
    "observed": "Se llamaba ternario a un ataque entero3 solo porque duraba1/3, y se añadían respuestas contradictorias.",
    "correction": "009offset0→2/3,duración1/3→2/3,luegoinversiónyunataqueporbar alternando2/3y5/3. Walking idéntico en todas.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "I-B03-004",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-independence-007-05",
    "location": "Elección y nuevos textos009/008",
    "expected": "Única omisión por comparación y autonomía real; ii no se llama tónica.",
    "observed": "La nueva007-05acumulabadosomisiones5.5/11;008/009finalesnopermitíanelecciónexplícitay009-04llamabatónicaalprimerii.",
    "correction": "Restauradoelbloquede11, solo seomite5.5;taskeligereferenciaootraúnicaomisión.008/009permiten elegirubicacionespreservandoLH; título009-04diceii.",
    "owner": "master",
    "status": "resolved"
  }
]
```
