verdict: approved

# Revisión musical independiente — expression, batch 02

## Alcance y evidencia

Revisadas completas las lecciones **004–006**: intros, objetivos, prerrequisitos, primarySkillId, mapa de cobertura, las 12 etapas nuevas y todos sus eventos. Parseados completos work y checks; inspeccionadas las líneas temporales nuevas sin truncación, agrupando solo eventos con idénticos inicio, duración, mano, role y velocity, y mostrando todas sus alturas. Comparados todos los campos musicales entre etapas consecutivas, sin depender de IDs de notas.

- Lote nuevo: **3 lecciones, 12 etapas, 12 primary, 64 acordes, 300 notas**.
- Acumulado work/checks: **24 etapas, 24 progresiones, 112 acordes, 534 notas**; checks contiene además las 90 fichas de diseño, no 90 lecciones compuestas.
- Los cuatro arrays musicales de work coinciden con checks; las seis fichas de work coinciden con diseño y snapshot. No se reabre la aprobación de 001–003.
- Ciclo 1: E-B02-001 **resolved** por verificación del hint real en work y checks. **Sin incidencias pendientes**, major ni blocker. Aprobación musical; validación técnica, hashes y aprobación global corresponden al maestro en paralelo.

Reverificación del ciclo 1: el hint de 005-04 ahora dice «Aísla el acorde de beat 6 solo como práctica parcial. Después reincorpora el bajo y los acordes de beats 0 y 4, recorre la introducción completa [0,8) con la señal de beat 6 y entra con la frase en beat 8». El texto conserva la destreza formal y resuelve la ambigüedad. Work/checks siguen coincidiendo y mantienen 534 notas acumuladas. Contrastadas las 300 notas del lote con la línea temporal anterior: idénticos inicios, duraciones, pitches, velocities, manos y roles; también se conservan los 64 eventos armónicos en símbolo/inicio/duración y tempo, compás, tonalidad, longitud y condición de loop de las 12 progresiones. El contenido fuente MIDI queda intacto; no se afirma comparación de archivos MIDI binarios ni hashes históricos. No se revisó 007 ni posteriores.

No se modificaron 001–003, el reporte batch-01, composición, scripts ni snapshot. Se escribió exclusivamente este reporte.

## Tabla de las 12 etapas

IDs abreviados de `stage-expression-`. Todos los ejemplos están en C mayor y 4/4. Las cifras LH/RH expresan velocity MIDI, no mediciones de volumen acústico.

| Etapa | Evidencia concreta y delta A/B verificado |
|---|---|
| 004-01 | 16 notas, 4 compases, 66 BPM. Cmaj7–Am7–G7–Cmaj7; bajos 48/45/43/48 sostenidos 4 beats a velocity 56. Derecha [59,64,67]/[60,64,67]/[59,65,67]/[59,64,67], duración 2, velocity 66; G4 superior fijo. V entra en 8 e I en 12. |
| 004-02 | Mismas 16 notas y armonía; únicamente seis velocities derechas cambian: las tres de V 66→80 y las tres de I final 66→58. Bajos, ataques y duraciones intactos; tensión/reposo por dinámica, no acordes nuevos. |
| 004-03 | Únicamente seis duraciones derechas cambian: V 2→3.5, I final 2→1.5. Soltadas en 11.5 y 13.5; entradas en 8 y 12, velocidades y bajo sostenido se conservan. No se atraviesa la frontera armónica con V. |
| 004-04 | Únicamente seis velocities cambian: V 80→74 e I final 58→62. Conserva duraciones 3.5/1.5 y todos los ataques. Sin retorno oculto a la base; referencia no única, invita a elegir contraste propio. |
| 005-01 | 34 notas, 8 compases, 80 BPM, no loopable. Intro [0,8): bajo y Cmaj7 en 0, G7 en 4; bloques derechos duran 2. Frase real de seis compases [8,32), empieza con MIDI 64@8 y bajo 48@8; 18 notas melódicas, todas presentes. |
| 005-02 | 42 notas: añade exclusivamente ocho notas derechas, dos acordes de cuatro notas en 2 y 6, duración 1.5, velocity 66. No modifica notas existentes, plan armónico ni frase desde 8. Ataques 0/2/4/6 hacen explícita la referencia temporal de blancas. |
| 005-03 | 42 notas: solo las cuatro duraciones del acorde en 6 pasan 1.5→0.75. Derecha calla [6.75,8); bajo G2 sigue hasta 8. No es silencio total del piano. Frase y demás señales intactas. |
| 005-04 | 38 notas: elimina exclusivamente las cuatro alturas del acorde en 2; conserva 0, 4, señal 6 de duración 0.75 y entrada melódica en 8. Sin restaurar duraciones antiguas. Elección abierta dentro de los dos compases; hint corregido distingue práctica parcial y reintegración completa [0,8). E-B02-001 resuelta. |
| 006-01 | 20 notas, 4 compases, 68 BPM. Cmaj7–Am7–Fmaj7–G7; izquierda raíz+tercera sostenidas, velocity 56. Derecha 64 salvo MIDI 65@8 a 78: acento aislado auténtico, sin reforzar el bajo. |
| 006-02 | Solo cambia velocity en 15 notas. LH por compás 50/56/62/62; RH 58/64/70/70. Segundo compás intacto respecto a 001; cambia el resto según la curva anunciada. Misma melodía, ataques, duraciones, roles y armonía; crecimiento por niveles, aún sin descenso. |
| 006-03 | Solo cinco velocities del cuarto compás cambian: dos izquierdas 62→50 y tres derechas 70→58. Queda LH 50/56/62/50 y RH 58/64/70/58: cumbre en tercero y retorno al nivel inicial, sin frenar ni añadir notas. |
| 006-04 | Solo cinco velocities del tercer compás aumentan 6: LH 62→68 y RH 70→76. Resto del arco intacto, incluido retorno final 50/58. Referencia no única; elección de intensidad del pico con diferencia MIDI de 8 entre planos. |

## Juicio musical y pedagógico

**004 — dirección y resolución.** La primarySkillId es tension-release; dinámica y duración son dos medios sucesivos de una misma destreza, no una nueva lección de armonía. Las terceras y séptimas están realizadas: C con E/B; Am con C/G; G con B/F. El F de V resuelve a E en I y el bajo G→C fija la llegada. G4 es nota común de los cuatro acordes. La quinta omitida en algunos voicings no impide reconocer su calidad. Las tres transformaciones tienen deltas exactos y acumulativos; los hints localizan V/I y sueltas sin cambiar la función principal.

**005 — señal formal de entrada.** La primarySkillId es form. Hay dos compases introductorios y seis de frase, sin anacrusa negativa ni introducción fuera del total. Cmaj7–G7 prepara realmente C en beat 8. Los bloques completos de intro incluyen tercera y séptima; después la textura declarada cambia a bajo+melodía, sin exigir acordes completos inexistentes. La señal de pulso se refuerza con acordes en intervalos de dos negras: no son ocho ataques a negras ni se afirma que lo sean. Añadir esos ataques enseña la señal temporal, no simula dinámica con densidad. La frase [8,32) es idéntica en las cuatro etapas. La pausa de 005-03/04 es derecha: el bajo sostiene la dominante. La autonomía permite elegir otra señal conservando 0–8 y la llegada. El hint final corregido delimita expresamente que aislar beat 6 es práctica parcial y exige después reintegrar bajo y acordes en 0 y 4, recorrer [0,8) y entrar en 8.

**006 — arco dinámico.** La primarySkillId vuelve a dynamics con ganancia distinta de 001: dirección de cuatro compases, no solo balance estático. El arco está discretizado por compás, no es crescendo continuo nota a nota; así lo hacen explícito los niveles y sus hints. El tercer compás es una zona culminante de tres notas, no una única nota más fuerte que sus vecinas. Es una reducción accesible del objetivo de arco: la última etapa abre su intensidad, sin requerir cambiar pitches o desplazar el pico. No hay retornos ocultos: el descenso aparece únicamente al pasar a 003 y se conserva en 004. Mantener ocho puntos MIDI entre planos documenta la intención de balance, no garantiza igualdad perceptiva entre registros o instrumentos.

**Tocabilidad y armonía contextual.** Contadas todas las notas sostenidas: 004 llega a tres sonidos derechos y ocho semitonos; 005 a cuatro y once; 006 a dos izquierdos separados como máximo por cuatro semitonos y una nota derecha. No hay colisiones de la misma tecla, terceras manos ni notas fuera del final de 16/32 beats. Los rangos y cambios de posición a estos tempos son accesibles. En 005, G y E sobre Fmaj7 actúan como novena y séptima; en 006, A sobre G7 es novena antes de G. Son colores diatónicos contextualizados, no errores detectables por una regla ingenua de pertenencia a tríadas. No se introduce armonía nueva entre etapas.

## Histórico de incidencias — protocolo 8.3

`observed` y `location` conservan el hallazgo inicial; `correction` documenta su resolución verificada en ciclo 1. No hay incidencias abiertas.

```json
[
  {
    "issueId": "E-B02-001",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-expression-005-04",
    "location": "simplifyHint: Toca solo la señal de beat 6 y espera el ataque escrito en 8",
    "expected": "La simplificación conserva la introducción de dos compases desde beat 0 y la información de pulso, o aclara que aislar la señal es práctica parcial antes de reintegrarla.",
    "observed": "El hint dice tocar solo la señal de beat 6, sin conservar explícitamente el bajo o los ataques de 0 y 4 ni pedir reintegración. Leído como versión completa simplificada, elimina el comienzo y debilita el pulso de la introducción. Los eventos principales sí conservan ambos compases y la entrada correcta en 8.",
    "correction": "Verificado en ciclo 1 en work y checks: simplifyHint identifica beat 6 aislado como práctica parcial y pide reincorporar bajo y acordes de 0 y 4, recorrer la introducción completa [0,8) con la señal de 6 y entrar en 8. Conserva la destreza formal. Las 300 notas del lote mantienen inicio, duración, pitch, velocity, mano y role de la revisión anterior; sin cambios del contenido musical para resolver esta incidencia.",
    "owner": "composer-expression",
    "status": "resolved"
  }
]
```

## Límites y cierre

No se escuchó ni renderizó audio, ni se exportó MIDI; se inspeccionó la totalidad de eventos nuevos y sus diferencias. Velocity y duración respaldan la intención compositiva, no una escucha ni una validación acústica. No se certifican aquí esquemas, exportación binaria, SQL o hashes: el maestro los audita en paralelo.

Aprobado musicalmente sin incidencias pendientes; E-B02-001 queda en el histórico como minor resuelta. Solo se actualizó este reporte, sin autorreparar datos ni tocar batch-01; técnica, hashes y decisión global continúan a cargo del maestro.
