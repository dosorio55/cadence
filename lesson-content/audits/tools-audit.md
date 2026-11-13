# Auditoría independiente de herramientas — primera etapa

Alcance: especificación completa, ponytail, README, cuatro scripts, siete schemas y todas las pruebas. Sin cambios en herramientas, contrato ni contenido. No constituye aprobación curricular: referencia de etapa, 19 lecciones musicalizadas aprobadas y 90 fichas de diseño; producción concurrente no recontada.

## Incidencias (§8.3)

```json
{
  "issueId": "TOOLS-001",
  "severity": "major",
  "entityType": "tool",
  "entityId": "export-midi",
  "location": "curriculum/scripts/curriculum.py:373-374; curriculum/schema/note-events.schema.json:15-31",
  "expected": "Exportar los enteros válidos según JSON Schema, incluidas representaciones como 60.0.",
  "observed": "validate batch acepta midi=60.0 o velocity=80.0; export-midi termina con código 2: 'float' object cannot be interpreted as an integer.",
  "correction": "Maestro verificó normalización a int al serializar midi/velocity/numerator ya validados. Regresión CLI con floats enteros produce bytes correctos y sigue rechazando 60.5; suite completa 27/27.",
  "owner": "technical",
  "status": "resolved"
}
```

Prueba: `test_curriculum.fixture()` en TemporaryDirectory; convertir únicamente `note-events[0].midi` a float, validar y exportar `prog-x-1`. Repetir con velocity. Ambos validan sin errores y fallan al exportar; control entero exporta y termina en tick 3840. La prevalidación CLI **no** elimina este fallo.

```json
{
  "issueId": "TOOLS-002",
  "severity": "major",
  "entityType": "approvalGate",
  "entityId": "audit_approvals",
  "location": "curriculum/scripts/audit_delivery.py:182-210,341",
  "expected": "Bloquear la entrega mientras existan incidencias blocker/major abiertas (§8.3, §13).",
  "observed": "El gate comprueba fingerprints y revisiones, pero nunca consulta reports/issues.json; devuelve aprobación con una major abierta.",
  "correction": "Maestro agregó consulta obligatoria de issues.json en audit_approvals: blocker/major no resolved rechazan entrega; regresión cubre ambas severidades, major cerrada, minor abierta y hash de revisión alterada. Suite completa 27/27.",
  "owner": "master",
  "status": "resolved"
}
```

Prueba aislada: `complete_global()`, revisión approved, cobertura/fingerprints completos; añadir incidencia major/open a issues.json. `audit_approvals` devuelve `lessonsCovered: 90`. Cambiar la revisión sin actualizar su hash sí bloquea. Registro y freeze sintéticos exclusivamente temporales; ninguno real modificado.

## Comprobaciones y límites

26/26 pruebas pasan (`PYTHONDONTWRITEBYTECODE=1 curriculum/.venv/bin/python -m unittest discover -s curriculum/tests -v`). Probes temporales adicionales: MIDI positivo, ciclos, huérfanos, orden duplicado, evento fuera del loop, BPM 181, idempotencia y `audit_sql` global sintético: resultados esperados. Suite confirma rollback DDL/DML y prerrequisitos ordenados.

MIDI 128 sí queda bloqueado por prevalidación CLI. No se reportan formatos ajenos al SMF0 del exportador como defectos del lector privado. Sin escucha, auditoría musical, integración productiva ni veredicto curricular final. Las dos incidencias anteriores fueron cerradas posteriormente por el maestro; ver evidencia abajo.

## Cierre verificado por el maestro

Único revisor desde el cambio de coordinación solicitado. Ambas reproducciones tienen regresión y pasan con `curriculum/.venv/bin/python -m unittest discover -s curriculum/tests -v` (27/27). Se revisaron los cambios reales del compositor técnico; se corrigió un literal de bytes mal escapado en su prueba. No hubo cambios de esquemas, contrato ni piloto. Esto no constituye aprobación global del currículo.

## Cierre de integración global — TOOLS-003

La primera integración productiva detectó reserialización del diseño congelado, sin cambio semántico. Se restauraron las huellas exactas desde respaldos y se corrigió `assemble`: sobre el mismo directorio de diseño solo escribe las cuatro tablas musicales. La regresión verifica preservación byte por byte y contenido musical; el contrato, los registros aprobados y las revisiones no cambian.

```json
{
  "issueId": "TOOLS-003",
  "severity": "major",
  "entityType": "tool",
  "entityId": "integrate-in-place",
  "location": "curriculum/scripts/integrate.py:126-131; curriculum/tests/test_integration.py:43-62",
  "expected": "Integrar en el directorio de diseño conserva byte por byte los tres JSON congelados.",
  "observed": "write_data volvía a serializar el diseño al integrar sobre data. La primera auditoría global rechazó skills.json; el formato de lessons.json también cambió, sin alterar registros.",
  "correction": "Se restauraron los SHA originales: skills desde global-parent-backup y lessons desde pending-013/checks de acompañamiento, cuyo hash coincide exactamente con el freeze. La integración in situ ahora escribe solo las cuatro tablas musicales; prueba de regresión conserva bytes y comprueba unión.",
  "owner": "master",
  "status": "resolved"
}
```
