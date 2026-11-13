approved

# rhythm — lote 01, revisión musical independiente

**Veredicto actual: approved, ciclo 1.** Cinco incidencias históricas verificadas y resueltas; ninguna abierta. Veredicto inicial: rejected, con dos major y tres minor. Este veredicto cubre únicamente `lesson-rhythm-001`, `lesson-rhythm-002` y `lesson-rhythm-003`. No se modificaron datos, piloto ni su revisión congelada.

## Alcance y método

Leídos README actualizado, metas/intros/prerrequisitos/dificultad del diseño, cobertura rhythm y los cinco arrays completos de trabajo y de `work/rhythm/checks`. Selección por relaciones lesson→stage→progression, no por posición física: **3 lecciones desarrolladas nuevas, 12 etapas, 12 progresiones, 34 acordes, 551 notas** en ciclo 1. Inicialmente fueron 37 acordes; la nueva base C única de003-01 sustituye cuatro eventos por uno, sin perder compases ni notas. El snapshot conserva 90 fichas de diseño; no son 90 lecciones desarrolladas. En esta revisión se comprobó que cada registro nuevo de trabajo existe idéntico en checks y que las fichas copiadas pertenecen al diseño. La comprobación de unión exhaustiva, huellas y puerta técnica del lote queda al maestro.

Se agruparon **todas** las notas por `(startBeat,durationBeats,hand,role)` e imprimieron todas las alturas y velocidades de cada grupo, sin truncamiento. No se muestrearon compases. Se exportaron las doce progresiones nuevas a un directorio temporal y se contrastaron todos sus eventos mediante `audit_delivery.inspect_midi`: **551 coincidencias**, PPQ 960, tempo 750000 µs/negra (80 BPM), 4/4, endTick 15360. `musical_metrics`: 12 progresiones, cero avisos; esto no valida símbolos de acorde ni pedagogía.

## Convenciones para la evidencia exhaustiva

En las tablas, t es negra desde 0 y b es comienzo de compás: 0,4,8,12. No confundir desplazamiento local 0 con tiempo musical uno. C4=MIDI60.

Todos los voicings usados se verificaron en cada ataque:

- **C:** bajo48; derecha `[60,64,67]`, C mayor.
- **G:** bajo43; derecha `[59,62,67]`, G mayor en inversión cómoda.
- **Am:** bajo45; derecha `[57,60,64]`, A menor; los seis eventos vi restantes ahora llevan símbolo Am correcto.
- **F:** bajo41; derecha `[57,60,65]`, F mayor.

Secuencia P = C/G/Am/F, un acorde por compás. Secuencia Q = C de t0 a8 y G de8 a16. Los grupos de bajos son siempre `left/bass`, velocidad72; los acordes son `right/harmony`. No hay notas de otros roles ni alturas ocultas. Velocidades derechas: 66 en001, 62 en002, 64 en003.

## Revisión por las doce etapas

Cada ID de etapa `stage-rhythm-LLL-SS` corresponde a `prog-rhythm-LLL-SS-primary`, sin alternativas nuevas. Los patrones siguientes abarcan todos los compases y todos los eventos de cada progresión.

| Etapa | Timeline concreto y notas contadas | Criterio musical/pedagógico |
|---|---|---|
| stage-rhythm-001-01 | P. Bajo t=0…15 enteros, duración1. Derecha t=0,4,8,12, duración4. 28 notas. | Cumple intro: bajo en negras, tríadas sostenidas y cuatro compases. I–V–vi–IV pop coherente en notas y símbolos Am corregidos (001 resuelta). |
| stage-rhythm-001-02 | P. Bajo idéntico. Derecha b+0 y b+2, duración2. 40 notas. | Novedad verificable: rearticular cada blanca sin alterar pulso bajo. El texto distingue tiempos musicales uno/tres y desplazamientos locales0/2 (005 resuelta). |
| stage-rhythm-001-03 | P. Bajo idéntico. Derecha t=0,4,12, duración4; silencio completo derecho [8,12). 25 notas. | Respiración audible y reentrada en el uno del compás4 (t12). Ahora identifica explícitamente A=base sostenida01 y B=03: la única novedad de esa comparación es omitir la tríada del compás3 (002 resuelta). Bajo45 solo en compás3 representa plan vi parcialmente, intencional durante el silencio. |
| stage-rhythm-001-04 | P. Bajo idéntico. Derecha t=0,8,12, duración4: omite compás2. 25 notas. | Autonomía explícita comparada con01: elegir un compás sin derecha. Referencia concreta muestra elección distinta de03, no solución única; conserva 16 negras. |
| stage-rhythm-002-01 | Q. Bajo t=0,2,…14, duración2. Derecha t=0,1,…15, duración0.5. 56 notas. | Bajo en blancas real; ataques derechos a negras separados, no duraciones de negra. La explicación se refiere a frecuencia de ataques: válido. Tríadas familiares y dos acordes, sin cromatismo. |
| stage-rhythm-002-02 | Q. Mismo bajo. Derecha t=0,0.5,…15.5, duración0.5. 104 notas. | Subdivisión real: 32 bloques a corcheas; las posiciones enteras y su articulación no cambian, se rellenan huecos. Densidad motivada por objetivo, no adorno automático. |
| stage-rhythm-002-03 | Q. Mismo bajo. Derecha b+{0,1,1.5,2,3,3.5}, duración0.5. 80 notas. | Elimina exactamente b+0.5 y b+2.5, musical 1&/3&, sin mover otros ataques. Ocho huecos en total: dos por compás, como explanationMd especifica. |
| stage-rhythm-002-04 | Q. Mismo bajo. Derecha b+{0,0.5,1.5,2,2.5,3.5}, duración0.5. 80 notas. | Autonomía real: dos huecos en b+1 y b+3, diferentes de03. Explicación y changeFromPrevious distinguen A=02 continua y B=04 con huecos musicales dos/cuatro; permite elegir otras posiciones (004 resuelta). |
| stage-rhythm-003-01 | C único [0,16). Bajo48 b+0/b+2, duración1. Derecha `[60,64,67]` b+0, duración0.5. 20 notas. | Base de contraste corregida: bajo y armonía idénticos a02; cambia únicamente la colocación/patrón derecho, no la progresión. Título, descripción y criterios también reflejan C estable. |
| stage-rhythm-003-02 | C único [0,16). Bajo48 b+0/b+2, duración1; derecha `[60,64,67]` b+1/b+3, duración0.5. 32 notas. | Backbeat auténtico dos/cuatro: frente a la base01 corregida conserva exactamente bajo y armonía C; ahora sí aísla el patrón rítmico (003 resuelta). |
| stage-rhythm-003-03 | P. Bajo b+0/b+2, duración1; derecha b+1/b+3, duración0.5. 32 notas. | El backbeat sobrevive a cada cambio de raíz: aquí el único cambio frente a02 es transferir el patrón a progresión P, expresamente documentado. Entradas derechas posteriores al cambio armónico son idiomáticas, no desincronización. |
| stage-rhythm-003-04 | Igual a03 excepto ausencia del bloque derecho en t11 (compás3, tiempo4). 29 notas. | Descanso de un ataque mantiene el dos del compás y todos los bajos. Es refinamiento válido del descanso propuesto en diseño, no obligación de callar todo el compás. Elección propia explícita, con referencia reproducible y no única. |

## Tonalidad, ejecución y propósito

Las tres fichas tienen una única primarySkill: pulso, subdivisión y patrón estilístico, respectivamente. Sus resultados audibles son distintos; no son clones con otro título. Las tareas, simplifyHint y extendHint repiten formulaciones, pero las explicaciones, cambios y criterios concretan material diferente por etapa; no hay placeholders ni se prometen pistas easy/hard inexistentes.

Las notas forman tríadas diatónicas de do mayor y acompañamientos pop sencillos. No se exige backbeat a001 ni002: allí importan pulso y subdivisión. En003 los ataques derechos locales1/3 son los tiempos musicales2/4, con bajo local0/2; el silencio final no destruye esa identidad.

Registros: izquierda41–48, monofónica; derecha57–67. Máximo simultáneo derecho **8 semitonos y tres notas**, izquierda0 semitonos y una nota; sin cruces ni teclas simultáneas duplicadas, sin solapamiento accidental ni notas fuera del loop. C→G conserva67 y mueve otras voces −1/−2; G→Am baja2/2/3; Am→F conserva57/60 y sube64→65. Saltos de bajo máximos5 semitonos, también al cerrar F→C. Todo es físicamente razonable para dificultad1 y conocimientos armónicos previos. Los 32 bloques derechos de002-02 equivalen a 2.67 ataques/s a80 BPM: exigencia repetitiva moderada, justificada por la corchea y con consejo de bajar tempo; no virtuosismo ni una tercera mano.

## Incidencias históricas — protocolo 8.3

Se conservan observed, location y correction originales para trazabilidad: describen el estado rechazado, no el estado actual. Cierre verificado por ID en la sección siguiente.

```json
[
  {
    "issueId": "R-B01-001",
    "severity": "major",
    "entityType": "chordEvent",
    "entityId": "chord-rhythm-001-01-primary-003",
    "location": "work/rhythm/chord-events.json y checks/chord-events.json: beat 8 de 001-01/02/03/04 y 003-01/03/04; IDs chord-rhythm-{001-01,001-02,001-03,001-04,003-01,003-03,003-04}-primary-003",
    "expected": "Símbolo Am para la función vi de do mayor y su realización A–C–E.",
    "observed": "Los siete registros dicen symbol A, que significa la mayor y exige C#; las notas derechas presentes son 57,60,64 y el bajo45, es decir Am. En001-03 solo suena bajo45 durante ese compás, pero el plan sigue indicando vi y debe ser Am.",
    "correction": "Cambiar los siete símbolos A a Am, conservando function vi y las notas diatónicas; actualizar snapshot y dependientes. No introducir C# para adaptar MIDI a una etiqueta incorrecta.",
    "owner": "composer-rhythm",
    "status": "resolved"
  },
  {
    "issueId": "R-B01-002",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-rhythm-001-03",
    "location": "work/rhythm/stages.json: explanationMd/changeFromPrevious; comparación prog-rhythm-001-02-primary con 001-03-primary",
    "expected": "Una respiración añadida sobre patrón anterior preservado o regreso explícito a la base01 antes de retirar un acorde.",
    "observed": "Dice conservar contexto y retirar el ataque del compás3, pero02 tenía dos ataques por compás de duración2. En03 desaparecen además t2,6,14 y se duplican duraciones derechas de los otros compases a4; el cambio no es únicamente callar compás3.",
    "correction": "Explicitar reinicio a la base sostenida01 y comparación A=01/B=03 para aislar la omisión del compás3, o conservar el patrón de blancas de02 fuera de ese compás.",
    "owner": "composer-rhythm",
    "status": "resolved"
  },
  {
    "issueId": "R-B01-003",
    "severity": "major",
    "entityType": "stage",
    "entityId": "stage-rhythm-003-02",
    "location": "work/rhythm/stages.json y progresiones/eventos de 003-01 frente a003-02, especialmente compases2–4",
    "expected": "Comparación A/B que aísle el nuevo backbeat manteniendo armonía y línea de bajo suficientes para atribuir el cambio audible a dos/cuatro.",
    "observed": "A=01 usa C/G/Am/F y bajos48/43/45/41. B=02 usa C durante16 negras y bajo48 en todos los compases, además de mover/agregar acordes a dos/cuatro. El texto reconoce tónica sostenida, pero afirmar que aísla el patrón no evita que la comparación completa cambie también la armonía.",
    "correction": "Hacer A/B sobre el mismo recorrido armónico y bajo: conservar P en02 o proporcionar una base de contraste en C para02 claramente identificada. Mantener03 como transferencia/estabilización justificada, sin añadir novedad artificial ni copiar eventos sin explicación.",
    "owner": "composer-rhythm",
    "status": "resolved"
  },
  {
    "issueId": "R-B01-004",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-rhythm-002-04",
    "location": "work/rhythm/stages.json: changeFromPrevious y referencia prog-rhythm-002-04-primary",
    "expected": "Distinguir la referencia externa A=etapa02 continua del ejemplo propio B con silencios elegidos.",
    "observed": "changeFromPrevious dice la referencia es corchea continua, pero la primary04 omite t1,3,5,7,9,11,13,15. explanationMd sí remite a02 como A, de modo que la tarea es recuperable pero la descripción del MIDI propio queda ambigua.",
    "correction": "Aclarar que A=02 es continua y B=04 ilustra una elección, omitiendo tiempos musicales dos/cuatro en cada compás, sin imponer esas posiciones al estudiante.",
    "owner": "composer-rhythm",
    "status": "resolved"
  },
  {
    "issueId": "R-B01-005",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-rhythm-001-02",
    "location": "work/rhythm/stages.json: explanationMd frente a changeFromPrevious",
    "expected": "Separar tiempos musicales1/3 de desplazamientos locales0/2, conforme a la convención de beats desde0.",
    "observed": "explanationMd dice beats1 y3 locales para las blancas derechas, pero los eventos empiezan local0 y2; changeFromPrevious correctamente sitúa el nuevo ataque en beat2 local. En003 local1/3 significa musical2/4, por lo que la terminología actual se contradice entre lecciones.",
    "correction": "Decir tiempos uno y tres, desplazamientos locales0 y2; no cambiar ataques ni duración de las notas.",
    "owner": "composer-rhythm",
    "status": "resolved"
  }
]
```

## Evidencia independiente de cierre — ciclo 1

Se parsearon nuevamente los cinco arrays completos reales de trabajo y los siete de checks. Para001–003 se comprobó igualdad exacta, incluidos orden y contenido, entre trabajo y snapshot: 3 fichas, 12 etapas, 12 progresiones, 34 acordes y551 notas. Se releyeron los textos completos de las etapas y los metadatos dependientes, no solo declaraciones de corrección. No se revisó material005+.

| Incidencia | Evidencia de cierre comprobada |
|---|---|
| R-B01-001 | Los eventos `chord-rhythm-001-{01,02,03,04}-primary-003` y `chord-rhythm-003-{03,04}-primary-003` llevan `symbol=Am,function=vi`, beat8 y duración4. No queda ningún símbolo A en el lote. El séptimo evento histórico, `chord-rhythm-003-01-primary-003`, desapareció correctamente al reemplazar toda su progresión por C único; no era necesario inventar un Am dentro de esa base nueva. Las notas A–C–E de los seis recorridos conservados permanecen diatónicas, sin C#. |
| R-B01-002 | `stage-rhythm-001-03.explanationMd` identifica A=base sostenida01 y B=03; `changeFromPrevious` anuncia explícitamente ese reinicio. Timeline confirmado: bajos a negras t0…15; derecha t0,4,12 duración4, única omisión respecto de01 en t8. No se afirma ya conservar las blancas de02. |
| R-B01-003 | `chord-rhythm-003-01-primary-001` es C/I, inicio0, duración16; solo existe ese acorde en003-01. Sus ocho bajos son48 en t0,2,…14 duración1; sus cuatro bloques derechos son60/64/67 en t0,4,8,12 duración0.5. Base01 y backbeat02 comparten ahora armonía, notas, articulación y bajo;02 cambia solo ataques derechos a t1,3,…15. Título y descripción de progression01, y explicación/cambio/criterio de stage01, describen esa base.003-03 transfiere después el mismo backbeat a C/G/Am/F, con cambio armónico documentado y sin otra novedad. |
| R-B01-004 | `stage-rhythm-002-04.explanationMd` y `changeFromPrevious` distinguen A=02 continua y B=04 con huecos en tiempos musicales dos/cuatro, offsets1/3; otras elecciones quedan permitidas. Timeline propio confirmado: ataques derechos locales0,0.5,1.5,2,2.5,3.5; bajo en blancas intacto. El criterio de éxito remite a silencios elegidos. |
| R-B01-005 | `stage-rhythm-001-02.explanationMd` dice literalmente tiempos musicales uno y tres, desplazamientos locales0 y2; corresponde a todas las notas derechas en blancas. El cambio conserva su nuevo ataque en offset2 local; no hay modificación MIDI innecesaria. |

Se volvieron a agrupar e inspeccionar **todos** los551 eventos por inicio/duración/mano/rol, con alturas y velocidades completas. Los demás timelines de la tabla permanecen válidos. La base nueva reduce exigencia de003-01 y mantiene dificultad1; no afecta registros máximos, objetivo único ni autonomía. No se observan regresiones musicales en001–003.

Se reexportaron las **12 progresiones** a directorio temporal y se contrastaron los551 note-on/off con `audit_delivery.inspect_midi`, además de velocidades, PPQ960, tempo750000, 4/4 y cierre15360 ticks: todas coinciden. La base003-01 corregida tiene SHA-256 MIDI `9a0f11aeaf2e2233f82cf9b7f62c9ce487a7aa8a47e3f0df4438cdf23522638a`. Los otros once SHA MIDI coinciden con los obtenidos en la revisión inicial: sus sonidos y tiempos no cambiaron; las correcciones de símbolos/textos no requieren alterar sus notas. Métricas reejecutadas: 12 progresiones, cero avisos.

## Límites y siguiente puerta

**Aprobación musical del lote001–003 tras ciclo1**, sin pendientes de esta revisión. Solo se actualizó este reporte; datos, piloto y reporte congelado permanecen fuera de la autoridad de escritura del revisor. Sin escucha de audio ni ejecución física; SQL, puerta técnica y comprobación global de huellas quedan al maestro. No se revisó ni produjo005+; continuar requiere la aprobación del maestro.
