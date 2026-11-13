verdict: approved

# Revisión musical independiente — expression, batch 01

## Revisión actual — ciclo 1

**Aprobación musical tras verificar las correcciones reales.** Las cuatro incidencias E-B01-001–004 quedan `resolved`; no hay incidencias musicales abiertas. Dictamen inicial histórico: `rejected`, con dos major y dos minor, sobre 230 notas. Dictamen actual: `approved`, sobre 234 notas. Esta aprobación no sustituye la validación técnica, hashes ni aprobación global del maestro.

Verificación del ciclo 1: 003-02 elimina únicamente MIDI 64 en beat 3; 003-03 elimina adicionalmente MIDI 64 en beat 11 y mantiene MIDI 55 en 12 y MIDI 60 en 15; 003-04 retira solo MIDI 60 en 7 respecto a 003-03, con autonomía explícita. 001-01 usa velocity 68/68 y 001-02 cambia solo las cuatro velocities izquierdas a 50. Los 12 pares de hints son específicos de balance, duración o respiración. 002-02 documenta explícitamente el solapamiento de 0.25 beats y la última duración de 1 para cerrar en 16.

## Alcance y método

Revisión de expression-001–003, sin modificar composición, scripts ni snapshot. Leídos completos `PIANO_LAB_CURRICULUM_SPEC.md`, skill `ponytail`, `curriculum/README.md`, mapa de cobertura y revisión pedagógica; cotejadas las tres fichas con el diseño aprobado.

Parseados completos los cinco arrays de `curriculum/work/expression/` y los siete de `checks/`. Conteos de composición: **3 lecciones, 12 etapas, 12 progresiones, 48 acordes, 234 notas**. Snapshot: 6 categorías, 30 skills, 90 fichas de diseño y los mismos 12/12/48/234 registros musicales. Las cinco particiones coinciden con sus registros en checks; las tres fichas coinciden con el diseño. No confundir las 90 fichas con lecciones musicalizadas.

Reinspeccionadas en ciclo 1 las **234 notas sin truncación**, ordenadas por inicio, con ID, duración, mano, role, pitch MIDI y velocity; además, los 48 eventos armónicos y todas las instrucciones. Comparados campos entre etapas y calculada simultaneidad contando notas sostenidas. La auditoría técnica, hashes y aprobación global corresponden al maestro en paralelo; aquí no se certifican ni se sustituyen.

## Evidencia por etapa

Los identificadores de esta tabla abrevían `stage-expression-`. Todas las progresiones son primary, 4/4, cuatro compases, 72 BPM, beats 0–16. El mapa armónico se conserva: Cmaj7/Am7/Fmaj7/G7, cuatro beats cada uno. La izquierda sostiene MIDI 48/45/41/43 durante cuatro beats por compás.

| Etapa | Evidencia concreta y juicio |
|---|---|
| 001-01 | 20 notas; velocity bajo/melodía 68/68. Texto y ejemplo alineados; distingue igualdad MIDI de volumen acústico. E-B01-003 resuelta. |
| 001-02 | 20 notas; solo cambian cuatro velocities izquierdas, 68→50; derecha 68. Alturas, ataques y duraciones idénticos: contraste de balance real sin densidad añadida. |
| 001-03 | Solo cambian las 16 velocities derechas, 68→82; bajo sigue 50. Una novedad verificable; misma armonía y contexto A/B. |
| 001-04 | Derecha 82→74, bajo 50; mismas 20 notas. Elección autónoma explícita y referencia no única; no se impone cambiar notas. |
| 002-01 | 20 notas; derecha en beats enteros, duración 1, velocity 68; bajo 58, duración 4. Referencia conectada exactamente hasta el ataque siguiente. |
| 002-02 | Mismos pitches, ataques y velocities; 15 duraciones derechas pasan 1→1.25; última queda 1 para cerrar en 16. Solapamiento de 0.25 explícito en explicación, cambio y hint. Tocable: máximo dos notas derechas, intervalo simultáneo de nueve semitonos. |
| 002-03 | Las 16 duraciones derechas pasan a 0.5; bajo intacto y sostenido. Separación efectiva sin mover ataques ni cambiar volumen. No se cortan notas izquierdas por imitación del staccato. |
| 002-04 | Duraciones derechas alternan 0.5/1; solo ocho cambian respecto a 002-03. Conserva notas, ataques, bajo y velocities. Autonomía de toque explícita; referencia no única. |
| 003-01 | 20 notas; melodía continua a negras, con finales de célula en 3/7/11/15. Base suficiente para comparar ocupación y silencio sin armonía nueva. |
| 003-02 | 19 notas: elimina únicamente MIDI 64@3 respecto a 003-01; conserva respuestas en 7 y 11, entrada en 12 y nota en 15. Bajo y demás campos intactos. E-B01-001 resuelta. |
| 003-03 | 18 notas: elimina únicamente MIDI 64@11 respecto a 003-02; crea la pausa [11,12) antes de MIDI 55@12. Mantiene 60@7 y 60@15; no corta otras duraciones. E-B01-002 resuelta. |
| 003-04 | 17 notas: elimina únicamente MIDI 60@7 respecto a 003-03; conserva entrada en 12 y nota en 15. Explica que se puede restaurar ese relleno o retirar otros: referencia autónoma no única. |

## Musicalidad, pedagogía y límites

Una primarySkillId por lección: dynamics, articulation y space respectivamente. Las tres lecciones aíslan correctamente el parámetro musical y preservan el contexto A/B. En 003, cada etapa retira ahora una sola nota de relleno y conserva los campos de todos los eventos restantes. La autonomía final es explícita en las tres lecciones. Leídos los 12 pares de hints: 001 orienta contrastes de velocity entre manos sin cambiar notas; 002 concreta duraciones 1.25/0.5/1 sin mover ataques ni cortar el bajo; 003 identifica rellenos y conteo hasta la entrada fija en 12. E-B01-004 resuelta.

No hay tres manos: únicamente bajo izquierdo y melodía derecha. Máximo simultáneo izquierdo: una nota; derecho: una, salvo 002-02, con dos y alcance máximo de nueve semitonos. Sin alturas iguales solapadas, ni eventos posteriores al beat 16. No se añade densidad para simular dinámica; el solapamiento de 002-02 resulta de duración, no de ataques adicionales.

La textura parcial está declarada en todas las descripciones («bajo y melodía, sin acordes añadidos»): no se exige completar terceras/séptimas simultáneas ni se certifican bloques completos inexistentes. El mi sobre Fmaj7 en beat 11 es séptima mayor; do sobre G7 en 15 funciona como tensión final que retorna a C. En 002-02, mi continúa hasta 12.25 sobre G y las notas de enlace se superponen brevemente: no son por sí mismas falsas disonancias ni imposibilidades técnicas. El texto de 002-02 ya describe el ligado como solapamiento de 0.25 beats, incluida la excepción de la última nota; coincide con los eventos.

**Ciclo 1: dos major y dos minor resueltas por verificación; ninguna incidencia abierta.** No se escuchó ni renderizó audio, ni se exportó MIDI en esta revisión. La evidencia de balance es velocity, no una medición acústica; su percepción depende del instrumento. No se afirma escucha ni validación técnica global. No se autorreparó ningún registro.

## Histórico de incidencias — protocolo 8.3

`observed` conserva el hallazgo inicial, no describe el estado actual. `correction` registra la corrección solicitada y su verificación en ciclo 1; las severidades originales se conservan para trazabilidad.

```json
[
  {
    "issueId": "E-B01-001",
    "severity": "major",
    "entityType": "stage",
    "entityId": "stage-expression-003-02",
    "location": "explanationMd/changeFromPrevious y prog-expression-003-02-primary, beats 3, 7 y 11",
    "expected": "La comparación guiada retira solo el relleno posterior al primer motivo, conservando las otras respuestas para las transformaciones posteriores.",
    "observed": "Respecto a 003-01 desaparecen tres notas: MIDI 64 en beat 3, MIDI 60 en 7 y MIDI 64 en 11. El texto anuncia un único grupo posterior al primer motivo. También desaparece ya el relleno previo a la entrada final en 12.",
    "correction": "Se solicitó una retirada localizada y revisar dependientes. Verificado en ciclo 1: 003-02 tiene 19 notas y elimina únicamente MIDI 64@3 respecto a 003-01; conserva notas en 7, 11, 12 y 15, bajo y todos los campos restantes. Texto alineado; dependientes reevaluados.",
    "owner": "composer-expression",
    "status": "resolved"
  },
  {
    "issueId": "E-B01-002",
    "severity": "major",
    "entityType": "stage",
    "entityId": "stage-expression-003-03",
    "location": "explanationMd/changeFromPrevious y prog-expression-003-03-primary, beats 11–16",
    "expected": "La novedad respecto a 003-02 es retirar relleno antes de la entrada final en beat 12, haciendo rastreable la respiración y la reentrada.",
    "observed": "El único evento eliminado respecto a 003-02 es MIDI 60 en beat 15, después de la entrada en 12. La pausa [11,12) ya estaba presente y no cambia. El nuevo silencio [15,16) prepara el retorno del loop, no la entrada anunciada.",
    "correction": "Se solicitó retirar relleno antes de beat 12. Verificado en ciclo 1: 003-03 tiene 18 notas y elimina solo MIDI 64@11 respecto a 003-02, creando silencio [11,12); mantiene MIDI 55@12, MIDI 60@7 y MIDI 60@15. 003-04 retira solo beat 7 respecto a 003-03 y explica la elección autónoma.",
    "owner": "composer-expression",
    "status": "resolved"
  },
  {
    "issueId": "E-B01-003",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-expression-001-01",
    "location": "explanationMd/task y prog-expression-001-01-primary, todos los compases",
    "expected": "La referencia al mismo nivel debe corresponder a la intención de balance del ejemplo, sin prometer igualdad acústica por un valor MIDI.",
    "observed": "El texto pide melodía y bajo al mismo nivel, pero todos los bajos tienen velocity 58 y la melodía 68. La base ya incorpora una jerarquía MIDI, aunque las transformaciones posteriores de velocity sí son verificables.",
    "correction": "Verificado en ciclo 1: las 20 notas de 001-01 tienen velocity 68; explicación y task distinguen velocity MIDI de volumen acústico. En 001-02 solo cambian las cuatro velocities izquierdas de 68 a 50; derecha, alturas, ataques y duraciones permanecen iguales.",
    "owner": "composer-expression",
    "status": "resolved"
  },
  {
    "issueId": "E-B01-004",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-expression-003-03",
    "location": "simplifyHint/extendHint de las 12 etapas del lote",
    "expected": "Consejos concretos que faciliten o amplíen la destreza de cada lección sin perder su parámetro principal.",
    "observed": "Las 12 etapas repiten practicar manos separadas a tempo cómodo y elegir un balance o toque propio. No indican cómo reducir la tarea de contar hasta la reentrada, graduar duración conservando ataques o controlar específicamente el contraste de manos.",
    "correction": "Verificados en ciclo 1 los 12 pares simplifyHint/extendHint: balance con valores 68/50/82/74 en 001; duración y ataques fijos, incluido solapamiento explícito de 0.25, en 002; rellenos localizados y conteo hasta beat 12 en 003. Son específicos de sus etapas, sin versiones MIDI adicionales ni conceptos ajenos.",
    "owner": "composer-expression",
    "status": "resolved"
  }
]
```

Se actualizó exclusivamente este reporte; no se autorrepararon datos. Lote aprobado en revisión musical tras ciclo 1; corresponde al maestro completar técnica/hashes y decidir su aprobación global.
