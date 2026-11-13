approved

# Ritmo, lote03 — maestro

Revisadas12etapas,48acordes y296notas nuevas completas, cotejadas además con patrones exhaustivos de cada ataque, altura, duración, velocity, mano y rol.

|Lección|Cuatro etapas verificadas|
|---|---|
|008|Backbeat;bolero1/1.5/3;respuesta máslarga;reset yúnicaomisión. TríadasI–vi–ii–V yblancasLH.|
|009|Tríadas en0;entrada1.5sostenidacruza2;duración2;otraentrada.5cruza2. Sin cambio de armonía ni textura.|
|010|LHparcial;línea a tierra0/1;frasecompleta a2/3y1+2/3;pausa final elegida. F4deV7llegaaE4deI tras el hueco.|

Los textos, criterios e hints corresponden con las referencias y sus reinicios. Sin corcheas rectas ocultas en el swing, manos cómodas y sin solapamientos de tecla.12MIDI coincidentes,métricas0,batchválido y001–007/piloto intactos. Sin escucha ni interpretación física.

```json
[
  {
    "issueId": "R-B03-001",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-rhythm-009",
    "location": "Tríadas, síncopa y comparación",
    "expected": "Misma tríada por acorde, dos blancas LH y solo cambio temporal.",
    "observed": "El borrador repetía Cmayor inclusoenAm/Dm/G ydespués sustituía acordes por una línea al desplazar, alterando texturayritmo a la vez.",
    "correction": "Triadas C/Am/Dm/G verdaderas enlas4etapas;RH0/dur1→1.5/dur1→1.5/dur2→primeronset.5/dur2. Bajo0/2inmutable yfrontera armónica fija.",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "R-B03-002",
    "severity": "major",
    "entityType": "lesson",
    "entityId": "lesson-rhythm-010",
    "location": "Rejilla swing, resolución y autonomía",
    "expected": "Entrada tardía de toda frase ternaria, pausa elegida y armonía compatible.",
    "observed": "La primera nota estaba2/3pero la segunda1.5recta; F→E se repetía dentrode cadaacorde yno se mostraba decisión real.",
    "correction": "ParesF/A,B/F,E/G,E/G sobreDm7/G7/Cmaj7/Cmaj7.02onsets0/1,dur1/3;03desplazaambas2/3;04omitesoloGfinalyseeligeotrofinalsinromperF(V)→E(I).",
    "owner": "master",
    "status": "resolved"
  },
  {
    "issueId": "R-B03-003",
    "severity": "minor",
    "entityType": "lesson",
    "entityId": "lesson-rhythm-008",
    "location": "Duración real de003 yreset004",
    "expected": "Describir el único parámetro que realmente cambia.",
    "observed": "003se llamaba compararacentos perosol oalargabadurRH;004restauraba.25sin explicitarreinicioB.",
    "correction": "003se llama Prolongar respuesta,.25→.5 sinotroscambios;004reset02 explícito yúnicaomisiónúltimobloque. Textos009corrigen2&yblancas0/2.",
    "owner": "master",
    "status": "resolved"
  }
]
```
