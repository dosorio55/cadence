approved

# rhythm — lote 02, revisión musical independiente

**Cierre: tres incidencias resueltas, sin pendientes.**

Los apartados de la revisión inicial siguientes se conservan como evidencia histórica del rechazo; el estado actual y los patrones corregidos constan en el cierre del maestro.

**Revisión inicial histórica:** Alcance exclusivo: `lesson-rhythm-005`, `lesson-rhythm-006`, `lesson-rhythm-007`. No se alteraron contenido, piloto ni reportes congelados.

## Alcance y comprobaciones

Se parsearon los arrays completos de trabajo y checks, seleccionando mediante relaciones las tres lecciones nuevas. Se verificó igualdad exacta trabajo/snapshot: **3 fichas, 12 etapas, 12 progresiones, 52 acordes y 744 notas**. Las fichas nuevas son copias exactas del diseño. Checks contiene las90 fichas, no90 lecciones desarrolladas. Se contrastaron intros, metas, primarySkill, prerrequisitos y cobertura rhythm; especificación y reglas de producción del README siguen siendo el contrato de revisión.

Se imprimieron e inspeccionaron todos los grupos `(start,duration,hand,role,pitches/velocity)` de las744 notas sin truncamiento, no muestras. Todas las12 progresiones se exportaron a directorio temporal y se leyeron con `audit_delivery.inspect_midi`: notas, velocidades y duraciones coinciden con JSON; PPQ960,4/4, tempo600000µs/negra para005,750000 para006 y666667 para007. Cierre15360ticks en005/007 y30720 en006. Las referencias ternarias se conservan como640/320ticks por pareja, sin cuantizar a corcheas rectas. `musical_metrics`:12 progresiones, cero avisos; los errores armónico/pedagógico siguientes no están cubiertos por esa métrica.

No se regeneró integración ni se ejecutó SQL/puerta técnica general: los realiza el maestro en paralelo. El cotejo MIDI verifica fidelidad al JSON, no que ese JSON sea musicalmente correcto.

## Diccionario exhaustivo de alturas y patrones

`t`: negras desde0; `b`: inicio de cada compás; C4=MIDI60. Todos los eventos pertenecen exclusivamente a estos patrones, confirmados en cada ataque:

- **005:** izquierda `bass`, velocidad70, duración2, ataques t0,2,4,6 con38(D2), t8,10,12,14 con43(G2). Derecha monofónica `melody`, velocidad62:69(A4) en[0,8),65(F4) en[8,16), salvo omisiones documentadas. No hay C ni E ni B ocultos que realicen una llegada a tónica. Plan escrito, idéntico en las cuatro etapas: Dm7[0,4),G7[4,8),Cmaj7[8,12),Cmaj7[12,16).
- **006:** secuencia C/G/Am/F repetida dos veces, ocho eventos de duración4 por progresión. Raíces izquierdas48/43/45/41; tríadas derechas `[60,64,67]`/`[59,62,67]`/`[57,60,64]`/`[57,60,65]`. Izquierda `bass`, velocidad70; derecha `harmony`,62. Todos duran0.5. Base: bajo a cada entero0…31; derecha b+0,b+2 en ocho compases. Las retiradas no cambian alturas ni los ataques restantes.
- **007:** un C7/I7 de0a16. Bajo48(C3), `left/bass`,70, duración0.5, en b+0,b+2. Derecha siempre `[60,64,67,70]`(C4/E4/G4/Bb4), `right/harmony`,60, duración0.25. Cuatro bloques por compás en todas las etapas; no hay escala ni notas decorativas añadidas.

## Evidencia por las doce etapas

Cada etapa `stage-rhythm-LLL-SS` tiene exactamente su `prog-rhythm-LLL-SS-primary`; sin alternativas nuevas. La tabla, junto al diccionario anterior, describe las744 notas completas.

| Etapa | Timeline y conteo | Juicio musical y delta A/B |
|---|---|---|
| stage-rhythm-005-01 | Bajo según diccionario; derecha n,n+0.5 para n=0…15, duración0.5.40 notas. | Base binaria real, una nota por ataque y bajo en blancas, pero no realiza el ii–V–I–I anunciado (001). |
| stage-rhythm-005-02 | Bajo idéntico; derecha n duración2/3, n+2/3 duración1/3.40 notas. | Único cambio: colocación y duración largo–corto, sin alterar alturas ni pulso. Explicita que2:1 no es regla universal del swing; musicalmente válida como referencia de subdivisión, con el mismo fallo armónico heredado. |
| stage-rhythm-005-03 | Igual a02 salvo nota corta ausente en15+2/3.39 notas. | Una pausa exacta de1/3 al terminar compás4; la nota anterior acaba en15+2/3, no se prolonga para fingir un hueco. Bajo termina en16. Delta verificable y criterio coherente. |
| stage-rhythm-005-04 | Referencia02, omite solo ataque largo t5; conserva corto5+2/3.39 notas. | Hueco real[5,5+2/3); no queda sonido anterior sostenido que lo tape. A=02 identificada y elección propia permitida; restaura el corto final como reinicio de esa referencia, no comparación engañosa con03. Autonomía válida, pendiente armonía. |
| stage-rhythm-006-01 | Base completa32b:32 bajos+16 tríadas,80 notas. | Ocho compases reales, dos vueltas con conducción cómoda. Bloques en tiempos uno/tres; no se exige backbeat a una lección de pulso. Bajo a negras de ataque, articulación breve0.5. |
| stage-rhythm-006-02 | Solo elimina derecha t12 y14;74 notas. Bajo conserva12,13,14,15. | Compás4 sin derecha; reentrada conjunta t16, compás5, C con bajo48 y tríada60/64/67. No cambia mapa, tempo ni largo del ciclo. |
| stage-rhythm-006-03 | Conserva hueco derecho; elimina únicamente bajos t21 y22;72 notas. | Compás6: bajo43 en20 y23; derecha G en20 y22. Puede contar dos ataques bajos ausentes sin silencio total obligatorio. Tras bajo23, llegada conjunta24 aAm(45+57/60/64) intacta; no se adelanta el compás7. |
| stage-rhythm-006-04 | Mismo hueco bajo21/22; silencio derecho pasa de compás4 a2: omite t4/6, repone12/14.72 notas. | Autonomía acotada y referencia explícita: reentradas t8 y24 conservadas con ambas manos. Una decisión nueva —dónde dejar aire— sobre material conocido, sin agregar dificultad armónica. |
| stage-rhythm-007-01 | C7; derecha b+{0,1,2,3}, duración0.25;8 bajos+64 notas derechas=72. | C7 completo con E/Bb; base a negras, no a corcheas como prevé intro para comparación (003). Articulación corta no convierte frecuencia de negra en corcheas. |
| stage-rhythm-007-02 | Mismo bajo/voicing; derecha b+{0,0.25,2,2.25};72 notas. | Dos parejas reales de semicorcheas; huecos amplios[0.5,2) y[2.5,4) en cada compás. Reagrupa cuatro ataques, no aumenta densidad. Reducción razonable de vamp funk con notas cortas y bajo espaciado. |
| stage-rhythm-007-03 | Derecha b+{0,0.25,2.25,2.5};72 notas. | Solo retrasa segunda pareja0.25 frente a02; primera pareja y bajo intactos. Delta real, pero la unidad elegida es pareja, no ataque único del objetivo final (002). |
| stage-rhythm-007-04 | Derecha b+{0.25,0.5,2.25,2.5};72 notas. | Frente a03 mueve primera pareja; frente aA=02 declarada mueve las dos. Conserva cuatro bloques, pero el ejemplo no ilustra la elección de una sola pareja/ataque que pide su propia explicación ni el ataque único del diseño (002). |

## Armonía, estilo y tocabilidad

Cada ficha conserva una primarySkill y un resultado propio: comparar recto/ternario005, sostener ciclo durante ausencias006 y colocar semicorcheas007. No se penaliza repetir consejos de bajar tempo o practicar manos: explicaciones y criterios son específicos, sin placeholders. Tampoco se fingen variantes easy/hard.

**005:** se permite textura raíz+línea monofónica, no exige rellenar acordes completos ni todas sus séptimas. El problema no es esa reducción: la izquierda dice tocar raíces, pero conservaD2 durante el G7 escrito en compás2 y tocaG2 durante ambosCmaj7. F4 repetido en cada parte fuerte de los compases3/4 no tiene resolución a E4; junto aG2 realiza una prolongación de dominante, no la llegada aI anunciada. A4 sobreG7 podría ser novena y G bajoC podría ser pedal, pero no están explicados y no subsanan la ausencia de tónica. La progresión práctica se parece a dos compases deD y dos deG, no a ii–V–I–I. Hay que corregir ambas manos en las cuatro versiones sin destruir la comparación temporal.

**006:** tríadas diatónicas completas, símbolos Am correctos y espacio de registro útil. Am→F conserva57/60 y mueve64→65; C→G conserva67 y mueve60→59,64→62. Los huecos derechos dejan raíces solas intencionalmente. Los huecos de bajo no cambian la armonía y no se promete silencio total donde hay acorde derecho. No hay ataque desplazado ni compás recortado accidentalmente.

**007:** Bb70 es séptima menor explícita del vamp C7; no es error por estar declarado centroC/major. Un vamp funk tónico admite ese color mixolidio/blues, sin obligar resolución aF. Hay semicorcheas, pausas y stabs reconocibles desde02, no mera etiqueta aplicada a una escala;01 es contraste preparatorio y no pretende representar todo el género. No hace falta imponer acentos nuevos para aprobar la habilidad de rejilla.

Tocabilidad, dificultad2:005 monofónico por mano, izquierda38–43 y derecha65–69;006 izquierda41–48 y derecha57–67, span derecho máximo8semitonos/3notas;007 bajo48 fijo y derecha60–70, span10/4notas. Sin cruces, alturas duplicadas solapadas ni colas exteriores. Las notas coincidentes de final/inicio son liberaciones seguidas de ataque, no pedal ficticio. En007 las parejas están separadas por0.25negra a90BPM≈167ms: cuatro voces repetidas requieren mano suelta, pero se presentan en ráfagas breves y con consejo de bajar tempo, razonables para este nivel.005 a100BPM tiene ataques cortos de200ms, sin virtuosismo. La ausencia de escucha limita valoración tímbrica, no oculta las discrepancias verificables.

## Incidencias — protocolo8.3

```json
[
  {
    "issueId": "R-B02-001",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-rhythm-005",
    "location": "work/rhythm/note-events.json y checks: prog-rhythm-005-{01,02,03,04}-primary, compases2–4, beats4–16; chord-events de esas cuatro progresiones",
    "expected": "Bajo en blancas y línea sencilla que sigan Dm7 en0–4, G7 en4–8 y Cmaj7 en8–16, conforme al intro y los cuatro mapas armónicos.",
    "observed": "En las cuatro versiones el bajo es38/D2 en0,2,4,6 y43/G2 en8,10,12,14; derecha69/A4 durante0–8 y65/F4 durante8–16. G7 escrito en4 no recibe raízG; Cmaj7 en8/12 recibe G y F repetido sin resolución. Ejemplo01: notas0019/0020 sonD2 en4/6;0029/0030 y0039/0040 sonG2 en8/10/12/14, mientras0021/0025/0031/0035 sonF4 en esos pulsos.",
    "correction": "Bajo D2/G2/C3/C3 y línea A4/F4/E4/E4 corregidos en las cuatro etapas; onsets, articulaciones y omisiones coinciden con la comparación recta/ternaria. La séptima F de V resuelve a E de I.",
    "owner": "composer-rhythm",
    "status": "resolved"
  },
  {
    "issueId": "R-B02-002",
    "severity": "major",
    "entityType": "stage",
    "entityId": "stage-rhythm-007-04",
    "location": "work/rhythm/stages.json y note-events.json:007-03/04, comparación con A=007-02; todos los compases",
    "expected": "Aplicación libre del objetivo aprobado: elegir un único ataque para desplazar una semicorchea, con referencia que demuestre esa elección y conserve cuatro ataques/huecos.",
    "observed": "007-03 mueve una pareja completa;007-04 conserva esa pareja desplazada y mueve además la primera. Respecto deA=02, los offsets0,0.25,2,2.25 pasan todos a0.25,0.5,2.25,2.5. La referencia mueve ambas parejas aunque explanationMd pide elegir una sola pareja o ataque y successCriteria pide un ataque.",
    "correction": "007-03 mueve solo 2.25->2.5 frente a02. 007-04 reinicia explícitamente desde02 y mueve solo .25->.5; los otros tres bloques se conservan. Textos y criterio corresponden a esa única elección.",
    "owner": "composer-rhythm",
    "status": "resolved"
  },
  {
    "issueId": "R-B02-003",
    "severity": "minor",
    "entityType": "stage",
    "entityId": "stage-rhythm-007-01",
    "location": "work/rhythm/stages.json y note-events.json:007-01/02 frente a lesson-rhythm-007.introMd",
    "expected": "Comparación de corcheas con célula de semicorcheas y huecos, manteniendo densidad controlada, como especifica el intro aprobado.",
    "observed": "Base01 ataca a negras en offsets0,1,2,3. Todas duran0.25, pero esa articulación no constituye una célula de ataques a corcheas; no aparece la referencia binaria de corcheas anunciada antes de02.",
    "correction": "007-01 usa cuatro ataques0/.5/2/2.5 y02 usa0/.25/2/2.25, ambos con duración.25, mismo bajo y voicing. Hay contraste real de colocación de corcheas/semicorcheas sin aumentar densidad.",
    "owner": "composer-rhythm",
    "status": "resolved"
  }
]
```

## Limitación y siguiente puerta

Revisión de todas las notas y lectura binaria, **sin escucha ni interpretación física**. No se rehízo piloto/lote1 ni se revisó producción posterior. Devolver las tres incidencias al compositor, regenerar solo afectados/dependientes y volver a revisar antes de aprobar este lote; la puerta técnica y huellas independientes siguen a cargo del maestro.

## Cierre del maestro — revisión de correcciones

Se verificaron las 744 notas de las 12 etapas contra patrones completos: alturas, onsets, duraciones, velocidades, manos y roles. 005 realiza D/G/C/C y A/F/E/E con las rejillas y omisiones anteriores intactas; 006 conserva íntegros sus patrones aprobables; 007 realiza los cuatro mapas0/.5/2/2.5,0/.25/2/2.25,0/.25/2/2.5 y0/.5/2/2.25. Las explicaciones, reinicios A/B y criterios corresponden a los eventos. Sin hallazgos en métricas; los 12 MIDI nuevos coinciden con los JSON. Aprobado musicalmente, sin escucha ni prueba física. No se volvió a delegar revisión.
