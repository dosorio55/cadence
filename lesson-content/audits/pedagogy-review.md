# Revisión pedagógica — cierre de fase B

## Resultado y límites

Entrega: **6 categorías, 30 skills, 90 lecciones**; cinco skills y quince lecciones por categoría. Cada skill reaparece tres veces con dificultad estrictamente creciente. Órdenes 1–15 e IDs canónicos; 225 enlaces de prerrequisitos sin ciclos. `coverage-map.md` contiene exactamente 90 filas de lección con skill, dependencias, dificultad, extensión y ganancia/autonomía.

Dificultad: 17 lecciones de nivel 1, 30 de nivel 2, 25 de nivel 3, 12 de nivel 4 y 6 de nivel 5. Sesiones de **15–30 minutos**, repetibles: no son promesas de dominio en una visita. La dificultad mide demanda local; las entradas a categorías posteriores pueden requerir conocimientos de otras ramas. El nivel 5 añade decisiones autónomas, no velocidad extrema.

El maestro aprobó categorías y skills; se conservan sin cambios. Lecciones y mapa quedan listos para aprobación de secuencia. Se revisó el diseño escrito, no interpretación, MIDI ni audio; no se escribieron etapas, progresiones o eventos.

## Coherencia y accesibilidad

Las tres apariciones de cada skill avanzan de recurso aislado a contexto y selección propia. Se intercalan cinco hilos, no quince conceptos inconexos ni transposiciones. Todos admiten referencia de cuatro u ocho compases en 4/4 y dos manos. Bajo + acordes o bajo/base + melodía; nunca tres partes independientes obligatorias. En musicalización, mano derecha de máximo una octava simultánea, incluidas notas sostenidas, y ninguna misma altura MIDI solapada entre roles.

Priorizar cinco transformaciones futuras: base, comparación A/B, integración, variación limitada y aplicación autónoma; cuatro si no se pierde un paso necesario. No se han creado registros de etapas. Simplificar reduciendo voces y ataques, sin retirar el objetivo audible.

La colocación pertenece a ritmo; la realización de acordes dados, a acompañamiento; la elección/duración de funciones, a armonía. Melodía construye el discurso; independencia sostiene procesos simultáneos; expresión jerarquiza material conocido.

## Estilos: condiciones de composición

Etiquetas no excluyentes: pop 32, jazz 30, balada 23, funk 4, bolero 3, bossa 3, son 2. No suman 90 por compartir contextos. Se retiró bolero de cadencias genéricas: por sí solas no justifican identidad rítmica.

Bolero comparte bajo uno/tres y respuesta dos, 2& y cuatro como reducción concreta, no patrón universal. Bossa debe compartir una célula de dos compases: acordes en uno, 2& y cuatro; después dos y 3&, con bajo uno/tres. Son conserva orientación de clave 2–3; funk trabaja rejilla y huecos; swing usa referencia ternaria sin declararla proporción universal. El carácter idiomático aún exige revisión del ejemplo compuesto.

## Piloto confirmado

**`lesson-rhythm-004`**, skill **`skill-rhythm-syncopation`**, dificultad 2, 20 minutos. Objetivo: **hacer llegar el acorde siguiente en 4& sin acelerar ni repetirlo en uno**. Requiere R002 y R003.

Reservar cinco transformaciones y cuatro compases de I–vi–ii–V. Comparación A/B: llegada regular frente a frontera interior adelantada de beat 4 a **3.5**; mover bajo, acorde y frontera armónica, terminar antes el acorde previo y sostener la llegada. Evitar anacrusa negativa y cola fuera del loop. Alternativa futura propia: I–V–vi–IV, con sus eventos completos; no transposición. Autonomía: elegir otra frontera interior y justificarla. La composición todavía no existe.

## Aprobación del maestro — fase B

El maestro leyó las seis categorías, las 30 skills, la secuencia completa de títulos/prerrequisitos/dificultades y las 90 filas del mapa. Repitió `validate --mode design` y un cotejo independiente: cada skill tiene tres lecciones con dificultad estrictamente creciente. Se aprueba la secuencia para componer el piloto; esta aprobación no sustituye la revisión de sus eventos ni autoriza todavía producción masiva.

La revisión audible podrá sustituirse por inspección documentada de línea temporal según la especificación si no hay instrumento reproducible disponible; no se afirmará una escucha inexistente.

## Comprobaciones y siguiente puerta

Comando de aceptación desde la raíz:

```sh
curriculum/.venv/bin/python curriculum/scripts/curriculum.py validate --mode design --data curriculum/data
```

Resultado: `Validación correcta`. Se ejecutó además `python3 -c` con asserts independientes de campos exactos, IDs, referencias, conteos, órdenes, DAG y dificultad creciente por skill; otro cotejo comprobó las 90 filas del mapa contra los JSON.

Siguiente puerta: composición del piloto y auditoría de tocabilidad, correspondencia A/B y escucha real. Permanecen sin verificar audio, guajeo idiomático, balance MIDI y transferencia efectiva del alumno; no son fallos ocultos ni aprobaciones de fase C.

## Cierre posterior de producción

Las referencias a composición futura de este documento describen la fase B histórica. La producción posterior está completa: 90 lecciones aprobadas, 400 etapas y 402 progresiones. Se repitió el cotejo de tres lecciones por skill con dificultad estrictamente creciente; diseño y 225 prerrequisitos originales intactos. Las decisiones y diferencias musicales se revisaron por lote y se registraron con huella. La auditoría y sus límites actuales están en `final-audit.md`; no se afirma escucha ni ejecución física.
