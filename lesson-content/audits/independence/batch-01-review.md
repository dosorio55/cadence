verdict: approved

# Revisión actual — cierre textual de I-B01-008

**Aprobación musical del lote; no sustituye la aprobación técnica/global del maestro.** Las ocho incidencias I-B01-001–008 están verificadas y resueltas: **sin incidencias musicales pendientes**. Se conserva debajo la revisión inicial como evidencia histórica, no como descripción del estado actual.

Verificación final focalizada: el texto de `stage-independence-001-05` coincide entre trabajo y snapshot y ahora describe B en beats globales **0, 2, 8 y 10**, duración **1** por respuesta, compases pares vacíos y dos blancas LH por compás. Declara explícitamente la segunda respuesta añadida en offset 2 respecto de 04 y la elección autónoma posterior de qué respuesta omitir. Los eventos reales son RH `(0,1,67), (2,1,67), (8,1,57), (10,1,57)`; las ocho blancas LH coinciden con 04. Se verificaron las 278 notas de trabajo contra snapshot y contra los 15 MIDI conservados del ciclo 1: correspondencia exacta de inicios/finales, alturas y velocidades, sin reexportar ni modificar archivos MIDI. No se revisaron lecciones 004 en adelante.

## Evidencia actual

Reparseados íntegramente los cinco arrays de `work/independence/` y los siete arrays de `checks/`; releídos todos los textos de las 15 etapas y progresiones y las tres fichas. Trabajo actual: **3 lecciones, 15 etapas, 15 primary, 45 chord-events y 278 note-events**. Snapshot: 6 categorías, 30 skills, 90 fichas, y esas mismas 15 etapas/15 progresiones/45 acordes/278 notas. Los cinco conjuntos de trabajo coinciden exactamente con sus registros del snapshot; las tres fichas siguen idénticas al diseño en `data/lessons.json`.

Validación batch: **0 errores**. `musical_metrics`: 15 progresiones, **0 findings**. Se ejecutaron asserts sobre las invariantes LH, cambios aislados RH, retirada de pares, desplazamiento de ataques, duración de shells y omisión global 7. Exportación y lectura binaria de **todos los 15 MIDI actuales**, con comparación exacta de las 278 notas, velocidades e inicios/finales: conforme. Archivos: `/tmp/independence-b01-cycle1-e7bmq20d/<progressionId>.mid`. PPQ 960, 4/4, tempo 833333 µs/negra y cierre tick 15360 en todos. No se escuchó ni renderizó audio; tampoco se probó físicamente en piano. Hashes/congelación y auditoría técnica general permanecen a cargo del maestro en paralelo.

## Timeline actual completa y agrupada

Cada fila corresponde a `stage-independence-LLL-EE` y `prog-independence-LLL-EE-primary`. Compases comienzan en **b=0,4,8,12**. Los patrones locales se aplican a cada b, salvo restricción explícita de compases impares. `offset:duración` está en negras; inicio global = b + offset. Listas de cuatro alturas corresponden en orden a los cuatro compases. Parejas entre corchetes son simultáneas. LH: `hand=left, role=bass, velocity=72`; RH: `hand=right, velocity=64, role=melody` en I001/I003 y `role=harmony` en I002. No hay eventos either/ornament.

**R=[48,45,41,43]** (C3,A2,F2,G2), **Q=[55,52,48,50]** (G3,E3,C3,D3), **A=[64,60,64,59]** (E4,C4,E4,B3), **B=[67,64,57,62]** (G4,E4,A3,D4), **S=[[64,71],[60,67],[57,64],[59,65]]** (tercera/séptima de los cuatro acordes).

I001/I002: en cada progresión hay cuatro eventos propios `(inicio,duración,símbolo,función)`: `(0,4,Cmaj7,Imaj7)`, `(4,4,Am7,vi7)`, `(8,4,Fmaj7,IVmaj7)`, `(12,4,G7,V7)`. I003: cada progresión tiene **un solo evento `(0,16,Cmaj7,Imaj7)`**. Así se enumeran los **45 acordes**, no los 60 históricos.

Máximos simultáneos: `notas/alcance en semitonos`, incluyendo sostenidas. Todas las progresiones: cuatro compases, Do mayor, pop, 72 BPM.

| Etapa | LH+RH=notas | LH: offsets:duración, alturas | RH: offsets:duración, alturas | Máx. LH; RH | Verificación actual |
|---|---:|---|---|---|---|
| 001-01 | 8+4=12 | 0:2 y 2:2, R | 0:2, A | 1/0; 1/0 | Base y segunda blanca bajo silencio RH. |
| 001-02 | 8+4=12 | 0:2 y 2:2, R | 0:1, A | 1/0; 1/0 | Solo acorta RH; conserva alturas e inicios. |
| 001-03 | 8+2=10 | 0:2 y 2:2, R | Solo compases 1/3, 0:1, A | 1/0; 1/0 | Pares completos sin RH. |
| 001-04 | 8+2=10 | 0:2 y 2:2, R | Solo compases 1/3, 0:1, B | 1/0; 1/0 | Solo cambia altura RH en impares. |
| 001-05 | 8+4=12 | 0:2 y 2:2, R | Solo compases 1/3, 0:1 y 2:1, B | 1/0; 1/0 | Ref. con ataques globales 0/2/8/10; pares vacíos; texto conforme, 008 resolved. |
| 002-01 | 8+16=24 | 0:2 y 2:2, R | 0:1 y 2:1, S | 1/0; 2/7 | Base simultánea real y bajo sostenido. |
| 002-02 | 8+16=24 | 0:2 y 2:2, R | 1:1 y 3:1, S | 1/0; 2/7 | Solo desplaza RH a tiempos 2/4. |
| 002-03 | 8+16=24 | 0:2 y 2:2, R | 1:0.5 y 3:0.5, S | 1/0; 2/7 | Solo acorta RH; LH nunca se recorta. |
| 002-04 | 8+16=24 | 0:2 R y 2:2 Q | 1:0.5 y 3:0.5, S | 1/0; 2/7 | Solo segunda altura LH cambia a quinta; shells intactos. |
| 002-05 | 8+14=22 | 0:2 R y 2:2 Q | Igual 04, excepto eliminar pareja S de inicio global 7 | 1/0; 2/7 | Solo omite un shell; LH idéntica a 04. |
| 003-01 | 16+4=20 | 0:1 48, 1:1 55, 2:1 48, 3:1 55 | 0:4, 64 | 1/0; 1/0 | Ostinato fijo bajo redonda E4. |
| 003-02 | 16+4=20 | 0:1 48, 1:1 55, 2:1 48, 3:1 55 | 0:1, 64 | 1/0; 1/0 | Solo duración RH 4→1. |
| 003-03 | 16+4=20 | 0:1 48, 1:1 55, 2:1 48, 3:1 55 | 0:2, 64 | 1/0; 1/0 | Solo duración RH 1→2; pausa 2–4. |
| 003-04 | 16+4=20 | 0:1 48, 1:1 55, 2:1 48, 3:1 55 | 0:2, 67 | 1/0; 1/0 | Solo altura RH E4→G4. |
| 003-05 | 16+8=24 | 0:1 48, 1:1 55, 2:1 48, 3:1 55 | 0:2 67 y 3:1 64 | 1/0; 1/0 | Referencia de respuesta y silencio 2–3; LH intacta. |

Esta notación expande exactamente las **278 notas actuales**, sin truncar eventos, duraciones, manos, roles, pitches ni compases repetidos.

## Cierre verificado de incidencias históricas

| ID histórico | Estado actual | Evidencia de resolución, ciclo 1 |
|---|---|---|
| I-B01-001 | resolved | 001-02 mantiene A=[64,60,64,59] y solo cambia duración 2→1; texto ya dice esto. |
| I-B01-002 | resolved | 001-03 tiene únicamente RH global 0/8; 04 conserva esos inicios/duraciones y cambia solo alturas a 67/57; 05 mantiene pares vacíos. Ocho blancas LH idénticas en las cinco etapas. |
| I-B01-003 | resolved | 002-01 tiene dos blancas LH completas por compás y shells simultáneos en offsets 0/2; tarea/base ya corresponden. 02 desplaza RH a 1/3 sin recortar LH. |
| I-B01-004 | resolved | 002-04 conserva exactamente RH de 03 (S, offsets 1/3, duración 0.5); solo segunda nota LH pasa de R a Q. 05 mantiene ese bajo y omite únicamente el shell global 7. |
| I-B01-005 | resolved | 003-01/02/03 usan siempre RH 64 y los mismos inicios, con duración 4/1/2; 04 cambia solo a 67. |
| I-B01-006 | resolved | Las cinco progresiones 003 usan un único Cmaj7 de 16 negras; LH idéntica 48/55 a negras durante las 16 posiciones. |
| I-B01-007 | resolved | Base 002-01 simultánea verificable frente a alternancia de 02; introducción y ejecución corresponden. |
| I-B01-008 | resolved | Verificación textual final: RH B global 0/2/8/10, duración 1; pares vacíos y LH intacta. Se declara segunda respuesta añadida respecto de 04 y decisión autónoma de omitir. |

**Independencia y tocabilidad:** 001 conserva blancas durante silencio derecho, incluyendo compases enteros; 002 pasa de control simultáneo a alternancia con bajo sostenido durante cada shell; 003 sostiene o libera RH sin detener la célula LH. La base simultánea de 002 es un control A/B, no falsa independencia presentada como resultado final. Máximo una nota LH y dos RH; alcance máximo RH de siete semitonos contando sostenidas, sin alturas MIDI solapadas, tercera mano ni necesidad de pedal. Cada lección mantiene una habilidad principal, dificultad 1, cuatro compases y progresión rastreable con retiro final de decisiones prescritas. Hints y tareas corresponden en lo sustancial a los patrones actuales.

**Cmaj7 parcial en 003:** aceptado sin exigir C triad/I ni añadir si. El texto declara explícitamente raíz–quinta LH y una tercera/melodía RH, no un bloque completo de séptima; `role=melody` lo confirma. C/E/G y luego C/G son realizaciones parciales compatibles con el plan Cmaj7, aunque no bastan por sí solas para distinguirlo auditivamente de C mayor. Esa limitación no contradice el objetivo de ostinato ni promete entrenar reconocimiento de séptimas. La regla de comprobar tercera/séptima de bloques/shells sí se exige en 002 y se cumple en sus cuatro shells S. No corresponde abrir incidencia por una séptima no realizada en esta textura explícitamente parcial.

**Detalle menor resuelto:** 001-05 ya nombra ambas respuestas por compás impar y explica la ampliación respecto de 04; descripción, tarea y criterios corresponden al MIDI. El diagnóstico original de 008 se conserva debajo como histórico, con estado actualizado tras verificarlo.

### Incidencia I-B01-008 resuelta — protocolo 8.3

```json
[
  {
    "issueId": "I-B01-008",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-independence-001-05",
    "location": "explanationMd/changeFromPrevious frente a notas RH de startBeat 2 y 10",
    "expected": "Que la descripción de la referencia mencione sus dos respuestas por compás impar y su diferencia con 04.",
    "observed": "El texto describe B al inicio de 1 y 3 durante una negra y libertad para omitir, pero el MIDI también reataca B en offsets locales 2 de ambos compases (globales 2 y 10). Pares y LH sí permanecen correctos.",
    "correction": "Precisar las entradas y la decisión autónoma del ejemplo 0/2 en impares, conservando pares vacíos y blancas LH; no requiere recomponer el bajo.",
    "owner": "composer-independence",
    "status": "resolved"
  }
]
```

Solo se actualizó este reporte. Aprobación musical sin incidencias pendientes; resolución técnica/hashes y aprobación global corresponden al maestro. No se atribuye escucha ni prueba instrumental a la inspección MIDI.

---

# Revisión inicial — histórica (verdict entonces: rejected)

Los conteos, fallos y conclusión siguientes corresponden al estado anterior al ciclo 1. Sus siete incidencias conservan el diagnóstico original y ahora se marcan resolved únicamente tras la comprobación anterior.

# Independencia — revisión musical independiente, lote 01

## Alcance y evidencia

Leídos completos `PIANO_LAB_CURRICULUM_SPEC.md`, skill `ponytail`, `curriculum/README.md`, mapa de cobertura y fichas de diseño I001–I003; leídos los textos de las 15 etapas y progresiones. Parseados íntegramente los cinco arrays de `work/independence/` y los siete del snapshot `checks/`, sin muestreo de acordes ni notas. Revisión sin subagentes, sin modificar contenido ni scripts.

Conteos reales de trabajo: **3 lecciones, 15 etapas, 15 progresiones primary, 60 eventos armónicos y 280 notas**. Snapshot: 6 categorías, 30 skills y 90 fichas de diseño, pero solamente esas 15 etapas/progresiones, 60 acordes y 280 notas compuestas. Todos los registros de trabajo coinciden exactamente por ID y contenido con su contraparte del snapshot; las tres lecciones coinciden con `data/lessons.json`.

Validación batch del snapshot: **0 errores**. `audit_delivery.musical_metrics`: 15 progresiones analizadas, **0 findings**. Esto no detecta las contradicciones musicales indicadas abajo.

Exportadas e inspeccionadas binariamente **las 15 progresiones**, sin selección aleatoria, en `/tmp/independence-b01-review-fgye4w12/`, archivos `<progressionId>.mid`. Comparación exhaustiva de note-on, note-off, alturas y velocidades contra JSON: conforme en las 280 notas. Cada archivo tiene PPQ 960, tempo 833333 µs/negra, 4/4 y cierre en tick 15360 (16 negras). No se escuchó ni renderizó audio: la valoración de independencia audible se fundamenta en tiempos, duraciones, registros y contexto armónico, no en una escucha simulada. Hashes de congelación y auditoría técnica general quedan al maestro, que los trabaja en paralelo; no se presentan como verificados aquí.

## Timeline completa, agrupada y sin omisiones

Notación comprimida **sin pérdida**: cada fila representa una etapa `stage-independence-LLL-EE` y su única `prog-independence-LLL-EE-primary`. Los cuatro compases comienzan en **b = 0, 4, 8, 12**. Cada patrón se aplica a los cuatro valores de b; las listas de cuatro alturas corresponden, en orden, a esos compases. `offset:duración` usa negras desde el inicio local; sumar b para obtener `startBeat`. Los corchetes de una pareja significan notas simultáneas, no sucesivas. Todos los eventos LH tienen `hand=left, role=bass, velocity=72`; RH tiene `hand=right, velocity=64`, `role=melody` en I001/I003 y `role=harmony` en I002. No hay eventos `either` ni `ornament`.

Plan armónico idéntico, explícito en **cada una de las 15 progresiones**, con cuatro eventos propios por ID:

| Inicio global | Duración | Símbolo | Función |
|---:|---:|---|---|
| 0 | 4 | Cmaj7 | Imaj7 |
| 4 | 4 | Am7 | vi7 |
| 8 | 4 | Fmaj7 | IVmaj7 |
| 12 | 4 | G7 | V7 |

Abreviaturas de alturas MIDI:

- **R** = [48,45,41,43] = C3,A2,F2,G2, fundamentales por compás.
- **Q** = [55,52,48,50] = G3,E3,C3,D3, quintas correspondientes.
- **A** = [64,60,64,59] = E4,C4,E4,B3.
- **B** = [67,64,57,62] = G4,E4,A3,D4.
- **C** = [71,57,60,65] = B4,A3,C4,F4.
- **S** = [[64,71],[60,67],[57,64],[59,65]] = shells tercera/séptima de cada acorde.

Máximos simultáneos en la tabla: `número de notas / alcance en semitonos`, contando todas las sostenidas, no solamente ataques. Cada fila tiene cuatro acordes, cuatro compases, 72 BPM, Do mayor y estilo pop.

| Etapa | Notas LH+RH=total | LH: offsets:duración, alturas | RH: offsets:duración, alturas | Máx. LH; RH | Dictamen musical |
|---|---:|---|---|---|---|
| 001-01 | 8+4=12 | 0:2 y 2:2, R | 0:2, A | 1/0; 1/0 | Bajo continúa en segunda mitad; ya existe silencio derecho 2–4. |
| 001-02 | 8+4=12 | 0:2 y 2:2, R | 0:1, B | 1/0; 1/0 | Aire real 1–4, no nueva retirada 2–4; también cambia altura. |
| 001-03 | 8+4=12 | 0:2 y 2:2, R | 0:1, C | 1/0; 1/0 | RH toca los cuatro compases; contradice retirada de pares. |
| 001-04 | 8+4=12 | 0:2 y 2:2, R | 0:1, A | 1/0; 1/0 | Cambia únicamente altura frente al MIDI real de 03. |
| 001-05 | 8+8=16 | 0:2 y 2:2, R | 0:1 y 2:1, B | 1/0; 1/0 | Ejemplo con silencios 1–2 y 3–4; autonomía explícita. |
| 002-01 | 4+16=20 | 0:2, R | 1:1 y 3:1, S | 1/0; 2/7 | Bajo ausente durante segunda respuesta; tarea imposible tal como está. |
| 002-02 | 4+16=20 | 0:4, R | 1:1 y 3:1, S | 1/0; 2/7 | Ambas respuestas sobre bajo sostenido; duración corregida de forma audible. |
| 002-03 | 8+16=24 | 0:2 y 2:2, R | 1:1 y 3:1, S | 1/0; 2/7 | Bajo 1/3, acordes 2/4: alternancia y duración correctas. |
| 002-04 | 8+16=24 | 0:2 y 2:2, R | 1:1 y 3:1, [71,74] en los cuatro compases | 1/0; 2/3 | LH no cambia respecto de 03; RH sí, pierde shells y resolución. |
| 002-05 | 8+16=24 | 0:2 y 2:2, R | 1:0.5 y 3:0.5, S | 1/0; 2/7 | Alternancia intacta; ejemplo elige dos blancas y acordes más breves. |
| 003-01 | 16+4=20 | 0:1 R, 1:1 Q, 2:1 R, 3:1 Q | 0:4, A | 1/0; 1/0 | Negras bajo redondas: procesos distintos desde la base. |
| 003-02 | 16+4=20 | 0:1 R, 1:1 Q, 2:1 R, 3:1 Q | 0:1, B | 1/0; 1/0 | Ostinato intacto; acorta y cambia alturas derechas. |
| 003-03 | 16+4=20 | 0:1 R, 1:1 Q, 2:1 R, 3:1 Q | 0:2, C | 1/0; 1/0 | Dos negras de sostén y dos de pausa, también nuevas alturas. |
| 003-04 | 16+4=20 | 0:1 R, 1:1 Q, 2:1 R, 3:1 Q | 0:2, A | 1/0; 1/0 | Varía altura; duración igual a 03, bajo intacto. |
| 003-05 | 16+8=24 | 0:1 R, 1:1 Q, 2:1 R, 3:1 Q | 0:2 y 3:1, B | 1/0; 1/0 | Pausa derecha 2–3; célula intacta bajo respuesta añadida. |

La expansión de esta tabla enumera exactamente **280 notas y 60 acordes**, incluidos sus inicios, duraciones, mano, rol y alturas; no se omiten compases repetidos ni se usan puntos suspensivos.

## Juicio pedagógico y musical

**Independencia efectiva:** I001 conserva exactamente sus ocho blancas izquierdas entre las cinco versiones; hay ataques LH y sostén mientras RH calla. I002-02 demuestra bajo continuo bajo entradas derechas separadas; I002-03/04/05 conservan ataques 1/3 y duración de blanca sin levantar el bajo para tocar el acorde 2/4. I003 conserva exactamente sus 16 negras raíz–quinta en las cinco versiones, mientras RH sostiene o descansa. Aunque bastantes ataques derechos coinciden con alguno izquierdo, las manos no duplican siempre ataques y duraciones: no es falsa independencia por simple homorritmia. El fallo de I001-03 sigue siendo bloqueante porque falta precisamente la retirada de compases completos que pide el ejercicio.

**Habilidad y dificultad:** cada ficha tiene una sola `primarySkillId`, respectivamente bass-pulse, alternation y ostinatos; todas dificultad 1 y cuatro compases, sin alternativas por transposición. Los patrones son accesibles a 72 BPM: LH monofónica entre MIDI 41–55 y RH entre 57–74, sin saltos rápidos; shells de máximo siete semitonos. I003 introduce cuatro raíces armónicas pese al diseño textual de «un acorde», observado como desviación menor porque el patrón técnico sigue siendo elemental.

**Armonía contextual:** Cmaj7–Am7–Fmaj7–G7 es coherente en Do y retorna a C al repetir. Las melodías A/B/C son notas acordales; séptimas y quintas no se rechazan por omitir terceras en una textura declarada de bajo más una nota. S sí realiza terceras y séptimas de los cuatro acordes. En cambio, si–re fijo en I002-04 contiene novena en C, novena/undécima en Am y #11/13 en F; estos colores podrían ser válidos en otro arreglo, pero aquí sustituyen las guías sin explicación ni resolución y contradicen «solo cambia la altura izquierda». En G7 omiten ambas guías si/fa como pareja: solo queda si, sin fa. No se rechaza por cromatismo automático, sino por función, promesa didáctica y dificultad/contexto.

**Tocabilidad:** ningún solapamiento de la misma altura MIDI, ni entre manos/roles ni dentro de una mano. Off/on contiguos de una misma tecla son rearticulaciones válidas, no superposiciones. Máximo global tres teclas simultáneas: una LH y dos RH; no hay tercera mano oculta. Todos los alcances sostenidos quedan dentro de octava y por debajo de cinco notas por mano. No se requiere pedal para ejecutar las duraciones escritas.

**Ayudas/autonomía:** las últimas etapas permiten elecciones limitadas y mantienen MIDI de referencia; no se presentan como única respuesta. I001 permite escoger entradas/silencios; I002 escoger nota larga o blancas; I003 diseñar respuesta y pausa sin alterar ostinato. Los `simplifyHint` separan primero LH y bajan tempo, con coherencia general; los `extendHint` conservan la base y agregan silencio. No exigen pistas easy/hard inexistentes. La repetición literal de ayudas y criterios no bloquea por sí sola; deben, sin embargo, dejar de contradecir el ejemplo de I001-03 e I002-01. La comparación inicial de I002 no materializa los ataques juntos anunciados por su introducción, por lo que se registra una incidencia menor adicional.

## Incidencias — protocolo 8.3

**Histórico inicial: 3 major bloqueantes y 4 minor registradas, entonces abiertas.** Tras verificar el ciclo 1, las siete figuran resolved; sus diagnósticos originales se conservan a continuación. El revisor no autorreparó contenido.

```json
[
  {
    "issueId": "I-B01-001",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-independence-001-02",
    "location": "explanationMd/changeFromPrevious y notas RH, compases 1–4",
    "expected": "Comparación A/B que describa el cambio real y aísle la retirada derecha anunciada.",
    "observed": "01 ya calla en offsets 2–4. 02 pasa de duración 2 a 1, calla 1–4 y además cambia alturas A por B, aunque declara que ahora deja libre la segunda mitad.",
    "correction": "Alinear texto y ejemplo para que el nuevo silencio y cualquier cambio de altura sean rastreables, preservando las blancas LH.",
    "owner": "composer-independence",
    "status": "resolved"
  },
  {
    "issueId": "I-B01-002",
    "severity": "major",
    "entityType": "stage",
    "entityId": "stage-independence-001-03",
    "location": "compases 2 y 4, startBeat 4 y 12; task/changeFromPrevious",
    "expected": "Compases pares completos sin melodía, con LH continua; siguiente variación conserva ese contexto si solo cambia altura.",
    "observed": "Hay RH MIDI 57 en beat 4 y MIDI 65 en beat 12, duración 1. No existe ningún compás par vacío y la tarea dice no rellenarlos.",
    "correction": "Componer la retirada derecha prescrita y revisar la dependencia de 001-04, que promete cambiar solo altura; no tocar las blancas LH.",
    "owner": "composer-independence",
    "status": "resolved"
  },
  {
    "issueId": "I-B01-003",
    "severity": "major",
    "entityType": "stage",
    "entityId": "stage-independence-002-01",
    "location": "cada compás, offsets 2–4; explanationMd/task",
    "expected": "Que la tarea de escuchar el bajo debajo de ambas respuestas sea realizable, o que se identifique explícitamente una demostración de recorte erróneo.",
    "observed": "LH ataca solo en offset 0 con duración 2 y termina antes del acorde de offset 3. Una blanca no sostiene todo el compás y no hay bajo bajo la segunda respuesta.",
    "correction": "Alinear base, tarea y comparación con 002-02: sostener la duración necesaria o presentar explícitamente el recorte como contraejemplo, no como ejecución correcta.",
    "owner": "composer-independence",
    "status": "resolved"
  },
  {
    "issueId": "I-B01-004",
    "severity": "major",
    "entityType": "stage",
    "entityId": "stage-independence-002-04",
    "location": "changeFromPrevious y RH de los cuatro compases, offsets 1 y 3",
    "expected": "Solo modificar el bajo según la transformación anunciada, manteniendo respuestas armónicas coherentes con tercera y séptima.",
    "observed": "LH es idéntica a 002-03, incluidas alturas. RH cambia los cuatro shells por [71,74] fijo; introduce tensiones sin explicación y pierde terceras/séptimas del contexto, especialmente sobre Am7 y Fmaj7.",
    "correction": "Recomponer una variación rastreable conforme a lo anunciado y restaurar respuestas armónicas adecuadas al nivel, o rediseñar explícitamente la transformación dentro de la misma habilidad; revisar continuidad con 002-05.",
    "owner": "composer-independence",
    "status": "resolved"
  },
  {
    "issueId": "I-B01-005",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-independence-003-02",
    "location": "changeFromPrevious de 003-02 y 003-03; alturas RH de los cuatro compases",
    "expected": "Que la afirmación de cambiar solo duración sea comprobable respecto de la etapa anterior.",
    "observed": "003-02 acorta duración 4 a 1 pero también cambia A por B; 003-03 amplía 1 a 2 y cambia B por C sin explicitarlo. LH sí permanece idéntica.",
    "correction": "Conservar alturas al comparar duraciones o declarar y justificar ambos cambios en las etapas afectadas, sin alterar el ostinato.",
    "owner": "composer-independence",
    "status": "resolved"
  },
  {
    "issueId": "I-B01-006",
    "severity": "minor",
    "entityType": "lesson",
    "entityId": "lesson-independence-003",
    "location": "introMd frente a los 20 chord-events de sus cinco progresiones",
    "expected": "Cuatro compases sobre un acorde según el diseño textual aprobado, o una justificación autorizada de otra situación.",
    "observed": "Las cinco progresiones usan Cmaj7–Am7–Fmaj7–G7; el ostinato cambia raíz/quinta por compás. No es la situación sobre un solo acorde que anuncia la ficha.",
    "correction": "Ajustar la composición al diseño de un acorde o elevar al maestro la discrepancia para decisión explícita; no modificar unilateralmente la ficha congelada.",
    "owner": "composer-independence",
    "status": "resolved"
  },
  {
    "issueId": "I-B01-007",
    "severity": "minor",
    "entityType": "lesson",
    "entityId": "lesson-independence-002",
    "location": "introMd y etapa base 002-01",
    "expected": "Comparación entre ataques simultáneos y alternancia que pueda identificarse en el material de referencia anunciado.",
    "observed": "La introducción anuncia comparar todos los ataques simultáneos con alternancia, pero ninguna de las cinco versiones ofrece la base simultánea ni una instrucción concreta para construirla; todas tienen RH en 2/4 y LH en 1 o 1/3.",
    "correction": "Hacer explícita una comparación ejecutable sin añadir material innecesario, o ajustar con aprobación del maestro la promesa introductoria al recorrido realmente compuesto.",
    "owner": "composer-independence",
    "status": "resolved"
  }
]
```

## Cierre histórico inicial (superado por ciclo 1)

Lote rechazado por contradicciones entre instrucciones y notas, no por fallo de parsing, MIDI o alcance. La independencia básica existe y los patrones izquierdos de I001/I003 se conservan; falta corregir las tres incidencias major y volver a revisar sus dependencias. No se modificó ningún registro musical ni script. La inspección temporal y binaria no sustituye escucha humana ni prueba física en piano.
