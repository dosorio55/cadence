# Revisión musical independiente — piloto

**Veredicto actual: approved — ciclo 1.** Las seis incidencias históricas están verificadas y resueltas; cero pendientes. Veredicto inicial: rejected (dos major y cuatro minor). Aprobación musical limitada a este piloto; integración, freeze y permiso de producción corresponden al maestro. No se modificó contenido del compositor.

## Alcance y comprobación

Lectura completa de especificación, skill ponytail, README, ejemplo, mapa pedagógico, diseño de 90 lecciones, snapshot de lecciones y los cinco archivos de trabajo: 1 lección desarrollada, 5 etapas, 6 progresiones, 24 acordes y 120 notas. Las copias de trabajo coinciden con el snapshot; las 90 lecciones del snapshot coinciden con diseño.

Ejecutado `curriculum/.venv/bin/python curriculum/scripts/curriculum.py validate --mode pilot --data curriculum/examples/pilot-data`: «Validación correcta». Exportadas las seis referencias a directorio temporal; `audit_delivery.inspect_midi` contrastó independientemente los 120 note-on/off con alturas, velocidades y tiempos JSON. Todas: PPQ 960, tempo 750000 µs/negra (80 BPM), 4/4, final 15360 ticks = 16 negras = cuatro compases. `examples/pilot.mid` corresponde exactamente a `prog-rhythm-004-02-primary`, no a toda la lección. Métricas automáticas: seis progresiones, cero avisos; no detectan omisión de séptimas.

## Evidencia musical de todas las notas

Convención C4 = MIDI 60. Cada grupo tiene una raíz izquierda y cuatro notas derechas; las alturas siguientes enumeran las 120 notas por repetición explícita del patrón en cada progresión.

| Patrón | Izquierda | Derecha MIDI | Realización observada |
|---|---:|---|---|
| C | 48 | 60,64,67,71 | Cmaj7 completo; C3 separado del registro medio |
| A | 45 | 57,60,64,67 | Am7 completo |
| D | 50 | 57,60,62,65 | Dm7 completo: A3–C4–D4–F4; séptima C4 presente |
| G | 43 | 55,59,62,65 | G7 completo |
| F | 41 | 53,57,60,64 | Fmaj7 completo: F3–A3–C4–E4; séptima E4 presente |

IDs de etapa `stage-rhythm-004-01` a `-05`; principales `prog-rhythm-004-01-primary` a `-05-primary`:

| Etapa/progresión | Grupos y ataques globales (negras) | Duraciones y comparación |
|---|---|---|
| 01 / 01-primary | C@0,A@4,D@8,G@12 | Ambos roles duran 4; base de acordes largos pop/balada, no backbeat obligatorio. |
| 02 / 02-primary | C@0,A@4,D@8,G@11.5 | 4,4,3.5,4.5 en ambas manos; única novedad: V anticipado. Notas `0035–0039` entran juntas, compás 3, 4&, tick 11040; ningún ataque en 12. |
| 03 / 03-primary | C@0,A@3.5,D@8,G@11.5 | 3.5,4.5,3.5,4.5; conserva V y añade vi anticipado. Notas `0045–0049` en tick 3360, compás 1, 4&; sin ataque en 4 ni 12. |
| 04 / 04-primary | C@0,A@3.5,D@8,G@11.5 | Bajo igual a 03; las 16 notas derechas `0061–0064,0066–0069,0071–0074,0076–0079` duran 1.5. Solo cambia articulación; todavía sostienen sobre el uno anticipado. |
| 05 / 05-primary | C@0,A@3.5,D@8,G@12 | Ambos roles duran 3.5,4.5,4,4. Referencia no obligatoria y elección de otra frontera explícitas; `changeFromPrevious` ahora documenta regreso a base sostenida y V regular antes de elegir una anticipación. |
| 05 / 05-alternative-01 | C@0,A@3.5,F@8,G@12 | Mismas duraciones y anticipación conjunta de vi; 20 eventos propios. I–vi–IV–V actual, no transposición; no se penaliza apartarse de I–V–vi–IV propuesto en el mapa. |

Las alturas, velocidad izquierda 72/derecha 66 y registro permanecen constantes entre principales: comparación temporal limpia hasta la vuelta a referencia de 05. Todos los sonidos pertenecen a do mayor; no hay cromatismo injustificado. I–vi–ii–V y I–vi–IV–V son recorridos tonales plausibles para pop/balada con color de séptimas; ahora todos los acordes realizan el color anunciado. Am7→Dm7 conserva A3 y C4, y mueve E4→D4 y G4→F4; Dm7→G7 conserva D4 y F4 y mueve C4→B3, con resolución de la séptima por semitono. La alternativa Fmaj7→G7 mantiene disposición compacta y movimiento de uno o dos semitonos por voz ordenada. La conducción no es óptima ni necesita serlo para esta habilidad: los bloques se desplazan como máximo cuatro semitonos por voz; bajo principal D3→G2 baja siete semitonos con tiempo suficiente. El loop G7→Cmaj7 recupera tónica sin cola ni pickup exterior.

Dificultad 2 razonable para estudiante con armonía previa: cuatro ataques conjuntos por ciclo, pocas fronteras y 80 BPM; etapa 04 añade liberación derecha independiente sin aumentar densidad. Máximo derecho actual **11 semitonos**, conforme al ejemplo: C y F abarcan 11, A y G 10, D solo 8. Las séptimas mayores simultáneas aún pueden requerir adaptación para manos pequeñas, sin exceder octava ni cuatro notas. Los consejos de simplificación permiten comenzar solo con bajo; las extensiones no prometen variantes MIDI inexistentes. Izquierda monofónica, MIDI 41–50; derecha 53–71. No hay cruces, alturas iguales solapadas ni notas fuera del loop; las liberaciones coincidentes con nuevos ataques no constituyen solapamiento accidental. No se requieren pedal ni tres manos.

## Incidencias históricas

Se conservan `observed` y `correction` de la revisión inicial como trazabilidad, no como descripción del estado actual. Los seis estados se cerraron solo después de comprobar datos, textos y dependientes; evidencia por ID después del bloque.

```json
[
  {
    "issueId": "PILOT-MUSIC-001",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-rhythm-004",
    "location": "work/rhythm/note-events.json: compás 3, beat 8; principales 01–05, notas 0011–0014 / 0031–0034 / 0051–0054 / 0071–0074 / 0091–0094",
    "expected": "Realizar Dm7 anunciado en chord-rhythm-004-{01,02,03,04,05}-primary-003 con su séptima C.",
    "observed": "En las cinco etapas, bajo 50 y derecha 57,62,65,69: Dm con A duplicado, sin C en ninguna mano.",
    "correction": "Conservar ritmo y conducción entre etapas y sustituir el A superior 69 por C 72 en las cinco realizaciones, o elegir otro voicing Dm7 cómodo; actualizar dependientes y reexportar piloto.",
    "owner": "composer-rhythm",
    "status": "resolved"
  },
  {
    "issueId": "PILOT-MUSIC-002",
    "severity": "major",
    "entityType": "progression",
    "entityId": "prog-rhythm-004-05-alternative-01",
    "location": "work/rhythm/note-events.json: note-rhythm-004-05-alternative-01-0010–0014; compás 3, beat 8",
    "expected": "Realizar Fmaj7, anunciado por chord-rhythm-004-05-alternative-01-003, con séptima E.",
    "observed": "Bajo 41, derecha 57,60,65,69: F mayor con A duplicado, sin E.",
    "correction": "Usar un voicing Fmaj7 cómodo, por ejemplo derecha 57,60,64,65, conservando entrada y duración; regenerar dependientes.",
    "owner": "composer-rhythm",
    "status": "resolved"
  },
  {
    "issueId": "PILOT-MUSIC-003",
    "severity": "minor",
    "entityType": "lesson",
    "entityId": "lesson-rhythm-004",
    "location": "examples/pilot-lesson.md: párrafo Métricas",
    "expected": "Alcance máximo derecho calculado de las notas reales.",
    "observed": "Declara 11 semitonos, pero 69−57=12 en todos los Dm y en F de alternativa.",
    "correction": "Recalcular después de corregir voicings y documentar el máximo verdadero.",
    "owner": "composer-rhythm",
    "status": "resolved"
  },
  {
    "issueId": "PILOT-MUSIC-004",
    "severity": "minor",
    "entityType": "lesson",
    "entityId": "lesson-rhythm-004",
    "location": "examples/pilot-lesson.md: comando export-midi",
    "expected": "Intérprete documentado curriculum/.venv/bin/python.",
    "observed": "Usa /tmp/pilot-venv/bin/python, ruta temporal no reproducible; hallazgo documental señalado también por el maestro.",
    "correction": "Cambiar el comando a curriculum/.venv/bin/python.",
    "owner": "composer-rhythm",
    "status": "resolved"
  },
  {
    "issueId": "PILOT-MUSIC-005",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-rhythm-004-05",
    "location": "work/rhythm/stages.json: explanationMd de las cinco etapas; especialmente stage-rhythm-004-01",
    "expected": "Explicación breve que identifique material A/B y transformación de cada etapa.",
    "observed": "Las cinco explanationMd son idénticas; incluso la base pide escuchar una B anticipada que su propia primary no contiene. task/change sí son específicos, por lo que no falta toda la guía.",
    "correction": "Especificar explicación por etapa: base regular; comparación 01/02; añadir vi; liberar derecha; elección autónoma. Nombrar la referencia A/B correspondiente sin prometer dos versiones dentro de una primary.",
    "owner": "composer-rhythm",
    "status": "resolved"
  },
  {
    "issueId": "PILOT-MUSIC-006",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-rhythm-004-05",
    "location": "work/rhythm/stages.json: changeFromPrevious; notas 0081–0099 frente a 0061–0079",
    "expected": "Retirada de ayudas como única novedad pedagógica, con contexto musical o reinicio a base claramente explicitado.",
    "observed": "Además de retirar pauta, V vuelve de 11.5 a 12 y las cuatro duraciones derechas pasan de 1.5 a 3.5/4.5/4/4. task dice usar base, pero changeFromPrevious omite estos dos restablecimientos.",
    "correction": "Explicitar que se vuelve a la base sostenida para elegir una sola anticipación y que la novedad es decidirla, no aprender simultáneamente nuevas articulaciones.",
    "owner": "composer-rhythm",
    "status": "resolved"
  }
]
```

## Evidencia de cierre — ciclo 1

`work/rhythm/pilot-corrections.json` fue leído como declaración del compositor, no como prueba. Se releyeron y contrastaron todos los registros reales de trabajo y snapshot: igualdad exacta de la lección desarrollada, cinco etapas, seis progresiones, 24 acordes y 120 notas; diseño de 90 lecciones intacto e idéntico al snapshot.

- **PILOT-MUSIC-001:** los cinco Dm7 en beat 8 tienen bajo 50 y derecha ordenada `[57,60,62,65]`. Verificados los grupos `0011–0014`, `0031–0034`, `0051–0054`, `0071–0074` y `0091–0094` tanto en trabajo como snapshot y en seis MIDI recién exportados. La alternativa de voicing compacto es mejor que ampliar hasta C5; satisface la corrección sin exigir aquella sugerencia literal.
- **PILOT-MUSIC-002:** alternativa, compás 3, beat 8: bajo 41 y derecha ordenada `[53,57,60,64]`. Los IDs `0011–0014` conservan sus tiempos; el orden físico 53,57,64,60 no cambia la simultaneidad ni el acorde. E4=64 verifica séptima mayor real, no inferida del símbolo.
- **PILOT-MUSIC-003:** máximo recalculado sobre los 24 bloques: 11 semitonos, cuatro notas derechas. El texto Métricas, aunque sigue diciendo 11, ahora coincide con las notas corregidas; no se exige cambiar una cifra que pasó a ser cierta. C=11, A=10, D=8, G=10, F=11.
- **PILOT-MUSIC-004:** el comando usa `curriculum/.venv/bin/python`; intérprete presente y utilizado para validación y pruebas. Ya no depende de `/tmp/pilot-venv`.
- **PILOT-MUSIC-005:** las cinco explicaciones son distintas y nombran referencias precisas. 01 aclara que aún no hay B anticipada; 02 compara 01/02; 03 compara 02/03; 04 compara 03/04 y especifica 1.5 beats; 05 compara base 01 con referencia 05. Tareas, criterios y consejos siguen siendo coherentes con sus eventos.
- **PILOT-MUSIC-006:** `stage-rhythm-004-05.changeFromPrevious` explicita V de 11.5 a 12 y restauración de bloques largos. Es reinicio de contexto conocido para una sola novedad pedagógica —decidir libremente una llegada—, no dos técnicas nuevas obligatorias. La referencia conserva vi@3.5 y no impone una solución única.

Puertas reejecutadas: validación `--mode pilot` correcta; `unittest discover -s curriculum/tests -v`: **23/23 OK**. Comprobación adicional de las 120 notas: alturas, manos, velocidades, grupos de cinco, ataques y duraciones exactos; etapa 04 conserva solo derecha de 1.5 beats. Anticipaciones de vi y V siguen en ticks 3360 y 11040, sin reataques en beats 4 y 12 cuando corresponde. Métricas automáticas: seis progresiones, cero avisos.

Se exportaron nuevamente los seis MIDI a directorio temporal, y `audit_delivery.inspect_midi` comprobó todos los note-on/off contra JSON, además de PPQ 960, tempo 750000, 4/4 y endTick 15360. El binario entregado `examples/pilot.mid` también coincide con la etapa 02 **corregida**, incluida C4 en Dm7; SHA-256: `03e12cf73aa376b15c7dea7e15a08fa0c7d962ec0fa66dfdf04fbcbf54d0a064`.

## Limitación y siguiente puerta

Inspección temporal y binaria, **sin escucha ni interpretación física**: hay sintetizador pero no soundfont local; no se reprodujo audio. No se reejecutó auditoría SQL del snapshot ni integración/freeze, asignadas al maestro; las pruebas generales sí incluyen casos SQLite. Aprobado musicalmente este piloto tras ciclo 1, sin autorización de producción ni aprobación de las 89 lecciones restantes.
