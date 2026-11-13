approved

# Acompañamiento, lote04 — maestro

15etapas,80acordes,400notas.010bossa4compases:densidad,shells,novenaopcionalconritmoybajofijos.011pop8compases:inversiones,vozsuperioryretorno;dosrutasmejoradasydecisiónpropia.012jazz4compases:iiVImayorvsiioVimenor,quinta disminuidayguías G#3→A3/D4→C4conGséptimanaturaleni7.

Revisados todos los ataques, duraciones, registros y calidades. Shells3/7completosensufunciónycolores9correctos;voicingsRHhasta11semitonos. Batchválido,métricas0,15MIDI completos coincidentes.001–009intactas. Sin escucha ni ejecución física.

```json
[
  {
    "issueId": "AC-B04-001",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-accompaniment-012",
    "location": "Texto, delta y notas de referencia",
    "expected": "Cada transformación audible y cada instrucción coinciden sin regresiones ocultas.",
    "observed": "01pedíaresolverAm7aunqueeraCmaj7;04decía soloi7pero restaurabainadvertidamenteiiøanterior;hintintroducíaG4envezG3yduplicababajoenRH.",
    "correction": "Criterio01Cmaj7/Bnatural.04conservaiiøinvertidode03,solocambiai7G3/A3/C4;hintsmismosregistros.05restauraiiøD4F4A4comodecisiónpropiaexplicitada.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "AC-B04-002",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-accompaniment-011",
    "location": "Texto, delta y notas de referencia",
    "expected": "Cada transformación audible y cada instrucción coinciden sin regresiones ocultas.",
    "observed": "03reiniciaba01yrestaurabaelsaltodeloopG4→C4tras02;decíasoloAm6peromanteníaobjetivoretornosinsuprimir salto.",
    "correction": "03conserva02ylastC[52,55,60],solocambiaAm6. CimasC/D/C/A/C/C/D/C. Rutas04/05tienenretornounísono.05distinguecimasdelareferenciadeelecciónpropia.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "AC-B04-003",
    "severity": "minor",
    "entityType": "lesson",
    "entityId": "lesson-accompaniment-010",
    "location": "Texto, delta y notas de referencia",
    "expected": "Cada transformación audible y cada instrucción coinciden sin regresiones ocultas.",
    "observed": "Tareasycriteriosnocontrolabanlasnovenaespecíficasnilaeleccióndedensidad.",
    "correction": "Añadidoscriterios4/2notasysoloE4(Dm9),A4(G9),D5(Cmaj9)segúnetapa;05eligeunúnicocolorconreinciode02sinmovercélula/bajo.",
    "owner": "master",
    "status": "resolved"
  }
]
```
