# Arquitectura – SmartDesk AI

```mermaid
flowchart LR
    A[Usuario] --> B[React + Vite]
    B -->|REST / JSON| C[FastAPI]
    C --> D[Ticket Service]
    D --> E[AI Classifier]
    E --> F[TF-IDF]
    F --> G[Regresión logística: categoría]
    F --> H[Regresión logística: prioridad]
    D --> I[Ticket Repository]
    I --> J[(SQLite)]
```

## Responsabilidades
- **React + Vite:** experiencia de usuario.
- **FastAPI:** validación, API y documentación.
- **Ticket Service:** lógica de negocio.
- **AI Classifier:** predicción y confianza.
- **Repository:** acceso a datos.
- **SQLite:** persistencia académica.
