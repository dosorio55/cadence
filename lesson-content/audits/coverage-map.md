# Mapa de cobertura — fase B

## Lectura y alcance

Este documento conserva el diseño aprobado de fase B, anterior a la composición; las referencias a material futuro describen ese momento. El piloto posterior fue aprobado tras corregir seis incidencias; su alternativa implementada es I–vi–IV–V, con eventos propios, según `pilot-music-review.md`.

Diseño de 6 categorías, 30 skills y 90 lecciones. Los tres JSON son arrays planos; este mapa explica decisiones, no agrega campos al contrato. No hay etapas, progresiones ni eventos compuestos todavía.

En las tablas, `skill` es el sufijo de `skill-<slug>-<sufijo>` dentro de la categoría del encabezado. Prerrequisitos abreviados: `R001` = `lesson-rhythm-001`, `A001` = `lesson-accompaniment-001`, `H001` = `lesson-harmony-001`, `M001` = `lesson-melody-001`, `I001` = `lesson-independence-001`, `E001` = `lesson-expression-001`. `—` significa sin lección previa obligatoria. D = dificultad pedagógica, no velocidad; c. = compases del futuro ejemplo de referencia en 4/4.

Cada fila declara una ganancia audible respecto del material anterior y una decisión que quedará en manos del estudiante. Los prerrequisitos JSON son autoritativos y explícitos: el orden visual no obliga a cursar otras ramas. La dificultad 5 exige selección autónoma y control de frase, no virtuosismo.

## Fronteras de responsabilidad

- **rhythm:** cambia cuándo suena algo. El piloto adelanta la frontera armónica solo para demostrar colocación temporal; no elige acordes nuevos.
- **accompaniment:** cambia qué notas y registros realizan acordes dados. La conducción es de voces, no una decisión de función armónica.
- **harmony:** cambia qué acorde ocurre, cuánto dura o adónde conduce. Voicings y ejecución se mantienen sencillos para aislar esa decisión.
- **melody:** cambia la línea cantable y sus destinos, con una base poco demandante.
- **independence:** mantiene un proceso de una mano mientras varía el otro. Los patrones estilísticos se conocen antes de coordinarlos.
- **expression:** modifica jerarquía, toque, respiración o función formal de material conocido; no introduce más notas para simular expresión.

El cruce no supone duplicación: R008 presenta la célula de bolero; I007 sostiene sus procesos simultáneos; E007 modifica las duraciones manteniendo los ataques. A007 elige notas guía; H006 organiza funciones menores; M006 elige destinos melódicos.

## rhythm — Ritmo y groove

| Lección | Skill | Prerrequisitos | D | c. | Ganancia audible y autonomía final |
|---|---|---|---:|---:|---|
| lesson-rhythm-001 | pulse | — | 1 | 4 | Establece el pulso bajo cambios de tríada; elegir una respiración sin acortar el ciclo. |
| lesson-rhythm-002 | subdivision | R001 | 1 | 4 | Oye y mantiene la corchea ausente, no solo la negra tocada; elegir dos huecos. |
| lesson-rhythm-003 | style-patterns | R002 | 1 | 4 | Convierte pulso abstracto en backbeat de pop en dos y cuatro; elegir un descanso que no lo borre. |
| lesson-rhythm-004 | syncopation | R002, R003 | 2 | 4 | Adelanta una llegada completa a 4& y la sostiene sobre uno; elegir otra frontera a anticipar. |
| lesson-rhythm-005 | swing | R002 | 2 | 4 | Distingue corchea recta y referencia ternaria sin mover la negra; elegir una pausa dentro de la frase. |
| lesson-rhythm-006 | pulse | R001, R003 | 2 | 8 | Conserva el ciclo al retirar ataques de ambas manos, más allá de repetir negras; elegir un compás de aire. |
| lesson-rhythm-007 | subdivision | R002, R006 | 2 | 4 | Introduce una célula corta de semicorcheas con huecos de funk; elegir un ataque desplazado en esa rejilla. |
| lesson-rhythm-008 | style-patterns | R003, R004 | 2 | 4 | Añade la respuesta de bolero en dos, 2& y cuatro sobre bajo uno/tres; elegir una omisión conservando identidad. |
| lesson-rhythm-009 | syncopation | R004, R007 | 3 | 4 | Sostiene 2& sobre tres sin cambiar la armonía: distingue síncopa y anticipación; elegir otro ataque ligado. |
| lesson-rhythm-010 | swing | R005, R006 | 3 | 4 | Entra en el último tercio del pulso, no siempre a tierra; elegir final con silencio manteniendo swing. |
| lesson-rhythm-011 | pulse | R006, R007 | 3 | 8 | Conserva tempo al pasar de densidad alta a baja; diseñar contraste y comprobar llegada al compás cinco. |
| lesson-rhythm-012 | subdivision | R007, R009 | 3 | 4 | Desplaza una célula completa una semicorchea sin deformarla; elegir cuándo recuperar su posición inicial. |
| lesson-rhythm-013 | style-patterns | R008, R009, R012 | 4 | 8 | Organiza guajeo reducido en ciclo de clave de son 2–3, no síncopas genéricas; variar sin invertir orientación. |
| lesson-rhythm-014 | syncopation | R004, R009, R013 | 4 | 8 | Integra una llegada anticipada en un ciclo de dos compases ya conocido; elegir otra sin anticipar todo. |
| lesson-rhythm-015 | swing | R010, R011, R012 | 5 | 8 | Construye un discurso de swing con entradas y pausas relacionadas; decidir frase propia de pocas notas. |

**Salida de categoría:** sostener un ciclo y decidir colocación, densidad y respiración; distinguir swing, subdivisión recta, síncopa y anticipación. El guajeo reducido es un recurso específico, no una certificación de dominio del son.

## accompaniment — Acompañamiento y voicings

| Lección | Skill | Prerrequisitos | D | c. | Ganancia audible y autonomía final |
|---|---|---|---:|---:|---|
| lesson-accompaniment-001 | inversions | R001 | 1 | 4 | Reduce saltos entre tríadas manteniendo raíces; elegir una inversión con nota común. |
| lesson-accompaniment-002 | shells | A001 | 1 | 4 | Conserva identidad de séptimas con tercera y séptima en vez de bloques completos; elegir octava cómoda. |
| lesson-accompaniment-003 | arpeggiation | A001, R002 | 1 | 4 | Despliega la tríada en el tiempo sin perder voz superior; elegir dónde sostenerla. |
| lesson-accompaniment-004 | spacing | A001, A002 | 2 | 4 | Despeja el grave distribuyendo entre manos, no abriendo la mano a la fuerza; elegir registro medio claro. |
| lesson-accompaniment-005 | comping | A002, A004, R005 | 2 | 4 | Reduce voces en huecos de una frase guía presentada aparte; elegir disposición que no ocupe su registro. |
| lesson-accompaniment-006 | inversions | A001, A004 | 2 | 8 | Conduce una voz superior por pasos sobre varios enlaces; elegir otro recorrido sin cambiar acordes. |
| lesson-accompaniment-007 | shells | A002, A006 | 2 | 4 | Relaciona shells por resoluciones pequeñas y no posiciones aisladas; elegir su inversión alternativa. |
| lesson-accompaniment-008 | arpeggiation | A003, A006 | 2 | 4 | Sostiene una nota superior sobre el arpegio interior; elegir un compás con menos relleno. |
| lesson-accompaniment-009 | spacing | A004, A007 | 3 | 4 | Añade novena preservando guías y bajo despejado; elegir dónde usar color y dónde volver a dos voces. |
| lesson-accompaniment-010 | comping | A005, A007, A009, R009 | 3 | 4 | Adapta densidad de voicings a una célula dada de bossa y bajo raíz–quinta; elegir disposición sin inventar ritmo nuevo. |
| lesson-accompaniment-011 | inversions | A006, A008 | 3 | 8 | Resuelve el salto entre final e inicio del loop, no solo enlaces internos; diseñar una ruta cerrada alternativa. |
| lesson-accompaniment-012 | shells | A007, A009, H006 | 3 | 4 | Hace reconocible iiø con quinta disminuida y llegada menor; elegir shell ampliado sin tensiones nuevas. |
| lesson-accompaniment-013 | arpeggiation | A008, A011 | 4 | 8 | Reduce actividad arpegiada preservando continuidad superior; decidir la transición de textura hacia el cierre. |
| lesson-accompaniment-014 | spacing | A009, A011, A012 | 4 | 8 | Contrasta frases por registro y densidad con dinámica fija; elegir retorno al registro inicial. |
| lesson-accompaniment-015 | comping | A010, A013, A014 | 5 | 8 | Selecciona shells, color y descansos según frase guía y patrón conocido; construir arreglo propio a dos manos. |

**Salida de categoría:** realizar una progresión dada con decisiones de inversión, registro y textura que dejen espacio al canto. No se exige melodía, bajo y acordes como tres partes físicamente independientes.

## harmony — Movimiento armónico

| Lección | Skill | Prerrequisitos | D | c. | Ganancia audible y autonomía final |
|---|---|---|---:|---:|---|
| lesson-harmony-001 | cadences | A001 | 1 | 4 | Hace oír preparación dominante y llegada a I frente a sucesión sin V; elegir su ubicación. |
| lesson-harmony-002 | harmonic-rhythm | H001, R002 | 1 | 4 | Cambia duración de funciones manteniendo ataques regulares; elegir dónde concentrar dos cambios. |
| lesson-harmony-003 | secondary-dominants | H001, A002 | 2 | 4 | Introduce V/V y resuelve su alteración hacia V; elegir si intensificar la preparación. |
| lesson-harmony-004 | passing-chords | H002, A001 | 2 | 4 | Une I y vi mediante V en primera inversión con tiempo armónico propio; elegir duración del descenso de bajo. |
| lesson-harmony-005 | substitutions | H001, A006 | 2 | 4 | Mantiene nota melódica mientras sustituye llegada I por vi; elegir cierre evitado, no reposo pleno. |
| lesson-harmony-006 | cadences | H001, A007 | 2 | 4 | Escucha iiø–V7–i y sensible en menor; elegir duración del descanso en i. |
| lesson-harmony-007 | harmonic-rhythm | H002, H005 | 2 | 8 | Contrasta prolongación inicial y respuesta de cambios más frecuentes; elegir duraciones de la respuesta. |
| lesson-harmony-008 | secondary-dominants | H003, H006 | 3 | 4 | Toniciza vi y retorna al centro principal, más allá de preparar V; decidir si aporta dirección. |
| lesson-harmony-009 | passing-chords | H004, H003, A007 | 3 | 4 | Enlaza I y ii con disminuido cromático resuelto, no simple inversión diatónica; elegir duración breve. |
| lesson-harmony-010 | substitutions | H005, H006 | 3 | 4 | Cambia IV por iv conservando nota superior y resolución de sexta rebajada; elegir repetición con préstamo. |
| lesson-harmony-011 | cadences | H006, H007, A007 | 3 | 8 | Diferencia cierre y turnaround I–vi–ii–V por su función de retorno; elegir terminar o relanzar. |
| lesson-harmony-012 | harmonic-rhythm | H007, H011 | 3 | 8 | Diseña una curva completa de frecuencia de cambios sin variar BPM; decidir máxima actividad y reposo. |
| lesson-harmony-013 | secondary-dominants | H008, H012 | 4 | 8 | Coordina dos tonicizaciones y regreso a I, no dominantes aisladas; elegir una o dos según la frase. |
| lesson-harmony-014 | passing-chords | H009, H011, H012 | 4 | 8 | Selecciona un enlace de paso sin erosionar funciones principales; decidir entre paso diatónico o disminuido conocido. |
| lesson-harmony-015 | substitutions | H010, H013, H014, A009 | 5 | 8 | Compara V7 y sustituto de tritono bajo fa–mi compatible; elegir una única sustitución con destino explícito. |

**Salida de categoría:** proponer una modificación armónica limitada, describir su destino y comprobar que conserva melodía y forma. No equivale a reharmonización libre sin restricciones.

## melody — Melodía y fraseo

| Lección | Skill | Prerrequisitos | D | c. | Ganancia audible y autonomía final |
|---|---|---|---:|---:|---|
| lesson-melody-001 | target-notes | H001, R002 | 1 | 4 | Señala cada cambio con una nota del acorde en vez de una nota indiferente; elegir objetivos. |
| lesson-melody-002 | motifs | M001 | 1 | 4 | Da identidad con un motivo de tres notas y pausa; elegir una adaptación de altura sin perder el ritmo. |
| lesson-melody-003 | passing-tones | M001, R002 | 1 | 4 | Conecta apoyos por paso débil en vez de salto directo; elegir una conexión con destino fijo. |
| lesson-melody-004 | approaches | M001, M003, H001 | 2 | 4 | Prepara una llegada desde vecina superior, no necesariamente entre dos apoyos; elegir nuevo objetivo. |
| lesson-melody-005 | question-answer | M002, M003 | 2 | 4 | Relaciona dos frases separadas por aire y cierra la respuesta; elegir nota final. |
| lesson-melody-006 | target-notes | M001, A007 | 2 | 4 | Usa terceras para revelar calidad mayor/menor, no cualquier nota acordal; elegir ruta cercana. |
| lesson-melody-007 | motifs | M002, M005, R004 | 2 | 4 | Transforma ritmo conservando alturas y contorno del motivo; inventar una segunda variación pequeña. |
| lesson-melody-008 | passing-tones | M003, M006 | 2 | 4 | Prolonga un apoyo con salida y regreso por bordadura; elegir dirección superior o inferior. |
| lesson-melody-009 | approaches | M004, M006, H006 | 3 | 4 | Añade aproximación cromática inferior con resolución exacta; elegir una llegada que la justifique. |
| lesson-melody-010 | question-answer | M005, M007, M008 | 3 | 8 | Construye respuesta distinta que conserva identidad motívica; elegir rasgo común y cierre. |
| lesson-melody-011 | target-notes | M006, M008, H011 | 3 | 8 | Planea llegadas de una cadencia completa antes de conectar; elegir objetivos de una segunda frase. |
| lesson-melody-012 | motifs | M007, M010, M011 | 3 | 8 | Sostiene desarrollo y regreso de un motivo durante la forma; elegir momento de recuperación. |
| lesson-melody-013 | passing-tones | M008, M011, M012 | 4 | 8 | Integra y retira adornos según jerarquía de frase, no por densidad; elegir dos conexiones y conservar silencios. |
| lesson-melody-014 | approaches | M009, M011, M013 | 4 | 4 | Rodea un objetivo con dos notas y resuelve a tiempo; elegir una sola llegada para el cerco. |
| lesson-melody-015 | question-answer | M010, M012, M013, M014 | 5 | 8 | Crea pregunta y respuesta cantables con objetivos y pausas propios; elegir recursos, sin obligación de usarlos todos. |

**Salida de categoría:** improvisar una frase breve identificable, con destinos y respiración, sobre armonía conocida. La izquierda queda deliberadamente sencilla para no adelantar exigencias de independencia.

## independence — Bajo e independencia

| Lección | Skill | Prerrequisitos | D | c. | Ganancia audible y autonomía final |
|---|---|---|---:|---:|---|
| lesson-independence-001 | bass-pulse | R001, M001 | 1 | 4 | Mantiene blancas izquierdas aunque la derecha calle; elegir un compás sin melodía. |
| lesson-independence-002 | alternation | I001, R003, A001 | 1 | 4 | Alterna bajo y acorde conservando duración izquierda, no solo ataques separados; elegir enlace problemático. |
| lesson-independence-003 | ostinatos | I001, R002 | 1 | 4 | Repite raíz–quinta a negras bajo notas derechas largas; elegir pausa sin cortar la célula. |
| lesson-independence-004 | walking | I002, A007, H001 | 2 | 4 | Dirige cuatro negras izquierdas al próximo acorde sobre shell largo; elegir aproximación diatónica. |
| lesson-independence-005 | melody-over-pattern | I003, M002 | 2 | 4 | Añade motivo y respiración a una base simple sin igualar ritmos; elegir dónde canta y calla. |
| lesson-independence-006 | bass-pulse | I001, I005, R009 | 2 | 4 | Mantiene negras cuando la derecha entra en 2& y sostiene; elegir otro contratiempo independiente. |
| lesson-independence-007 | alternation | I002, I006, R008 | 2 | 4 | Coordina respuesta de bolero con dos ataques derechos próximos sin arrastrar el bajo; elegir una omisión. |
| lesson-independence-008 | ostinatos | I003, I006, R007, R009 | 2 | 4 | Conserva ostinato reducido de funk frente a síncopa derecha; elegir hueco derecho con izquierda intacta. |
| lesson-independence-009 | walking | I004, I006, R010 | 3 | 4 | Mantiene walking mientras un shell entra en contratiempo ternario; elegir una respuesta por compás. |
| lesson-independence-010 | melody-over-pattern | I005, I007, M008 | 3 | 4 | Sostiene y resuelve una nota derecha sobre cambio izquierdo; elegir una ligadura compatible sin que el bajo espere. |
| lesson-independence-011 | bass-pulse | I006, I010, M010 | 3 | 8 | Mantiene base en una forma con respiraciones derechas distintas; diseñar pausas sin copiarlas abajo. |
| lesson-independence-012 | alternation | I007, I008, A010 | 3 | 8 | Conserva bajo raíz–quinta frente a célula de bossa de dos compases; elegir versión derecha más escasa. |
| lesson-independence-013 | ostinatos | I008, I011, R012 | 4 | 8 | Mantiene ostinato de funk durante contraste entre frases; elegir síncopas y silencios sin cambiar bajo. |
| lesson-independence-014 | walking | I009, I011, H011, M009 | 4 | 8 | Añade aproximación cromática al walking manteniendo comping escaso; elegir dos respuestas para toda la frase. |
| lesson-independence-015 | melody-over-pattern | I010, I012, I013, M012 | 5 | 8 | Crea melodía propia sobre patrón de balada invariable; decidir llegadas y respiraciones sin deformar la base. |

**Salida de categoría:** sostener una función izquierda conocida mientras la derecha toma decisiones reales. El walking con comping y la melodía sobre patrón son tareas distintas; no se suman en una exigencia de tres manos.

## expression — Interpretación y forma

| Lección | Skill | Prerrequisitos | D | c. | Ganancia audible y autonomía final |
|---|---|---|---:|---:|---|
| lesson-expression-001 | dynamics | M001, I001 | 1 | 4 | Destaca melodía sobre base sin cambiar notas; elegir balance que mantenga audible el bajo. |
| lesson-expression-002 | articulation | E001, M002 | 1 | 4 | Distingue ligado y separado manteniendo inicios idénticos; elegir toque sin confundirlo con volumen. |
| lesson-expression-003 | space | E001, M005, R006 | 1 | 4 | Sostiene silencio deliberado y reentrada puntual; elegir duración del hueco, no rellenarlo por reflejo. |
| lesson-expression-004 | tension-release | E001, E002, H001 | 2 | 4 | Dirige dinámica y duración hacia V y relaja en I; elegir grado de énfasis sin alterar tempo. |
| lesson-expression-005 | form | E003, E004, H002 | 2 | 8 | Introduce señal previa que anuncia pulso y llegada; elegir entrada de dos compases dentro del total. |
| lesson-expression-006 | dynamics | E001, E004 | 2 | 4 | Construye arco dinámico continuo en vez de acentos aislados; elegir una nota culminante. |
| lesson-expression-007 | articulation | E002, I007 | 2 | 4 | Diferencia bajo sostenido y respuesta breve de bolero sin mover ataques; elegir grado de separación. |
| lesson-expression-008 | space | E003, I005, E006 | 2 | 4 | Deja respirar melodía mientras la base sigue, no silencio indiscriminado; elegir hueco que prepare respuesta. |
| lesson-expression-009 | tension-release | E004, E006, A007, M008 | 3 | 4 | Hace perceptible suspensión 4–3 ya presentada en la base y su descanso; elegir balance de voz superior. |
| lesson-expression-010 | form | E005, E008, H011 | 3 | 8 | Usa armonías conocidas como señales de retorno o final; elegir función formal y articulación. |
| lesson-expression-011 | dynamics | E006, E008, M010 | 3 | 8 | Jerarquiza dos frases por nivel y dirección sin perder melodía; elegir una cumbre para el conjunto. |
| lesson-expression-012 | articulation | E007, E011, I010 | 3 | 4 | Combina melodía ligada y base breve con duraciones independientes; elegir conexión sin alargar la izquierda. |
| lesson-expression-013 | space | E008, E011, M013, R010 | 4 | 8 | Retira relleno antes de una llegada para darle peso; elegir qué quitar manteniendo swing y armonía. |
| lesson-expression-014 | tension-release | E009, E011, E012, E013 | 4 | 8 | Ordena tensiones secundarias alrededor de una cumbre de ocho compases; elegir resolución sin sumar densidad. |
| lesson-expression-015 | form | E010, E012, E013, E014 | 5 | 8 | Organiza entrada, idea, respuesta y cierre en miniatura; decidir balance, respiración y señal final propios. |

**Salida de categoría:** interpretar una miniatura con jerarquía y forma reconocibles, usando recursos conocidos y dejando espacio. No se depende de detección automática de expresividad.

## Plan de producción accesible posterior

Priorizar cinco transformaciones futuras por lección: fijar base; comparar una modificación A/B; sostenerla en contexto; variar una elección limitada; transferir con menos ayudas. Es una pauta de diseño, no registros de `stages`. Mantener cuatro transformaciones cuando combinar y variar se resuelvan sin salto; no ampliar a seis para aumentar volumen.

La aplicación libre conservará un ejemplo reproducible de referencia de cuatro u ocho compases a dos manos, nunca una respuesta única. Primero reducir voces o ataques y después bajar tempo si hace falta; extensión y simplificación serán consejos salvo que se compongan variantes completas. Las decisiones de las tablas delimitan la autonomía, no exigen improvisar todos los parámetros simultáneamente.

Condiciones para musicalización: mano derecha con extensión simultánea máxima de octava, contando notas sostenidas; sin solapamientos de la misma altura MIDI entre roles. Son y bossa exigirán patrones de dos compases con ataques, duraciones y relación bajo–acordes explícitos; en son, además, orientación de clave 2–3. Estas comprobaciones quedan para fase C, no se dan por superadas con el diseño.

## Piloto reservado

**ID:** `lesson-rhythm-004`. **Destreza única:** `skill-rhythm-syncopation`. Dificultad 2; 20 minutos; pop. Requiere R002 y R003. La novedad es adelantar una llegada armónica a 4&, no reharmonizar ni coordinar un patrón estilístico avanzado.

Prever cinco transformaciones futuras dentro de cuatro compases de I–vi–ii–V: base regular; comparación de una llegada en uno frente a 4&; estabilización del cambio sin reataque en uno; elección de otra frontera interior; aplicación con menos indicaciones. Esta reserva no implementa etapas.

La alternativa tendrá arreglo y eventos propios sobre I–V–vi–IV, con idéntico objetivo y voicings sencillos. No será transposición de la principal. Mantener la primera entrada en beat 0; anticipar únicamente una frontera interior para no necesitar anacrusa negativa ni cola fuera del loop. La fase C deberá componer, validar y escuchar ambas versiones antes de aprobarlas.

## Cierre posterior de producción

Las referencias a composición futura de este documento describen la fase B histórica. La producción posterior está completa: 90 lecciones aprobadas, 400 etapas y 402 progresiones. Se repitió el cotejo de tres lecciones por skill con dificultad estrictamente creciente; diseño y 225 prerrequisitos originales intactos. Las decisiones y diferencias musicales se revisaron por lote y se registraron con huella. La auditoría y sus límites actuales están en `final-audit.md`; no se afirma escucha ni ejecución física.
