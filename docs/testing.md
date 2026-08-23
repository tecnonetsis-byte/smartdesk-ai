# Estrategia de pruebas

## Unit tests
Las pruebas unitarias comprueban que el clasificador:
- siempre devuelva una categoría permitida;
- siempre devuelva una prioridad permitida;
- mantenga la confianza entre 0 y 1;
- marque revisión manual cuando la confianza sea inferior al 60 %.

## Integration tests
Las pruebas de integración utilizan `TestClient` de FastAPI y una base SQLite en memoria para comprobar el flujo completo de creación y listado de solicitudes.

## Ejecución
```bash
pytest -v
```
