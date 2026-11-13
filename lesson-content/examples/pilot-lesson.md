# Piloto: anticipar la llegada en cuatro y

Lección `lesson-rhythm-004` · habilidad `skill-rhythm-syncopation` · pop, 4/4, 80 BPM. Cada ejemplo es de cuatro compases (16 negras; 15 360 ticks a PPQ 960). El bajo izquierdo y el acorde derecho atacan juntos. Compara cada versión con los cambios en el uno: una anticipación cambia el mapa armónico, no es solo mover una nota.

## Etapas y reproducción

Todos los principales son autocontenidos; carga IDs desde `lesson-content/examples/pilot-data/progressions.json` y sus eventos. Comando desde la raíz del repositorio:

```sh
lesson-content/.venv/bin/python lesson-content/tools/scripts/curriculum.py export-midi PROG_ID --data lesson-content/examples/pilot-data --output /tmp/PROG_ID.mid
```

1. **Base** — `stage-rhythm-004-01`, `prog-rhythm-004-01-primary`. I–vi–ii–V inicia en beats 0, 4, 8 y 12. Bajo y bloque derecho atacan en cada cambio y sostienen hasta el siguiente. Criterio: cuatro negras estables y cambios en el uno.
2. **Una anticipación** — `stage-rhythm-004-02`, `prog-rhythm-004-02-primary`. A compara con la etapa 1; B mueve el comienzo armónico de V de beat 12 (compás 4, uno) a 11.5 (compás 3, 4&) y sostiene V hasta el final. Bajo y acorde llegan juntos; **no hay reataque en beat 12**. Criterio: percibir la llegada adelantada sin acelerar.
3. **Combinación** — `stage-rhythm-004-03`, `prog-rhythm-004-03-primary`. Conserva V en 11.5 y además adelanta vi: beat 4 pasa a 3.5 (compás 1, 4&); dura hasta beat 8. Compara con etapa 2 y comprueba ambas llegadas conjuntas.
4. **Variación** — `stage-rhythm-004-04`, `prog-rhythm-004-04-primary`. Conserva los ataques armónicos de etapa 3; solo la duración del bloque derecho se reduce a 1.5 beats. El bajo sigue hasta el próximo cambio. Identifica que no cambió el mapa armónico.
5. **Autonomía/referencia** — `stage-rhythm-004-05`, `prog-rhythm-004-05-primary`. Referencia: anticipa vi en beat 3.5, con ii en 8 y V en 12; se retira la instrucción de combinar anticipaciones. Elige y explica otra llegada: no es una solución única.

La alternativa `prog-rhythm-004-05-alternative-01` usa I–vi–IV–V (Cmaj7–Am7–Fmaj7–G7), no una transposición; vi sigue entrando en beat 3.5 con bajo y acorde juntos. Para A/B final, exporta el principal y la alternativa con el comando anterior y compara sus MIDI.

Métricas: 6 progresiones, 24 eventos de acorde y 120 eventos de nota; las voces derechas simultáneas abarcan como máximo 11 semitonos y cuatro notas. MIDI canal único y no hay alturas simultáneas duplicadas. Se verifican datos/ticks; no se afirma escucha humana.