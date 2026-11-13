# Auditoría final — currículo Piano Lab 1.0.0

**Veredicto del maestro: aprobado para entrega curricular.** Las 90 lecciones están compuestas, revisadas e integradas. No hay incidencias pendientes ni trabajo de aplicación web incluido.

## Entrega numérica

| Categoría | Skills | Lecciones | Etapas | Progresiones/MIDI | Acordes | Notas |
|---|---:|---:|---:|---:|---:|---:|
| Ritmo | 5 | 15 | 63 | 64 | 311 | 2862 |
| Acompañamiento | 5 | 15 | 75 | 76 | 408 | 2049 |
| Armonía | 5 | 15 | 60 | 60 | 320 | 1166 |
| Melodía | 5 | 15 | 64 | 64 | 348 | 1204 |
| Independencia | 5 | 15 | 74 | 74 | 336 | 2040 |
| Expresión | 5 | 15 | 64 | 64 | 368 | 1695 |
| **Total: 6 categorías** | **30** | **90** | **400** | **402** | **2091** | **11016** |

Hay 50 lecciones de cuatro etapas y 40 de cinco. Las dos progresiones adicionales son alternativas reales: la del piloto y la guía melódica separada de acompañamiento 015. Los 225 prerrequisitos conservan relaciones y orden.

Los siete arrays finales están en `curriculum/data/`; sus SHA-256 y el desglose completo están en `final-summary.json`. `curriculum/examples/midi/` contiene los 402 MIDI. `curriculum/examples/curriculum.sqlite` es una importación persistente de prueba, no una base de producción.

## Puertas técnicas completadas

- **Unión exacta:** `integrate.py --mode global --output curriculum/data --check` coincide con las seis particiones, sin pérdidas, registros ajenos ni diseño modificado. Evidencia: `global-union-check.json`.
- **Contrato y aprobaciones:** 31 entradas, incluido el piloto, cubren exactamente las 90 lecciones, sin duplicados. Se repitieron los SHA congelados de contrato, diseño y piloto, las huellas de registros y los hashes de cada revisión; todos coinciden. Evidencia: `batch-register.json` y `delivery-checks.json`.
- **Validación global:** esquemas estrictos, IDs, referencias, órdenes, DAG, cantidades, cuadrícula y límites temporales aprobados.
- **Pruebas:** 28/28 pasan. Incluyen rollback, idempotencia, orden de prerrequisitos, rechazo de datos inválidos, serialización MIDI y preservación byte por byte del diseño durante integración in situ. Evidencia: `final-tests.log`.
- **MIDI exhaustivo:** los 402 archivos se exportaron y leyeron binariamente. Coinciden todos los ataques y liberaciones de las 11016 notas, alturas, velocities, PPQ 960, tempo, compás y final del loop. Evidencia por archivo con SHA: `all-midi-checks.json`. Además, la selección reproducible de semilla 202603 cubre seis categorías, doce selecciones aleatorias y todo el piloto: 24 archivos únicos en `curriculum/examples/audited-midi/`, registrados en `delivery-checks.json`.
- **SQL:** importación vacía y segunda importación idéntica; conteos, claves, orden y precisión temporal conservados. `foreign_key_check` vacío e `integrity_check=ok`. La base persistente reproduce el mismo dump verificado por la auditoría temporal. Evidencia: `sqlite-delivery-checks.json`; dump SHA-256 `15ee3048c853978b2e302abe9be26e8e597d95599c232d6d1577127918dae8a3`.
- **Métricas musicales:** las 402 progresiones no presentan alcances simultáneos superiores a una octava, más de cinco notas por mano, solapamientos de la misma tecla ni ejemplos idénticos entre etapas consecutivas. Estas métricas no sustituyen la revisión musical.

## Revisión musical y pedagógica

El maestro cotejó las entregas contra las fichas congeladas y revisó texto, armonía, alturas, manos, cronología, duraciones, perfiles dinámicos y diferencias entre etapas antes de registrar cada lote. Las revisiones por categoría están en `curriculum/reports/<categoría>/batch-NN-review.md`; el registro enlaza cada una con sus lecciones y huella.

Se conservaron objetivos y prerrequisitos del mapa aprobado. Cada skill tiene tres lecciones de dificultad creciente. Las últimas fases distinguen un ejemplo reproducible de la elección del estudiante: no obligan a acumular cambios o aplicar todos los recursos.

Criterios musicales aplicados:

- Terceras, séptimas y notas alteradas se contrastan con los acordes reales; los arreglos parciales se identifican como tales, sin fingir voicings completos.
- Se comprobaron resoluciones, notas comunes reatacadas frente a sostenidas, cierres frente a retornos, y ubicación exacta de anticipaciones.
- Swing usa relaciones temporales explícitas cuando corresponde; funk, bolero, bossa y son se documentan mediante sus patrones reducidos, no solo etiquetas. Son conserva orientación 2–3 sin exigir una tercera mano de clave.
- Registro, densidad, duración, dinámica y omisiones se introducen por fases. Cuando se reinicia una referencia, se explica qué se restaura; una omisión no elimina notas adicionales ni detiene accidentalmente la otra mano.
- Las referencias iguales no consecutivas son reinicios pedagógicos declarados, como melodía 013/05 y armonía 015/04, no variantes por mera transposición.

La composición/corrección se mantuvo en Luna, con revisión del maestro y sin nuevos subagentes Sol para este cierre. No se sustituyeron modelos silenciosamente. Los datos y la metainformación congelada permanecen intactos.

## Incidencias y excepción documentada

**125 incidencias cerradas: 2 blocker, 76 major y 47 minor; 0 pendientes.** Registro: `issues.json`. Las correcciones de los últimos lotes incluyen restauración de manos perdidas, omisiones que no existían o se acumulaban, notas de cerco mal situadas, funciones incorrectas y discrepancias entre dinámica/duración anunciadas y MIDI.

La primera integración global fue rechazada con `Contrato/diseño/piloto congelado alterado: curriculum/data/skills.json`: el integrador reserializaba el diseño sin cambiar sus registros. Se restauraron `skills.json` y `lessons.json` desde copias con SHA exactamente iguales al contrato; no se reemplazaron huellas para ocultar el cambio. TOOLS-003 corrige la causa: al escribir sobre el directorio del diseño solo se escriben las cuatro tablas musicales. La regresión y la repetición real de integración, auditoría y hashes pasan. Detalle: `tools-audit.md`, `curriculum/scripts/integrate.py:126` y `curriculum/tests/test_integration.py:44`.

Queda una advertencia aceptada de registro, no una incidencia abierta: 15 notas B2 (MIDI 47) en la derecha de acompañamiento 015/03–05. Están encima del bajo G2/D2, sus shells caben en la mano y dejan libre la guía. No hay colisión de teclas ni cruce efectivo entre manos. El log repite estos avisos al validar varias veces la misma entrega.

## Límites y fuera de alcance

No se realizó escucha de audio, interpretación física ni prueba con estudiantes. La aprobación se basa en análisis musical y lectura de JSON/MIDI; no certifica balance acústico, digitación para todas las manos ni aprendizaje efectivo. Se recomienda interpretar las piezas al incorporarlas a un instrumento virtual o piano real.

SQLite es el destino SQL de prueba. PostgreSQL/JSONB requiere adaptación explícita; el importador hace UPSERT y no elimina automáticamente registros retirados de una versión previa. No se construyeron aplicación web, reproductor con audio, evaluación automática, transposición de runtime ni progreso personal.

**Cierre:** currículo y herramientas entregados, con cero bloqueantes pendientes. El siguiente trabajo, separado de este alcance, es su integración en la aplicación y prueba sonora/pedagógica real.
