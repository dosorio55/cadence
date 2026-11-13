approved

# Acompañamiento, lote03 — maestro

Inspeccionadas15etapas,60acordes y252notas nuevas completas, antes y después de corregir el borrador.

|Lección|Cinco etapas verificadas|
|---|---|
|007|Shells separados;ii invertido con enlace cercano;C4de llegada;otra posición deI7;elección de posición. Blancas y3/7seconservan.|
|008|Tres notas cortas; cima larga sobre arpegio inferior;dos planos;menosrellenoencompás2;eleccióndeotrocompás. Notas acordales reales sin3manos.|
|009|Shell;9enii/V;9tambiénI;Vvuelve7;eleccióndeIcolor. NovenasE/A/Dreales con3/7completas.|

Todos los deltas se corresponden con eventos, y los criterios no presuponen notas aún ausentes. Mano derecha máximo11semitonos/3notas, sin solapamientos de tecla.001–006intactas;batchválido,métricas0 y15MIDI completos coincidentes. Sin escucha ni ejecución física.

```json
[
  {
    "issueId": "A-B03-001",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-accompaniment-007",
    "location": "Guías y deltas",
    "expected": "Shells cercanos y sensible ascendente, con una inversión alternativa.",
    "observed": "002añadíaC4 pese a prometer alturas intactas;003soloacortabaC4y005eraidéntica04sinmostrarinversión.",
    "correction": "002invierteiiC4/F4paraC4→B3yF4común;003añadeC4brevepararecibirB3conF4→E4;004mueveI7B4→B3;005eligeprimerIenB4. Guías completas, LHblancas idénticas.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "A-B03-002",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-accompaniment-008",
    "location": "Armonía real y simultaneidad",
    "expected": "Tres notas acordales cercanas, cima sostenida mientras suena arpegio inferior y elección de menos relleno.",
    "observed": "Se repetíaC/E/G/CsobreAm/F/G; la cima entraba después del relleno, no durante;003/004/005eranidénticas y04prometía duración1.5peroera2.",
    "correction": "Arpegios propiosdeC/Am/F/G con3alturas; cima0yrelleno1/2.01todoRH.5;02cima4;03interiores55/cima75;04omiteA3en5;005mueveúnicaomisióna9. LHraízquinta ydosmanos reales.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "A-B03-003",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-accompaniment-009",
    "location": "Novena y símbolos",
    "expected": "Novena real, 3/7 preservadas y disposición dentro de octava en todas las etapas.",
    "observed": "Texto llamabaA novena deD (esquinta);G9usaba span16;02yaañadíaD5aI sinetiqueta;005rotulaba9sinnotas9.",
    "correction": "Dm9F3/C4/E4, G9B3/F4/A4, Cmaj9E4/B4/D5.02añadeii/V,03añadeI,04quitaV9,05quitaii9. Assertions cotejan3/7y9contraTODOSsímbolos; spanmáximo11.",
    "owner": "master",
    "status": "resolved"
  }
]
```
