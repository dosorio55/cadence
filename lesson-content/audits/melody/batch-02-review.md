verdict: approved

# Revisión musical independiente — melody, lote 02

## Alcance, evidencia y límites

Aprobación **musical** de lesson-melody-004–006: una incidencia minor, ninguna major/blocker. No constituye aprobación técnica ni autorización de otro lote.

Parseados íntegramente los JSON de la partición y checks; selección exclusiva de las tres lecciones nuevas y sus dependencias musicales. Inspeccionados todos sus registros y sus líneas temporales ordenadas por inicio, duración, mano, rol, altura y velocidad, sin depender de salida JSON truncada. **13 etapas, 13 progresiones primary, 52 acordes, 155 notas nuevas**. Checks tiene 25 progresiones acumuladas; no se reevalúan 001–003. Cada registro musical nuevo coincide con su copia de checks. Las tres fichas coinciden con el diseño aprobado y la cobertura; prerrequisitos: M004 M001/M003/H001, M005 M002/M003, M006 M001/A007. Dificultad 2 y cuatro compases en las tres.

`audit_delivery.musical_metrics`, limitado a las 13 progresiones nuevas: `findings: []`. Sin avisos de alcance simultáneo, cantidad de notas por mano, colisiones de tecla ni ejemplos consecutivos idénticos. Esto no sustituye el juicio musical. Maestro responsable de puerta técnica, hashes, exportación/lectura binaria MIDI y SQL en paralelo. Aquí no hubo exportación, render ni escucha; se revisaron eventos y tiempos, no audio.

Única escritura: `curriculum/reports/melody/batch-02-review.md`. Composición, scripts, checks, 001–003 y reporte 01 quedan sin cambios.

## Línea temporal completa y convenciones

Notación: `MIDI@inicio/duración`, en negras desde cero; C4=60. Todas las progresiones: Do mayor, 4/4, cuatro compases, 16 beats, 72 BPM, loop. Todas las notas derechas: `right/melody`, velocidad 76. Todas las izquierdas: `left/bass`, velocidad 58, duración 4; no hay otras manos o roles.

Planes completos, repetidos con IDs propios en cada etapa:

- **M004:** Dm7/ii7@0/4, G7/V7@4/4, Cmaj7/Imaj7@8/4, Cmaj7/Imaj7@12/4. Izquierda: 50@0/4, 43@4/4, 48@8/4, 48@12/4.
- **M005:** Cmaj7/Imaj7@0/4, G7/V7@4/4, Am7/vi7@8/4, Cmaj7/Imaj7@12/4. Izquierda: 48@0/4, 43@4/4, 45@8/4, 48@12/4.
- **M006:** Cmaj7/Imaj7@0/4, Am7/vi7@4/4, Fmaj7/IVmaj7@8/4, G7/V7@12/4. Izquierda: 48@0/4, 45@4/4, 41@8/4, 43@12/4.

Estos planes cubren los 52 acordes y las 52 notas izquierdas. La tabla cubre las 103 notas derechas. En M005, las listas entre corchetes asignan una altura a cada inicio entero indicado, todas con duración 1; cada fila define su línea entera, no una referencia implícita entre archivos.

| Etapa | Derecha íntegra | Transformación y evidencia concreta |
|---|---|---|
| stage-melody-004-01 | 65@0/1; 59@4/1; 67@8/1; 64@12/1 | Base directa F/B/G/E: tercera de Dm7, tercera de G7, quinta y tercera de Cmaj7. ii–V–I mayor real; 12 beats de silencio derecho. |
| stage-melody-004-02 | 65@0/1; 60@3.5/0.5; 59@4/1; 67@8/1; 64@12/1 | Única adición C4@3.5, vecina superior diatónica de B3; resuelve por semitono justo al ataque de G7, sin mover el destino. C es séptima del Dm7 previo: contexto coherente. |
| stage-melody-004-03 | 65@0/1; 60@3.5/0.5; 59@4/1; 69@7.5/0.5; 67@8/1; 64@12/1 | Conserva C–B y añade únicamente A–G: vecina diatónica superior en 7.5, resolución por tono en 8 sobre Cmaj7. A sobre G7 es tensión breve resuelta, no error por no ser nota del acorde. |
| stage-melody-004-04 | 65@0/1; 60@3.5/0.5; 59@4/1; 69@7.5/0.5; 67@8/1; 65@11.5/0.5; 64@12/1 | Añade solo F–E en la última frontera; F diatónico resuelve por semitono a la tercera de Cmaj7 en 12. Instrucción final permite escoger otro destino y simplificar a una sola vecina con su llegada. |
| stage-melody-005-01 | Beats 0–15: [64,67,64,67,62,65,67,59,64,67,69,67,67,64,67,60], duración 1 cada una | A continua real: sin silencio melódico entre las mitades. Pregunta en 0–8 y respuesta en 8–16 comparten E–G y ritmo de negras; termina en C, raíz estable. La falta inicial de aire es contraste explícito, no incumplimiento del objetivo final. |
| stage-melody-005-02 | Beats 0–6: [64,67,64,67,62,65,67]; beats 8–15: [64,67,69,67,67,64,67,60], duración 1 cada una | Único delta: retira B3@7. G4@6 acaba en 7 y E4 entra en 8: silencio derecho real [7,8), una negra completa. Bajo G2 sostenido no anula la respiración de la melodía. |
| stage-melody-005-03 | Beats 0–6: [64,67,64,67,62,65,67]; beats 8–15: [64,67,72,67,67,64,67,60], duración 1 cada una | Solo A4@10→C5; C es tercera de Am7. Conserva pregunta, pausa, arranque E–G de respuesta, ritmo y final C. Variación relacionada, no nueva melodía arbitraria. |
| stage-melody-005-04 | Beats 0–6: [64,67,64,67,62,65,67]; beats 8–15: [64,67,72,67,67,64,67,64], duración 1 cada una | Solo cierre C4@15→E4: tercera estable de Cmaj7. Respuesta ocupa compases 3–4; pausa y vínculo motívico intactos. Se permite elegir otro final estable; hint reduce densidad sin suprimir pausa ni cierre. |
| stage-melody-006-01 | 60@0/1; 57@4/1; 53@8/1; 55@12/1 | Raíces C/A/F/G explícitamente nombradas como raíces, nunca como terceras. Base acordal controlada para oír posteriormente la calidad; no se simula una armonización completa. |
| stage-melody-006-02 | 64@0/1; 57@4/1; 53@8/1; 55@12/1 | Único delta C4→E4. E es tercera mayor real de Cmaj7; las tres notas restantes siguen siendo raíces, tal como dice el texto. |
| stage-melody-006-03 | 64@0/1; 60@4/1; 53@8/1; 55@12/1 | Único delta A3→C4. C es tercera menor real de Am7; F y G permanecen raíces. Sin promesa prematura de cuatro terceras. |
| stage-melody-006-04 | 64@0/1; 60@4/1; 57@8/1; 55@12/1 | Único delta F3→A3. A es tercera mayor real de Fmaj7; G3 sigue como raíz, declarado expresamente. |
| stage-melody-006-05 | 64@0/1; 60@4/1; 57@8/1; 59@12/1 | Único delta G3→B3. Ruta completa E4/C4/A3/B3: terceras mayor/menor/mayor/mayor de Cmaj7/Am7/Fmaj7/G7, intervalos sucesivos −4/−3/+2 semitonos. Autonomía de octava y frase explícita; hint conserva una tercera correcta por acorde. |

## Juicio musical y pedagógico

**M004:** entrada diatónica desde arriba y resolución puntual verificables en las tres preparaciones. No se exige movimiento conjunto desde la nota anterior: se enseña aproximación al destino, no paso entre dos apoyos. El F sobre Cmaj7 y el A sobre G7 son tensiones débiles breves con destino inequívoco. La textura parcial está declarada en las trece etapas/progresiones; ni bajo + melodía ni díadas se presentan como bloques completos de séptima. «Jazz» identifica aquí el contexto armónico, sin anunciar swing ni fingir un patrón idiomático no escrito.

**M005:** forma 2+2 clara mediante registro compartido, E–G inicial común, respuesta variada y cierre C/E sobre tónica. La pausa aparece mediante eliminación de una sola nota, no mediante una mera afirmación textual. No se exige silencio absoluto de ambas manos: la izquierda larga mantiene pulso mientras la línea respira. La versión inicial continua sirve de A/B. Única inconsistencia menor en el hint avanzado de esa base, registrada abajo.

**M006:** construye una ruta de terceras por una sustitución cada vez, sin alterar ritmo ni armonía y sin atribuir séptimas a tríadas. El contraste base usa raíces declaradas, no una versión aleatoria compuesta; es una comparación controlada útil y las instrucciones no aseguran haber generado alturas aleatorias. La tercera mayor de G7 no convierte la dominante en acorde mayor con séptima mayor: el símbolo sigue siendo G7 y no se promete otra cosa. El registro final próximo y el aire cumplen el objetivo de revelar calidad sin escalas ni relleno.

Autonomía final referencial presente en las tres lecciones: elegir destino preparado en 004, final estable en 005 y octavas/frase de las terceras en 006. No son tres copias del mismo adorno; el delta audible cambia de preparación a sustracción/forma y a selección de alturas. Los hints principales conservan el recurso en sus etapas de práctica; las etapas de base pueden mantener su material previo al recurso.

**Tocabilidad:** una nota simultánea por mano en todas las progresiones, sin cruces ni colisiones. Izquierda F2–D3; derecha F3–C5 en el lote. Salto izquierdo máximo 7 semitonos en 004, 5 en 005 y 4 en 006, preparado con notas de cuatro negras. Mayor salto derecho: B3→A4, 10 semitonos en 004-03/04, con 2.5 negras de silencio para recolocar; no extensión simultánea. 005 enlaza negras a 72 BPM, con salto máximo de ocho semitonos solo en su base. 006 tiene tres negras de silencio entre objetivos. No necesita tercera mano ni rangos inviables.

Silencio derecho por etapa: 004 = 12/11.5/11/10.5; 005 = 0/1/1/1; 006 = 12 en sus cinco etapas. Los finales no exceden 16 beats. La base continua de 005 es deliberadamente más densa para el contraste, no una densidad impuesta a las otras lecciones.

## Incidencias — protocolo 8.3

Una minor abierta, no bloqueante; ninguna corrección aplicada por el revisor.

```json
[
  {
    "issueId": "M-B02-001",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-melody-005-01",
    "location": "extendHint frente a la línea continua de prog-melody-005-01-primary, frontera beats 7–8",
    "expected": "El consejo de ampliación debe distinguir la base continua de la versión con respiración, sin pedir conservar un silencio que todavía no existe.",
    "observed": "El hint dice 'Conserva la pausa y transforma una nota de la respuesta', pero la etapa 01 tiene notas de duración 1 en todos los inicios 0–15; B3@7 termina exactamente cuando empieza E4@8. La pausa se introduce recién en etapa 02. El ejemplo y el contraste principal sí son correctos.",
    "correction": "Cierre verificado por el maestro: extendHint de 005-01 transforma una nota de respuesta manteniendo el vínculo con pregunta, sin afirmar una pausa en esta base continua. Snapshot batch válido; lote anterior intacto y métricas sin avisos.",
    "owner": "composer-melody",
    "status": "resolved"
  }
]
```

## Conclusión

**Approved:** destinos, forma, terceras y transformaciones de las trece etapas son verificables y tocables; la minor textual no bloquea el lote. Quedan el ajuste por el compositor y las comprobaciones técnicas independientes del maestro. Sin escucha afirmada y sin tocar el lote 01.

## Cierre del maestro

M-B02-001 verificada sobre el campo corregido y el snapshot. Se conserva la revisión musical previa; no se repitió ni se afirmó escucha. Revisor único para las siguientes entregas: maestro, sin subagentes revisores.
