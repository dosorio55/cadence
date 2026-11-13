approved

# Expresión,lote03 — maestro

Revisadas las12etapas,48acordes y329notas nuevas, completos por grupos de ataque/duración/pitch/velocity/mano/rol. Correcciones del compositor verificadas y completadas por el maestro; sin subagentes revisores.

|Lección|Cuatro etapas|
|---|---|
|007|Toqueuniforme.5;LH2mantieneRH.5;RH.25conLH2;eleccióndeseparación. Mismos ataques y alturas en todas.|
|008|Pausa total;continuidadLH durante pausaRH;reentrada destacada;eleccióndehuecoconbase.|
|009|C5preparado4y suspendido8;resuelveB4en9;balance78soloarriba;prolongahasta9.5antesIen12.|

Las calidades están realizadas: C6 con E/A,Am7 con C/G,Dm7 con F/C yG7 con B/F; en009la cuarta C5ajenaalG7resuelve a terceraB4 con F4séptima sostenida. LHmásRHsin tercerahand,mano derecha máximo12semitonos/5notas durante preparaciónAm7+C5, sin solapamientos de tecla. Assertions verifican todoslosonsets/duraciones requeridos y pausas;12MIDI coincidentes,métricas sinavisos ybatchválido.001–006 intactas. Sin escucha ni ejecución física.

```json
[
  {
    "issueId": "E-B03-001",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-expression-007",
    "location": "Célula de bolero, G7 y deltas",
    "expected": "LH1/3,RH2/2&/4; duraciones comparables y calidades reales.",
    "observed": "RH usabaoffset2.5(3&), G7omitíaF;01/02teníanduracionesdistintasdelasafirmadas.",
    "correction": "OffsetsRH1/1.5/3, G7B/D/F.01todo.5,02soloLH2,03soloRH.25,04eligeRH.25/.5. FunciónC6esI(add6),noinversiónI6; textosprecisanpatrónyduration.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "E-B03-002",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-expression-008",
    "location": "Comparación y continuidad durante hueco",
    "expected": "Comparar pausa total con silencio RHsobrebase continua.",
    "observed": "Faltaba un contraste de pausa total;corrector cambió textos03/04aparatotalaunqueLHseguía, y01noquitabalasnotas.",
    "correction": "01silenciototal[4,8),02añadeúnicamenteLH4/6,03destacareentrada8,04eligecompásderechoconLHcontinua. Notas/criterios/descripciones cotejados.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "E-B03-003",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-expression-009",
    "location": "Preparación y resolución4–3",
    "expected": "Retardo preparado desde acorde anterior y resolución dentrodominante.",
    "observed": "C5atacaba8sinpreparación,base3.75seafirmaba4y04dejabahueco/resetvelocityfrentealtexto.",
    "correction": "C5preparado4enAm7yatraviesaG7desde8.01hasta12sin4–3dentroV;02C4–9/B9–12;03soloambasvelocity78;04resuelve9.5conCdur5.5yBdur2.5,vel78. F4esséptimaG7,nosu3.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "E-B03-004",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-expression-007",
    "location": "Copias de fichas en lessons.json",
    "expected": "Metadata de diseño inmutable.",
    "observed": "El corrector alteró las fichas007/008/009 yel integrador rechazó la partición.",
    "correction": "Restauradas las tres fichas exactas de data/lessons.json; solamente etapas/eventos fueron corregidos. Puerta batch yhuellas previas pasan.",
    "owner": "master",
    "status": "resolved"
  }
]
```
