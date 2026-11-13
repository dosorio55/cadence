verdict approved

# Revisión musical independiente — harmony, lote 01

Aprobación musical de H001–H003 tras verificar el cierre de las cuatro incidencias **minor**: **cero pendientes**, cero major/blocker. No equivale a integración, aprobación global ni permiso para otro lote; esas decisiones y la puerta técnica/hashes corresponden al maestro. No se autorreparó contenido.

## Alcance y pruebas

Leídos completos la especificación maestra, ponytail, README, mapa de cobertura, estándar `reports/pilot-music-review.md`, las tres fichas de diseño y todos los registros de trabajo/snapshot mediante parseo JSON completo. Trabajo: **3 lecciones, 12 stages, 12 progressions, 48 chord-events, 196 note-events**. Snapshot `work/harmony/checks`: 6 categorías, 30 skills, 90 fichas, y los mismos 12/12/48/196 registros musicales. Los cuatro arrays musicales coinciden exactamente entre trabajo y checks; las tres fichas de trabajo coinciden con diseño, y los tres arrays de diseño del snapshot coinciden con `data/`. No se confundieron las 90 fichas con 90 lecciones musicalizadas.

Se exportaron las **12** progresiones con `curriculum.midi_file` a un directorio temporal de `/tmp`, eliminado al terminar. `audit_delivery.inspect_midi` contrastó independientemente los **196 note-on/off**, incluyendo alturas, velocidades, inicios y finales exactos. Todos: SMF 0, PPQ 960, 833333 µs/negra = 72 BPM redondeados, 4/4 y endTick 15360 = 16 negras. Exportación directa para inspección musical, no ejecución de la CLI con validación previa. `musical_metrics`: 12 progresiones, **cero avisos**; no sustituye el juicio sobre símbolos y textos.

## Tabla de las 12 etapas

IDs abreviados H001-01 = `stage-harmony-001-01`; su referencia es `prog-harmony-001-01-primary`, y análogamente para todas las filas. Todas conservan do mayor, 72 BPM, 4/4 y cuatro compases. C4 = MIDI 60.

| Stage | Evidencia concreta y evaluación |
|---|---|
| H001-01 | C–F–C–C en 0/4/8/12, duración 4 cada uno: A realmente carece de V y repite tónica en el cierre. |
| H001-02 | Solo el tercer acorde pasa a G: derecha 59/62/67; B3=59 llega a C4=60 en beat 12. Preparación V–I inequívoca, contexto A/B conservado. |
| H001-03 | Mismo plan; G pasa a 62/67/71 y C final a 64/67/72. B4=71→C5=72 expone la sensible arriba; una novedad de disposición, no otra armonía. |
| H001-04 | Referencia vuelve a las alturas de 02: G 59/62/67→C 60/64/67. Texto actual remite a etapa 2, explicita el reinicio y B3 interior; description nombra V–I. H-B01-002/003 resueltas. |
| H002-01 | C–F–G–C, duraciones 4+4+4+4 y ataques 0/4/8/12. Base de bloque sostenido a dos manos. |
| H002-02 | ChordEvent y ambas manos pasan a 8+2+2+4, ataques 0/8/10/12. Se prolonga I y se concentran IV–V, sin alterar alturas, cantidad de bloques ni BPM. |
| H002-03 | Duraciones reales 6+4+2+4, ataques 0/6/10/12. IV gana dos negras; V e I final conservan tiempos de 02. |
| H002-04 | Referencia 6+3+3+4, ataques 0/6/9/12. La consigna permite otra distribución positiva de 16 negras; ejemplo no obligatorio y decisión limitada al ritmo armónico. |
| H003-01 | C–Dm7–G7–C; segundo bloque bajo D2=38 y derecha C4/D4/F4=60/62/65: shell de Dm7 sin quinta. Símbolo, función ii7 y texto actual coinciden; C compartido permite aislar F→F#. H-B01-001 resuelta. |
| H003-02 | Segundo bloque 60/62/66: F4→F#4 es la única altura que cambia respecto de A. D7 contiene tercera 66 y séptima 60; G7 siguiente contiene G4=67 y B3=59: F#→G y C→B disponibles en el enlace. |
| H003-03 | D7 cambia a 60/66/69, mantiene bajo 38: C/F#/A, shell con quinta y raíz en el bajo. G7 sigue 59/62/65/67. Guías presentes y destinos explícitos; tres→cuatro voces exige redistribución interior, no cinco notas derechas. |
| H003-04 | Regresa exactamente a A de 01: 60/62/65 sobre 38. La elección ii frente a V/V está acotada y B se remite a etapa 02; símbolo Dm7 y texto del shell/C compartido ahora coinciden con ii7 real. |

## Timeline completa agrupada — sin selección ni truncación

Cada fila representa **dos grupos completos** de NoteEvent con idénticos inicio/duración: `(inicio, duración, left, bass, alturas izquierda)` y `(inicio, duración, right, harmony, alturas derecha)`. Velocidad de todas las notas izquierdas: 70; derechas: 64. Las listas enumeran cada altura MIDI individual; no hay otros roles, manos, ataques ni notas sostenidas fuera de estos grupos. Las filas incluyen los 48 ChordEvent y los 96 grupos que contienen las 196 notas. El símbolo refleja literalmente el registro actual, incluidos los dos Dm7 corregidos.

| Progresión (sufijo H) | Inicio | Duración | ChordEvent símbolo / función | left / bass / pitches | right / harmony / pitches |
|---|---:|---:|---|---|---|
| 001-01 | 0 | 4 | C / I | [48] | [60,64,67] |
| 001-01 | 4 | 4 | F / IV | [41] | [60,65,69] |
| 001-01 | 8 | 4 | C / I | [48] | [60,64,67] |
| 001-01 | 12 | 4 | C / I | [48] | [60,64,67] |
| 001-02 | 0 | 4 | C / I | [48] | [60,64,67] |
| 001-02 | 4 | 4 | F / IV | [41] | [60,65,69] |
| 001-02 | 8 | 4 | G / V | [43] | [59,62,67] |
| 001-02 | 12 | 4 | C / I | [48] | [60,64,67] |
| 001-03 | 0 | 4 | C / I | [48] | [60,64,67] |
| 001-03 | 4 | 4 | F / IV | [41] | [60,65,69] |
| 001-03 | 8 | 4 | G / V | [43] | [62,67,71] |
| 001-03 | 12 | 4 | C / I | [48] | [64,67,72] |
| 001-04 | 0 | 4 | C / I | [48] | [60,64,67] |
| 001-04 | 4 | 4 | F / IV | [41] | [60,65,69] |
| 001-04 | 8 | 4 | G / V | [43] | [59,62,67] |
| 001-04 | 12 | 4 | C / I | [48] | [60,64,67] |
| 002-01 | 0 | 4 | C / I | [48] | [60,64,67] |
| 002-01 | 4 | 4 | F / IV | [41] | [60,65,69] |
| 002-01 | 8 | 4 | G / V | [43] | [59,62,67] |
| 002-01 | 12 | 4 | C / I | [48] | [60,64,67] |
| 002-02 | 0 | 8 | C / I | [48] | [60,64,67] |
| 002-02 | 8 | 2 | F / IV | [41] | [60,65,69] |
| 002-02 | 10 | 2 | G / V | [43] | [59,62,67] |
| 002-02 | 12 | 4 | C / I | [48] | [60,64,67] |
| 002-03 | 0 | 6 | C / I | [48] | [60,64,67] |
| 002-03 | 6 | 4 | F / IV | [41] | [60,65,69] |
| 002-03 | 10 | 2 | G / V | [43] | [59,62,67] |
| 002-03 | 12 | 4 | C / I | [48] | [60,64,67] |
| 002-04 | 0 | 6 | C / I | [48] | [60,64,67] |
| 002-04 | 6 | 3 | F / IV | [41] | [60,65,69] |
| 002-04 | 9 | 3 | G / V | [43] | [59,62,67] |
| 002-04 | 12 | 4 | C / I | [48] | [60,64,67] |
| 003-01 | 0 | 4 | C / I | [48] | [60,64,67] |
| 003-01 | 4 | 4 | Dm7 / ii7 | [38] | [60,62,65] |
| 003-01 | 8 | 4 | G7 / V7 | [43] | [59,62,65,67] |
| 003-01 | 12 | 4 | C / I | [48] | [60,64,67] |
| 003-02 | 0 | 4 | C / I | [48] | [60,64,67] |
| 003-02 | 4 | 4 | D7 / V/V7 | [38] | [60,62,66] |
| 003-02 | 8 | 4 | G7 / V7 | [43] | [59,62,65,67] |
| 003-02 | 12 | 4 | C / I | [48] | [60,64,67] |
| 003-03 | 0 | 4 | C / I | [48] | [60,64,67] |
| 003-03 | 4 | 4 | D7 / V/V7 | [38] | [60,66,69] |
| 003-03 | 8 | 4 | G7 / V7 | [43] | [59,62,65,67] |
| 003-03 | 12 | 4 | C / I | [48] | [60,64,67] |
| 003-04 | 0 | 4 | C / I | [48] | [60,64,67] |
| 003-04 | 4 | 4 | Dm7 / ii7 | [38] | [60,62,65] |
| 003-04 | 8 | 4 | G7 / V7 | [43] | [59,62,65,67] |
| 003-04 | 12 | 4 | C / I | [48] | [60,64,67] |

Comprobación del recuento: H001/H002 = 8 × 16 = 128 notas; H003 = 4 × 17 = 68; total **196**, no 192. Cada G7 tiene cuatro notas derechas más un bajo: **cinco sonidos entre dos manos**, no cinco notas en una mano ni un error de densidad.

## Juicio musical y pedagógico

**Función y conducción.** H001 contrasta preparación dominante real con reposo repetido, no una mera reetiquetación de I. F→G en las disposiciones bajas mueve voces ordenadas 60→59, 65→62, 69→67; G→C conserva G4 y resuelve B3→C4. H001-03 expone B4→C5 sin alterar el plan. El reinicio H001-04 es musicalmente válido y ahora está explicado con exactitud como regreso a la disposición de etapa 2.

H003 sostiene la comparación diatónica/cromática a tempo y duración idénticos. F#4=66 aparece solo bajo D7, dura cuatro negras y tiene G4=67 como destino inmediato; no se sanciona por estar fuera de do mayor. C4=60 de D7 puede bajar a B3=59; F4=65 de G7 puede bajar a E4=64 y B3 subir a C4 al llegar a I. En 003-02, F#→G no es una línea monofónica aislada: G7 añade una voz por debajo del sol; en 003-03 la redistribución permite seguir F#→G, C→B y A→F. Es ejecución pianística posible con reasignación de voces/dedos, no una afirmación de que todas las voces ordenadas avanzan por semitono. La omisión de quinta de D7 en 02 es un shell legítimo: raíz, tercera y séptima están realmente presentes. El rótulo actual Dm7 y la explicación del shell reconocen C natural como séptima compartida; no se lo trata como supuesto cromatismo erróneo.

**Ritmo real.** H002 modifica duración del plan y de toda su realización, no solo metadatos o BPM. Se conserva la regla de ejecución «un bloque sostenido por cambio», cuatro ataques por ciclo y los mismos voicings. Las posiciones de ataque necesariamente cambian con las fronteras armónicas: conservar patrón aquí no significa congelar timestamps mientras se cambian acordes. El C inicial de ocho negras dura unos 6.67 segundos a 72 BPM; su decaimiento natural es aceptable en balada y no requiere reataques ocultos. El mínimo de dos negras deja unos 1.67 segundos por bloque, accesible para la dificultad 1.

**Tocabilidad.** Izquierda monofónica MIDI 38–48; derecha 59–72. Máximo simultáneo: izquierda una nota, derecha tres en H001/H002 y cuatro en H003. Extensión derecha máxima: nueve semitonos; G7 abarca ocho. Bajo C3→D2 de H003 baja diez semitonos, con cuatro negras disponibles y sin acorde izquierdo extendido. No hay teclas compartidas solapadas, cruces de manos, colas exteriores ni necesidad de pedal o tercera mano. Dificultades 1/1/2 plausibles para un estudiante con los prerrequisitos declarados. No se evaluó físicamente ergonomía individual.

**Contexto, autonomía y ayudas.** Cada final permite una decisión concreta (ubicación de V, distribución temporal o ii/V/V) y mantiene referencia reproducible sin exigir una respuesta única. Las comparaciones A/B son recuperables entre etapas, no se promete una alternativa separada inexistente. H003-03 dirige una escucha nueva sobre guías ya presentes y cambia disposición, sin añadir otro concepto armónico. Las ampliaciones son consejos textuales, no falsas pistas advanced. La ayuda específica actual de H003-03 propone practicar F#–G y C–B por separado, o mantener ambas guías en shells sin quinta y con las mismas duraciones; ya no elimina la séptima objetivo de D7. Pop/balada de bloques sostenidos es una reducción pertinente; la etiqueta jazz de H003 describe el recurso de dominantes/séptimas, no promete swing ausente.

## Incidencias — protocolo 8.3

Histórico de cuatro **minor**, todas **resolved** tras comprobar trabajo y checks actuales. `observed`, `location` y `correction` conservan la devolución original, no describen fallos actuales. La evidencia de cierre figura después del bloque; cero incidencias pendientes.

```json
[
  {
    "issueId": "H-B01-001",
    "severity": "minor",
    "entityType": "chordEvent",
    "entityId": "chord-harmony-003-01-primary-002",
    "location": "work/harmony/chord-events.json: symbol Dm frente a function ii7, beat 4; también chord-harmony-003-04-primary-002 y textos A de stages 003-01/003-04",
    "expected": "Símbolo, explicación de A y función describen con precisión la calidad realizada, conservando una comparación A/B de una sola alteración.",
    "observed": "A dice Dm, pero realiza D2 más C4/D4/F4: Dm7 sin quinta, coherente con ii7. B conserva C4 y cambia únicamente F4 por F#4. El contraste audible funciona, pero A no es la tríada anunciada.",
    "correction": "Rotular explícitamente Dm7/shell en los eventos y textos afectados, indicando la séptima compartida con D7. Mantener el diseño aprobado; si es necesario aclarar su intro congelada, elevar esa precisión al maestro en vez de modificarla unilateralmente.",
    "owner": "composer-harmony",
    "status": "resolved"
  },
  {
    "issueId": "H-B01-002",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-harmony-001-04",
    "location": "work/harmony/stages.json: explanationMd y changeFromPrevious; beats 8 y 12 de la primary",
    "expected": "La retirada de ayuda identifica exactamente la referencia B y cualquier regreso a disposición conocida.",
    "observed": "explanationMd identifica B como etapa 3, pero la referencia sonora de 04 reproduce etapa 2: G [59,62,67] y C [60,64,67], no [62,67,71] y [64,67,72]. changeFromPrevious no explica este regreso de la sensible al interior.",
    "correction": "Remitir la referencia sonora a etapa 2 y explicitar el reinicio a su disposición antes de decidir ubicación de V, o mantener realmente la disposición de etapa 3; no introducir otra tarea técnica.",
    "owner": "composer-harmony",
    "status": "resolved"
  },
  {
    "issueId": "H-B01-003",
    "severity": "minor",
    "entityType": "progression",
    "entityId": "prog-harmony-001-04-primary",
    "location": "work/harmony/progressions.json: description",
    "expected": "Nombrar V–I como enlace funcional de los compases 3–4.",
    "observed": "La descripción dice 'B–I aparece en los compases 3–4'; los eventos son G/V y C/I. B es la etiqueta comparativa o la sensible, no el acorde dominante realizado.",
    "correction": "Decir 'V–I en los compases 3–4 de la referencia B', evitando confundir etiqueta A/B, nombre de nota y función.",
    "owner": "composer-harmony",
    "status": "resolved"
  },
  {
    "issueId": "H-B01-004",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-harmony-003-03",
    "location": "work/harmony/stages.json: simplifyHint frente a task y successCriteria",
    "expected": "La ayuda reducida conserva las dos líneas objetivo, o propone practicarlas separadas de forma explícita.",
    "observed": "El consejo genérico 'solo bajo y tercera' elimina C, séptima de D7, y con ello C–B, una de las dos guías que esta etapa pide oír. El ejemplo completo sí contiene ambas guías.",
    "correction": "Adaptar solo la ayuda de esta etapa: practicar por separado F#–G y C–B como ya propone task, o conservar ambas guías con menos duplicaciones y sin cambiar duraciones.",
    "owner": "composer-harmony",
    "status": "resolved"
  }
]
```

## Evidencia de cierre — ciclo 1

Se parsearon íntegramente los cinco arrays actuales de trabajo y los siete de checks. Se mantienen 3/12/12/48/196 en trabajo y 6/30/90/12/12/48/196 en checks. Los cuatro arrays musicales coinciden exactamente entre ambos; las fichas de trabajo y el diseño completo de checks siguen coincidiendo con `data/`.

Las **196 notas actuales** se contrastaron una por una con la timeline de la revisión inicial: progresión, inicio, duración, mano, role, altura y velocidad permanecen idénticos; 196 IDs actuales únicos. No se afirma una comparación histórica de IDs no incluidos en aquella timeline. La tabla completa se conserva y solo actualiza los dos símbolos Dm7. La exportación e inspección MIDI corresponden a la revisión inicial; no se reexportó en este cierre porque los eventos y los parámetros musicales de reproducción siguen coincidiendo con los allí documentados.

- **H-B01-001:** `chord-harmony-003-01-primary-002` y `chord-harmony-003-04-primary-002` ahora dicen `symbol: Dm7`, `function: ii7`. Las explicaciones y tareas de 003-01/04 nombran Dm7/shell y explicitan C compartido; el A/B de 01/02 conserva 60/62 y cambia únicamente 65→66. Las fichas congeladas permanecen intactas: es una precisión de la realización mediante shells, no una modificación del diseño.
- **H-B01-002:** `stage-harmony-001-04.explanationMd`, `task` y `changeFromPrevious` remiten a etapa 2, describen el regreso a su disposición y la sensible B3 interior. Las alturas 59/62/67→60/64/67 confirman ese texto.
- **H-B01-003:** `prog-harmony-001-04-primary.description` dice ahora «V–I en los compases 3–4 de la referencia B», coherente con G/V@8 y C/I@12.
- **H-B01-004:** `stage-harmony-003-03.simplifyHint` propone «F#–G y C–B por separado» o ambas guías en shells sin quinta, conservando expresamente la séptima de D7 y las duraciones. Coincide con task, criterios y notas completas.

Los cuatro cierres se verificaron en trabajo **y** checks; no se aceptaron solo por declaración del compositor. Sin incidencias nuevas observadas en estos cambios de texto/rotulado. Pendientes: **0**.

## Límites y siguiente puerta

Inspección completa temporal, musical y binaria, **sin escucha de audio ni interpretación física**. No se ejecutaron validación técnica global, pruebas generales, SQL, integración ni hashes: responsabilidad paralela del maestro. Solo se escribió este informe; no se modificaron JSON, scripts ni otros reportes y no se lanzaron subagentes.

Resultado musical: aprobado este lote con las cuatro minor verificadas y resueltas, cero pendientes. La siguiente puerta técnica/inmutable corresponde al maestro; cualquier futura major bloquearía la aprobación.
