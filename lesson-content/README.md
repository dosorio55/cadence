# Herramientas de currículo Piano Lab

**schemaVersion: 1.0.0** Contrato, herramientas y contenido curricular de Piano Lab. La aprobación de la entrega y sus límites se documentan en `audits/final-audit.md` cuando concluye la auditoría. Requiere Python 3.10 o superior y SQLite mediante `sqlite3` de Python. Los JSON Schemas son arrays estrictos de registros y el validador carga esos archivos desde `schemas/`; no mantiene una copia de runtime distinta.

## Organización

- `approved/`: JSON canónico aprobado; no se modifica durante trabajo de UI.
- `schemas/`: contrato JSON Schema.
- `tools/`: scripts, pruebas y dependencias Python.
- `drafts/`: particiones por categoría y sus checks de autoría.
- `archive/`: backups, snapshots de recuperación y herramientas históricas; no ejecutar sus scripts como herramientas activas.
- `audits/`: evidencia y registro de aprobación. Los documentos históricos conservan sus rutas originales para preservar sus huellas; los registros JSON usados por las herramientas apuntan a la estructura actual.
- `examples/`: referencias MIDI, piloto y SQLite.

## Instalación y comandos

Desde `lesson-content/`:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r tools/requirements.txt
.venv/bin/python -m unittest discover -s tools/tests -v
.venv/bin/python tools/scripts/curriculum.py --help
.venv/bin/python tools/scripts/curriculum.py validate --mode design --data RUTA
.venv/bin/python tools/scripts/curriculum.py validate --mode pilot --data RUTA
.venv/bin/python tools/scripts/curriculum.py validate --mode batch --data RUTA
.venv/bin/python tools/scripts/curriculum.py validate --mode global --data RUTA
.venv/bin/python tools/scripts/curriculum.py export-midi PROGRESSION_ID --data RUTA --output /tmp/ejemplo.mid
.venv/bin/python tools/scripts/curriculum.py import-sqlite --mode pilot --data RUTA --database /tmp/curriculum.sqlite
```

`import-sqlite` exige `--mode pilot|batch|global`, sin inferirlo del número de categorías. Los datos son siete arrays UTF-8, con nombres correspondientes a `schemas/*.schema.json`. `design` valida solo categories, skills y lessons. `design` solo lee y valida los tres archivos de diseño; ignora los archivos musicales. `pilot`/`batch` requieren el diseño completo: exactamente seis categorías, 4–6 skills por cada categoría y 15 lecciones numeradas 1–15 por categoría; permiten subconjuntos de etapas/progresiones/eventos. `global` exige además 3–6 etapas para cada una de las 90 lecciones (incluidas las que no tengan ninguna etapa). No se generan registros automáticamente.

## Contrato congelado para composición

Los esquemas fijan propiedades requeridas y rechazan las adicionales. Campos: categories `id,slug,name,description,order`; skills `id,categoryId,name,description,order`; lessons `id,primarySkillId,orderInCategory,title,difficulty,goal,introMd,prerequisiteLessonIds,targetMinutes,styleTags`; stages `id,lessonId,order,title,explanationMd,task,changeFromPrevious,successCriteria` y los opcionales `simplifyHint,extendHint`; progressions `id,stageId,kind,order,title,keyTonic,keyMode,style,bpm,timeSignature{numerator,denominator},totalBars,description,loopable`; chord-events `id,progressionId,order,symbol,function,startBeat,durationBeats`; note-events `id,progressionId,midi,startBeat,durationBeats,velocity,role,hand`. No se permiten valores `null`. IDs son strings estables; relaciones se expresan mediante IDs. Una etapa tiene exactamente una progresión `primary`; cada progresión requiere eventos de acorde y nota. Las órdenes de presentación empiezan en 1 y son correlativas donde aplica. Los eventos armónicos cubren el loop completo sin solapamientos ni huecos.

Los campos temporales usan beats de negra; BPM siempre significa negras por minuto. El total es `totalBars × numerator × (4 / denominator)`. Ataques y duraciones deben pertenecer al grid de 0.25 o múltiplos de 1/3 (tolerancia numérica), y permanecer dentro del loop. BPM permitido: 40–180. Las lecciones con 3 o 6 etapas requieren una justificación escrita en `introMd` (p. ej. “porque”, “criterio”, “justifica”), sin campo extra. El rango MIDI de piano 21–108 y cruces de registro/mano solo producen advertencias; nunca se prohíbe cromatismo.

Para cargar contenido: lesson → stages por `order` → progressions → chord-events y note-events de esa progression por `startBeat`. Exportación MIDI Standard format 0, una pista, PPQ 960, tempo, compás y end-of-track al final del loop; `export-midi` valida en modo `batch` antes de escribir y rechaza entradas inválidas; no requiere `mido`, sintetizador ni soundfont. Pruebas inspeccionan bytes/ticks, no renderizan audio.

Importación SQLite valida antes, activa claves foráneas y realiza DDL e inserciones en una transacción con UPSERT. Los prerrequisitos se guardan en `lesson_prerequisites(lesson_id, prerequisite_lesson_id, sort_order)`, con `PRIMARY KEY(lesson_id, prerequisite_lesson_id)` y `UNIQUE(lesson_id, sort_order)`; `sort_order` conserva desde 1 la posición en `prerequisiteLessonIds`. SQLite es el SQL de prueba por su disponibilidad en Python y sus transacciones, claves y UPSERT; el mapeo lógico a producción PostgreSQL/JSONB requiere adaptación explícita. No se hacen migraciones ni ALTER silenciosos: para este esquema de prueba usa una base SQLite nueva. Si encuentra el puente de una versión anterior sin `sort_order`, el importador aborta y revierte la transacción. Reimportar el mismo seed conserva exactamente su contenido; UPSERT no elimina registros de versiones anteriores que hayan desaparecido del JSON. Para verificar una versión nueva sin residuos, importar a una base vacía.

## Particiones, integración y auditoría independiente

Los compositores solo escriben su partición `drafts/<category>/`. Cada partición contiene `lessons.json` (copias exactas del diseño aprobado) y los cuatro archivos musicales. Nunca se altera el diseño durante la integración.

```sh
# Piloto o lote: valida en un directorio separado, sin sustituir los consolidados.
.venv/bin/python tools/scripts/integrate.py --mode pilot --category rhythm --output examples/pilot-data
# Solo cuando todas las lecciones estén aprobadas:
.venv/bin/python tools/scripts/integrate.py --mode global --output approved
.venv/bin/python tools/scripts/integrate.py --mode global --output approved --check
.venv/bin/python tools/scripts/audit_delivery.py
```

El maestro registra cada lote solo después del veredicto independiente y el cierre de incidencias:

```sh
.venv/bin/python tools/scripts/record_approval.py melody 1 lesson-melody-001 lesson-melody-002 lesson-melody-003
```

Este comando no evalúa musicalidad ni reemplaza al revisor: verifica su reporte, repite las puertas técnicas y congela la huella de los registros aprobados. Rechaza incidencias abiertas y cambios a lotes anteriores. `audits/batch-register.json` conserva revisiones y huellas; la auditoría final exige cobertura de las 90 lecciones sin duplicados y coteja nuevamente todas las huellas, incluidos contrato, diseño y piloto.

`--check` compara cada consolidado con la unión exacta de las particiones, independientemente del orden físico. La auditoría exporta una muestra por categoría, doce selecciones con semilla `202603` y todas las progresiones del piloto; elimina duplicados entre esas selecciones. Un lector MIDI independiente contrasta note-on/off, velocidades, PPQ, tempo, compás y duración total. También importa a SQL vacío, comprueba conteos, claves, precisión temporal y una segunda importación idéntica. Guarda evidencia en `audits/delivery-checks.json` y muestras en `examples/audited-midi/`.

## Cargar una lección desde SQL

Primero consulta `lessons` por ID. Recorre sus etapas y selecciona una progresión por etapa; acordes y notas siempre se cargan con el **mismo** `progression_id`:

```sql
SELECT * FROM stages WHERE lesson_id = ? ORDER BY sort_order;
SELECT * FROM progressions WHERE stage_id = ?
ORDER BY CASE kind WHEN 'primary' THEN 0 WHEN 'alternative' THEN 1
         WHEN 'simplified' THEN 2 ELSE 3 END, sort_order;
SELECT * FROM chord_events WHERE progression_id = ? ORDER BY start_beat, sort_order;
SELECT * FROM note_events WHERE progression_id = ? ORDER BY start_beat, midi;
SELECT prerequisite_lesson_id FROM lesson_prerequisites
WHERE lesson_id = ? ORDER BY sort_order;
```

No se infieren relaciones del Markdown ni de nombres de archivo. Cambiar de progresión cambia ambos conjuntos de eventos. `pilot.mid` reproduce solo la segunda etapa del piloto; los demás ejemplos se exportan por su ID.

## Reglas de producción por categoría

El maestro es el único revisor musical y técnico; no se lanzan subagentes revisores con Sol. Se mantienen hasta seis subagentes Luna para composición o correcciones, con encargos acotados y sin delegación adicional.

Cada compositor trabaja solo en `drafts/<slug>/`, con copias exactas del diseño y un máximo de tres lecciones nuevas por lote. Conserva sin cambios los registros ya aprobados y respalda los cinco JSON antes de escribir. No regenera una partición sustituyendo los registros anteriores: preserva los IDs ajenos al lote y comprueba sus huellas antes y después. Antes de continuar con otro lote necesita revisión musical independiente y aprobación del maestro. El piloto es `lesson-rhythm-004`; sus registros aprobados se conservan también en `examples/pilot-data/`.

- Componer cada lección según su objetivo y el mapa de cobertura, no aplicar la misma transformación genérica a todos los temas. Mantener cuatro o cinco etapas con una novedad audible rastreable y autonomía final explícita.
- Definir voicings, líneas y patrones deliberadamente. En acordes realizados como bloques/shells, comprobar tercera y séptima anunciadas (y quinta disminuida en iiø); no confundir una tríada con un acorde de séptima. Una línea melódica o un bajo solos pueden representar un plan armónico de forma parcial si se explica esa textura; no fingir un acorde completo.
- Contar todas las notas sostenidas: máximo orientativo de una octava y cinco sonidos simultáneos por mano. Sin alturas MIDI solapadas entre roles/manos: un mismo piano/canal no puede sostener dos ataques independientes de la misma tecla.
- Estilos de swing, funk, bolero, bossa y son requieren patrones explícitos, no etiquetas sobre acordes genéricos. Para bolero, reducción compartida bajo uno/tres y respuesta dos, 2& y cuatro; bossa de dos compases, acordes uno/2&/cuatro y después dos/3&, bajo uno/tres. Para son, documentar orientación de clave 2–3 y guajeo reducido de dos compases, sin exigir una tercera mano de percusión. No universalizar estas reducciones.
- Sin variantes por mera transposición. Consejos easy/hard son textuales salvo composición completa de versiones adicionales. Cada alternativa tiene notas y acordes propios.
- Generadores locales son aceptables para serializar planes musicales explícitos; no reemplazan el diseño específico de cada lección ni su revisión.

Validación de un lote, sustituyendo `rhythm` por su categoría:

```sh
.venv/bin/python tools/scripts/integrate.py --mode batch --category rhythm --output drafts/rhythm/checks
.venv/bin/python tools/scripts/curriculum.py validate --mode batch --data drafts/rhythm/checks
```

El snapshot incluye las 90 fichas del diseño, pero solo las lecciones compuestas tienen etapas. La revisión informa separadamente ambos conteos. Además de validar, se inspeccionan todas las progresiones nuevas con `audit_delivery.musical_metrics` y lectura binaria MIDI; un compositor no aprueba su propio lote.

La inspección musical automática calcula alcance simultáneo y cantidad de notas por mano, solapamientos de altura y ejemplos idénticos entre etapas. Sus avisos requieren juicio musical; no equivalen a una aprobación idiomática ni a una escucha. Las revisiones pedagógicas y musicales están separadas de la validación técnica.

## Entrega curricular aprobada

El cierre está en `audits/final-audit.md`; las cifras y huellas en `audits/final-summary.json`. Entrega: 6 categorías, 30 skills, 90 lecciones, 400 etapas, 402 progresiones, 2091 acordes y 11016 notas; 125 incidencias cerradas, ninguna pendiente.

- `approved/`: los siete JSON consolidados, unión exacta de las seis particiones. Integrar sobre este directorio preserva los bytes de los tres archivos de diseño congelados.
- `examples/midi/`: los 402 MIDI, uno por progresión, incluidos piloto y alternativas. `audits/all-midi-checks.json` documenta el cotejo binario completo.
- `examples/curriculum.sqlite`: base SQLite de prueba con las 90 lecciones y 225 prerrequisitos ordenados. `audits/sqlite-delivery-checks.json` documenta su importación y segunda importación idéntica.
- `audits/final-tests.log`: 28 pruebas aprobadas; `audits/delivery-checks.json`: auditoría global de aprobación, MIDI y SQL.

No se realizó escucha ni ejecución física. La aplicación web y adaptación a PostgreSQL quedan fuera de esta entrega.
