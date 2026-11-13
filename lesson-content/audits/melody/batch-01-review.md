verdict: approved

# Revisión musical independiente — melody, lote 01

## Dictamen vigente — ciclo 1

**Aprobado musicalmente para melody-001–003. M-B01-001…007 verificadas y resueltas; cero incidencias abiertas.** No constituye aprobación técnica ni autorización para producir 004+.

Se reparsearon completos los cinco JSON de `work/melody/` y los siete de `checks/`, inspeccionando todos los registros y las doce líneas temporales por inicio, duración, mano, rol, altura y velocidad. Conteo vigente: **3 lecciones, 12 etapas, 12 progresiones, 48 acordes, 143 notas**. Checks conserva 6 categorías, 30 skills y 90 fichas de diseño. Las cuatro entidades musicales coinciden exactamente entre work y checks; las tres fichas siguen siendo copias exactas del diseño aprobado y están presentes en checks.

`audit_delivery.musical_metrics` se repitió sobre las 12 progresiones: `findings: []`. Se comparó además la totalidad de alturas, ataques, duraciones, manos, roles y velocidades de M002 con la evidencia inicial: **MIDI musical intacto en sus cuatro etapas**, no solo conteos iguales. Hashes, exportación/inspección binaria MIDI, SQL y puerta técnica quedan al maestro en paralelo; no se afirman aquí. Sin escucha ni render. No se modificaron composición, scripts, checks ni diseño.

### Evidencia vigente de las doce etapas

Convención: `MIDI@inicio/duración`, negras desde cero; C4=60. Todas las notas derechas son `right/melody`, velocidad 76; izquierdas `left/bass`, velocidad 58. Todas las progresiones conservan cuatro compases 4/4, Do mayor y 72 BPM.

Plan armónico A (M001 y M003): C/I@0/4, Am/vi@4/4, F/IV@8/4, G/V@12/4. Plan B (M002): C/I@0/4, C/I@4/4, Am7/vi7@8/4, Am7/vi7@12/4. Los 48 eventos siguen completos y coherentes.

Izquierda M001, **en cada etapa**: [48,55]@0/4, [45,52]@4/4, [41,48]@8/4, [43,50]@12/4. Son raíz y quinta simultáneas, no bloques completos. Izquierda M002: 48@0/4, 48@4/4, 45@8/4, 45@12/4. Izquierda M003: 48@0/4, 45@4/4, 41@8/4, 43@12/4. La descripción de realización armónica parcial sigue siendo explícita.

En M002, célula P = 64@0/0.5, 67@1/0.5, 72@2/1; célula Q = misma célula con última altura 69. `P+4`, por ejemplo, desplaza todos sus ataques cuatro negras. La tabla, junto con esas izquierdas, cubre las **143 notas actuales: 64 izquierdas y 79 derechas**, sin omitir sostenimientos.

| Etapa | Derecha completa | Evidencia y juicio vigente |
|---|---|---|
| 001-01 | 67@0/1; 67@4/1; 67@8/1; 67@12/1 | A real: G4 repetido sobre cuatro bajos distintos. G es quinta de C y raíz de G; sobre Am y F produce color sin señalar por igual cada cambio. No se penaliza como error armónico: cumple el contraste pedagógico anunciado. |
| 001-02 | 64@0/1; 60@4/1; 65@8/1; 67@12/1 | B: tercera de C, tercera de Am, raíz de F y raíz de G. Ataques, duraciones, bajo y armonía iguales a A; cambio exclusivo de selección melódica, con G final común. Contraste ejecutable. |
| 001-03 | 64@0/1; 60@4/1; 65@8/1; 71@12/1 | Único delta respecto de B: 67→71 en beat 12. B4 es tercera real de G. Ya no promete una cadena de terceras inexistente: compara dos destinos acordales válidos. |
| 001-04 | 72@0/1; 64@4/1; 69@8/1; 74@12/1 | Cuatro destinos efectivamente nuevos: raíz de C, quinta de Am, tercera de F, quinta de G. Se pide cantar y elegir objetivos propios; referencia no única. |
| 002-01 | P; P+4 | Célula íntegra de tres notas, dos breves y una larga; pausas conservadas. Criterios y simplificación exigen tres notas y aire, no una sola nota de apoyo. |
| 002-02 | P; P+4; P+8; P+12 | Repeticiones añadidas en compases 3 y 4; título, tarea y delta ahora localizan exactamente esa extensión. Célula válida sobre Am7; se preservan ritmo, contorno y pausa. |
| 002-03 | P; P+4; Q+8; Q+12 | Solo cambia última altura en las dos respuestas, 72→69; primeras dos alturas, ritmo y pausa intactos. Texto describe adaptación, sin presentar C como nota errónea. |
| 002-04 | P; P+4; Q+8; Q+12; 67@15.5/0.5 | Conserva célula reconocible y agrega cola G, séptima de Am7. La pausa anterior existe y la libertad textual sigue explícita. Hints no eliminan las tres notas del motivo. |
| 003-01 | 64@0/3.5; 60@4/3.5; 57@8/1; 59@12/1 | Apoyos E4/C4/A3/B3 acordales sobre C/Am/F/G. Los dos primeros se sostienen hasta las posiciones débiles donde se insertarán pasos: comparación limpia, con 7 beats de aire. |
| 003-02 | 64@0/3.5; 62@3.5/0.5; 60@4/3.5; 57@8/1; 59@12/1 | Única adición D4 en 3.5: E–D–C, tono descendente en entrada y salida; paso débil diatónico que resuelve en el apoyo de Am. D sobre C es disonancia contextual justificada. |
| 003-03 | 64@0/3.5; 62@3.5/0.5; 60@4/3.5; 59@7.5/0.5; 57@8/1; 59@12/1 | Conserva primera conexión y añade B3@7.5: C–B–A, semitono y tono diatónicos descendentes. B sobre Am resuelve a A, tercera de F. Sin cromatismo ni cerco. |
| 003-04 | 64@0/3.5; 60@4/3.5; 59@7.5/0.5; 57@8/1; 59@12/1 | Retira D@3.5; conserva solo segunda conexión C–B–A. Autonomía explícita al elegir una frontera con destino fijo; no añade bordaduras ni relleno. |

Tocabilidad: M001 exige como máximo dos notas izquierdas y siete semitonos simultáneos; M002/M003, una nota izquierda; derecha siempre monofónica. Sin colisiones, cruces ni alcances excesivos. El salto C5→E4 de M001-04 es de ocho semitonos y tiene tres negras de silencio para preparar la mano: cómodo a 72 BPM, no extensión sostenida. En M003 la línea baja hasta A3 pero queda sobre el bajo F2.

Silencio derecho por etapas: M001 12/12/12/12; M002 12/8/8/7.5; M003 7/6.5/6/6.5 negras. Hay respiración suficiente y la mayor duración de apoyos en M003 hace audible el paso sin vacíos intermedios. Se conservan objetivos únicos, intros, cuatro compases y prerrequisitos aprobados: M001 H001/R002, M002 M001, M003 M001/R002. No hay plantilla musical genérica ni anticipación del cromatismo de lecciones futuras.

### Cierre comprobado de incidencias

| Incidencia histórica | Evidencia de resolución en ciclo 1 |
|---|---|
| M-B01-001 | M001-03 cambia únicamente G4→B4 al llegar a G; título, explicación, tarea y criterios describen esa elección acordal real. |
| M-B01-002 | M003 rehecha y propagada a sus cuatro etapas: apoyos E/C/A/B, paso E–D–C y segundo paso C–B–A; final selecciona solo este último. Criterios comprueban entrada y salida; desaparecieron F# y bordaduras. |
| M-B01-003 | M001-04 presenta cuatro objetivos nuevos 72/64/69/74, todos del acorde correspondiente; autonomía explícita. |
| M-B01-004 | Raíz y quinta presentes durante cuatro negras en cada compás de las cuatro etapas M001, en ambas copias. |
| M-B01-005 | M001-01 es A con 67 repetido; M001-02 es B con 64/60/65/67. Instrucciones permiten alternarlas sobre idéntico bajo y pulso. |
| M-B01-006 | M002-02 identifica compases 3 y 4 en título, explicación, tarea, delta y criterio; notas intactas. |
| M-B01-007 | Las cuatro etapas M002 tienen criterios/hints propios de tres notas, identidad y pausa; M003 comprueba parte débil y grados conjuntos. No se elimina la habilidad al simplificar. |

**Conclusión vigente:** siete incidencias históricas resueltas tras inspección, ninguna nueva. Aprobación musical del lote 01; falta la resolución técnica independiente del maestro. Única escritura: este reporte. No se revisó ni autorizó 004+.

---

# Histórico — revisión inicial (verdict: rejected, sustituido por ciclo 1)

Todo lo que sigue documenta el estado inicial de 140 notas, no el estado vigente. Se conservan observaciones, severidades e IDs para trazabilidad; los `status` del protocolo se actualizan a `resolved` según la evidencia anterior.

## Alcance y método

Lectura completa de `PIANO_LAB_CURRICULUM_SPEC.md`, skill `ponytail`, `curriculum/README.md`, diseño y cobertura de melody-001–003. Parseados íntegramente todos los JSON de `work/melody/` y `work/melody/checks/`; leído también `build.py`, sin ejecutarlo ni modificarlo. Inspección ordenada de cada nota por inicio, duración, mano, rol, altura y velocidad; no se juzgó a partir de un JSON truncado.

Conteos: **3 lecciones, 12 etapas, 12 progresiones primary, 48 acordes y 140 notas**. El snapshot contiene además el diseño global: 6 categorías, 30 skills y 90 lecciones, no 90 lecciones compuestas. Las cuatro entidades musicales coinciden exactamente entre partición y snapshot; las tres fichas coinciden con el diseño aprobado y están presentes en checks.

`audit_delivery.musical_metrics`: 12 progresiones analizadas, `findings: []`. Esto acredita ausencia de avisos por alcance simultáneo, más de cinco notas, colisiones de tecla y ejemplos consecutivos idénticos; **no acredita el contenido pedagógico**. La puerta técnica, hashes y validación MIDI corresponden al maestro en paralelo; aquí no se repiten ni se presuponen aprobados. No hubo reproducción, render ni escucha; no se exportó MIDI porque la línea temporal completa permite comprobar los problemas encontrados.

## Convenciones y acompañamiento común

Todos los ejemplos: Do mayor, 4/4, cuatro compases, 16 negras, 72 BPM, loop. Notación de la tabla: `altura@inicio/duración`, en negras desde cero; C4 = MIDI 60. Todas las notas derechas son `right/melody`, velocidad 76. Todas las izquierdas son `left/bass`, velocidad 58, duración 4. No existen notas `harmony` ni `ornament`.

- **Plan A**, todas las etapas de 001 y 003: C/I@0/4, Am/vi@4/4, F/IV@8/4, G/V@12/4. Bajo íntegro: C3@0/4, A2@4/4, F2@8/4, G2@12/4.
- **Plan B**, todas las etapas de 002: C/I@0/4, C/I@4/4, Am7/vi7@8/4, Am7/vi7@12/4. Bajo íntegro: C3@0/4, C3@4/4, A2@8/4, A2@12/4.

Estos dos planes especifican los **48 registros armónicos y las 48 notas izquierdas**; la tabla especifica las **92 notas derechas** restantes. Se inspeccionaron también sus IDs y metadatos originales. Los textos declaran explícitamente realización parcial bajo + melodía: no se exige completar terceras/séptimas como si fueran bloques. Am7 en 002 es legítimo: G y C de la melodía aportan séptima y tercera sobre A, aunque no se sostengan todas las voces simultáneamente.

## Evidencia de las doce etapas

Los sufijos de la primera columna corresponden a `stage-melody-<sufijo>` y a su `prog-melody-<sufijo>-primary`.

| Etapa / plan | Línea derecha completa | Evaluación musical y transformación |
|---|---|---|
| 001-01 / A | E4@0/1; C4@4/1; F4@8/1; G4@12/1 | Cuatro destinos reales: tercera de C, tercera de Am, fundamentales de F y G. 12 beats de silencio derecho. Base clara, pero no realiza quinta izquierda ni contraste de nota indiferente anunciado en intro. |
| 001-02 / A | E4@0/1; E4@3/0.5; C4@4/1; F4@8/1; G4@12/1 | Única adición verificable: E4 en beat 3. E es nota común C/Am, válida; se apaga en 3.5 y no es el C del apoyo siguiente. No se oye una versión de «no-llegada»; el título sobrepromete el contraste. |
| 001-03 / A | E4@0/1; E4@3/0.5; C4@4/1; E4@7/0.5; F4@8/1; A4@11/0.5; G4@12/1 | Añade E@7 y A@11. E es quinta del Am vigente y A tercera del F vigente; no son terceras de las llegadas F/G. Los apoyos F y G permanecen fundamentales. E→F y A→G son enlaces plausibles, pero no ejemplifican lo explicado. |
| 001-04 / A | E4@0/1; E4@3/0.5; C4@4/1; E4@7/0.5; F4@8/1; A4@11/0.5; G4@12/1; B4@15/0.5 | Añade B, tercera del G vigente. Mantiene exactamente los cuatro destinos E/C/F/G; contradice «objetivos distintos y cercanos». Autonomía textual explícita, ejemplo no único, pero cambio anunciado falso. |
| 002-01 / B | E4@0/0.5; G4@1/0.5; C5@2/1; E4@4/0.5; G4@5/0.5; C5@6/1 | Motivo de tres notas ascendente, duraciones 0.5/0.5/1 y pausa; dos presentaciones exactas. La derecha calla de 7 a 16: espacio deliberado para completar una respuesta, no registros ausentes. |
| 002-02 / B | E4@0/0.5; G4@1/0.5; C5@2/1; E4@4/0.5; G4@5/0.5; C5@6/1; E4@8/0.5; G4@9/0.5; C5@10/1; E4@12/0.5; G4@13/0.5; C5@14/1 | Añade dos repeticiones exactas en compases 3 y 4, sobre Am7. Todas las alturas pertenecen al plan. El texto sitúa la repetición nueva en los dos primeros compases, donde ya existía. |
| 002-03 / B | E4@0/0.5; G4@1/0.5; C5@2/1; E4@4/0.5; G4@5/0.5; C5@6/1; E4@8/0.5; G4@9/0.5; A4@10/1; E4@12/0.5; G4@13/0.5; A4@14/1 | Solo C5→A4 en la última nota de ambas respuestas. Conserva primeras dos alturas, ataques, duraciones y contorno ascendente. Variación reconocible y acordal. C ya encajaba en Am7: cambio de color/énfasis, no reparación de un error. |
| 002-04 / B | E4@0/0.5; G4@1/0.5; C5@2/1; E4@4/0.5; G4@5/0.5; C5@6/1; E4@8/0.5; G4@9/0.5; A4@10/1; E4@12/0.5; G4@13/0.5; A4@14/1; G4@15.5/0.5 | Añade cola G4, séptima de Am7, tras pausa de 0.5. Célula conservada; respuesta y final abierto válidos. Autonomía explícita y referencia concreta. |
| 003-01 / A | E4@0/1; A4@4/1; F4@8/1; G4@12/1 | Apoyos acordales y espacios claros, sin notas de paso. Salto E→A y A→F, enlace F→G; base pertinente para comparar conexiones. |
| 003-02 / A | E4@0/1; G4@3.5/0.5; A4@4/1; F4@8/1; G4@12/1 | G entra débil y resuelve conjuntamente a A; pero E→G es tercera menor. No es un paso conjunto entre ambos apoyos E/A. La resolución por sí sola no demuestra el objetivo completo. |
| 003-03 / A | E4@0/1; G4@3.5/0.5; A4@4/1; G4@7.5/0.5; F4@8/1; F#4@11.5/0.5; G4@12/1 | A–G–F sí es paso diatónico completo, dos tonos descendentes. F–F#–G es conexión cromática bien resuelta, no error por disonancia, pero no es el «mismo principio» diatónico anunciado ni preparado. Persiste E–G–A. |
| 003-04 / A | E4@0/1; G4@3.5/0.5; A4@4/1; G4@7.5/0.5; F4@8/1; F#4@11.5/0.5; G4@12/1; F#4@14.5/0.5; G4@15/0.5 | Conserva conexiones previas y añade G–F#–G: bordadura cromática inferior, no paso entre dos apoyos distintos. Resolución local correcta, pero adelanta otra habilidad sin explicación. Autonomía verbal sí existe; el ejemplo no se limita a elegir un paso con destino fijo. |

## Juicio transversal

La textura es accesible y deliberadamente escasa: una nota simultánea por mano, sin cruces ni colisiones, izquierda F2–C3 (A2–C3 en 002), derecha C4–C5. Saltos izquierdos máximos 4 semitonos en A y 3 en B; derecha como máximo 8 semitonos en 002, separados por silencio entre células. No se exige mantener una extensión manual de octava: no hay acordes simultáneos. Velocidades 58/76 favorecen la línea. A 72 BPM, no se detecta dificultad motora impropia del nivel 1.

Silencio derecho por etapa: 001 = 12/11.5/10.5/10 beats; 002 = 12/8/8/7.5; 003 = 12/11.5/10.5/9.5. Hay aire real, no relleno continuo. El loop V→I queda abierto pero musicalmente razonable; no se promete cadencia cerrada dentro del cuarto compás.

Las fichas conservan prerrequisitos exactos: 001 H001/R002; 002 M001; 003 M001/R002. Cuatro compases, dificultades, objetivos e intros corresponden al diseño. No hay exigencia de independencia avanzada. Sin embargo, el cromatismo de 003 adelanta recursos de aproximación que la cobertura reserva después (especialmente M009), y 001-03 promete terceras, recurso cuyo desarrollo específico se reserva a M006. Lo bloqueante no es usar una tercera o un cromatismo: es enseñar otra transformación y afirmar que se ha realizado la solicitada.

No es una plantilla musical única: 001 establece destinos, 002 conserva una célula concreta, 003 añade enlaces. Sí hay plantilla textual común en tareas, criterios y consejos, que impide comprobar adecuadamente motivo y resolución. Las etapas finales declaran libertad y ejemplo no único; ello no exime de que `changeFromPrevious` describa las notas reales.

## Incidencias — protocolo 8.3

Dos incidencias major bloquean aprobación. Las cinco minor se registran sin bloquear por sí solas. No se reparó ninguna composición, ficha ni script.

```json
[
  {
    "issueId": "M-B01-001",
    "severity": "major",
    "entityType": "stage",
    "entityId": "stage-melody-001-03",
    "location": "explanationMd/title; prog-melody-001-03-primary, beats 7, 8, 11 y 12",
    "expected": "Las terceras y destinos anunciados deben ser identificables respecto del acorde que se está señalando, manteniendo el objetivo de notas acordales.",
    "observed": "Se añaden E4@7 sobre Am y A4@11 sobre F; solo A es tercera del acorde vigente. Los apoyos F4@8 y G4@12 siguen siendo fundamentales, no terceras de F y G. Tampoco E y A son terceras de esos acordes de llegada.",
    "correction": "Alinear explicación y transformación MIDI con destinos acordales reales; no presentar enlaces válidos como terceras que no son ni anticipar sin necesidad la especialización de M006.",
    "owner": "composer-melody",
    "status": "resolved"
  },
  {
    "issueId": "M-B01-002",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-melody-003",
    "location": "stages 02–04; notas 0116, 0125–0127, 0136–0140 de sus progresiones respectivas",
    "expected": "Demostrar un paso diatónico débil entre dos apoyos, con movimiento conjunto de entrada y salida, conservar destinos y sostener ese objetivo en combinación y autonomía.",
    "observed": "E4@0–G4@3.5–A4@4 salta tercera al entrar en G: solo la salida es conjunta. A–G–F sí cumple. F–F#–G en 03 y 04 es cromático sin explicación; G–F#–G añadido en 04 es bordadura, no paso. Son gestos musicalmente resolubles, pero el ejemplo inicial no enseña el objetivo íntegro y las etapas siguientes mezclan recursos no preparados.",
    "correction": "Recomponer las conexiones afectadas conservando apoyos pertinentes para una entrada y salida conjuntas y el objetivo diatónico; retirar o reservar los gestos de otra habilidad. Actualizar sus dependientes y describir exactamente cada transformación, sin tratar toda nota ajena como error.",
    "owner": "composer-melody",
    "status": "resolved"
  },
  {
    "issueId": "M-B01-003",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-melody-001-04",
    "location": "changeFromPrevious; prog-melody-001-04-primary, beats 0, 4, 8, 12 y 15",
    "expected": "La referencia de autonomía debe mostrar los objetivos distintos anunciados o describir con precisión el cambio que sí realiza.",
    "observed": "Los destinos E4/C4/F4/G4 son idénticos a 03. Solo añade B4@15/0.5, tercera del G vigente. La invitación a elegir objetivos propios es válida, pero el delta declarado no existe.",
    "correction": "Alinear el delta textual con la referencia o realizar una elección distinta de destinos sin perder el objetivo de la lección.",
    "owner": "composer-melody",
    "status": "resolved"
  },
  {
    "issueId": "M-B01-004",
    "severity": "minor",
    "entityType": "lesson",
    "entityId": "lesson-melody-001",
    "location": "introMd frente a las cuatro progresiones de la lección",
    "expected": "La referencia debe concordar con la textura anunciada: fundamental y quinta cómodas, o una reducción explícita a fundamental sola.",
    "observed": "Cada compás tiene únicamente una fundamental izquierda de cuatro beats; no hay quintas. La declaración de plan armónico parcial es correcta, pero no explica esta diferencia concreta con la intro congelada.",
    "correction": "Hacer explícita en las etapas la reducción elegida respecto de la intro o realizar la textura prometida, sin fingir bloques completos ni modificar unilateralmente el diseño aprobado.",
    "owner": "composer-melody",
    "status": "resolved"
  },
  {
    "issueId": "M-B01-005",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-melody-001-02",
    "location": "title/explanationMd y comparación con stage-melody-001-01",
    "expected": "El contraste llegada/no-llegada anunciado por título e intro debe ser ejecutable con instrucciones concretas o ejemplos que realmente lo muestren.",
    "observed": "Ambas etapas usan los mismos cuatro apoyos acordales. La única diferencia es repetir E4@3 antes de C4@4; E es común a C y Am. No se proporciona la nota indiferente ni una instrucción concreta para producir y comparar la no-llegada.",
    "correction": "Dar una comparación A/B ejecutable dentro de la etapa o ajustar el alcance del contraste anunciado sin confundir repetición preparatoria con una demostración de no-llegada.",
    "owner": "composer-melody",
    "status": "resolved"
  },
  {
    "issueId": "M-B01-006",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-melody-002-02",
    "location": "changeFromPrevious; prog-melody-002-02-primary, compases 3 y 4",
    "expected": "Nombrar la repetición nueva en los compases donde aparece.",
    "observed": "El texto sitúa el cambio en los dos primeros compases, que ya contenían el motivo exacto en 01; las seis notas nuevas están en beats 8/9/10 y 12/13/14.",
    "correction": "Describir la extensión de la repetición a los compases 3 y 4 sobre Am7, conservando el mismo motivo.",
    "owner": "composer-melody",
    "status": "resolved"
  },
  {
    "issueId": "M-B01-007",
    "severity": "minor",
    "entityType": "lesson",
    "entityId": "lesson-melody-002",
    "location": "successCriteria/simplifyHint de sus cuatro etapas; patrón textual compartido con 001 y 003",
    "expected": "Autoevaluar específicamente ritmo, tres notas, contorno reconocible y pausa; simplificar sin borrar la habilidad principal.",
    "observed": "Se repiten criterios genéricos de cantar, apoyo armónico y balance. El consejo de tocar solo la nota de apoyo de cada compás elimina el motivo de tres notas. En 003 los mismos criterios tampoco exigen comprobar entrada y salida conjuntas del paso.",
    "correction": "Dar criterios y consejos específicos para motivo y paso; preservar la célula al simplificar 002 y comprobar las dos conexiones del paso en 003.",
    "owner": "composer-melody",
    "status": "resolved"
  }
]
```

## Conclusión y límites

**Rechazado musicalmente:** el lote es tocable, tiene espacio y un motivo reconocible, pero no demuestra fielmente dos transformaciones centrales. Debe volver a `composer-melody`; no se autorreparó ni se aprobó por métricas limpias.

Única escritura: este reporte. No se verificó audio, exportación MIDI, SQL ni hashes; corresponden a las puertas técnicas separadas. Tras corrección, revisar nuevamente los registros afectados y sus etapas dependientes antes de aprobación del maestro.
