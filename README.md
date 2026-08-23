# SmartDesk AI

Sistema inteligente para registrar, clasificar y priorizar solicitudes de soporte empresarial.

## Problema
La clasificación manual de solicitudes puede producir demoras, criterios inconsistentes y dificultad para identificar rápidamente casos prioritarios.

## Solución
SmartDesk AI analiza el asunto y la descripción de cada solicitud mediante procesamiento de lenguaje natural y propone:
- categoría;
- prioridad;
- nivel de confianza;
- revisión manual cuando la confianza es baja.

La IA funciona como apoyo a la decisión; un operador puede corregir la clasificación.

## Tecnologías
- **Frontend:** React + Vite
- **Backend:** Python + FastAPI
- **Persistencia:** SQLite + SQLAlchemy
- **IA:** scikit-learn, TF-IDF y Regresión Logística
- **Pruebas:** pytest + FastAPI TestClient
- **Especificaciones:** Kiro (`Requirements`, `Design`, `Tasks`)
- **Versionado:** Git + GitHub

## Estructura
```text
smartdesk-ai/
├── .kiro/specs/smartdesk-ai/
│   ├── requirements.md
│   ├── design.md
│   └── tasks.md
├── backend/
├── frontend/
├── data/
├── docs/
├── .github/
├── README.md
└── pytest.ini
```

## Ejecutar backend
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r backend/requirements.txt
uvicorn app.main:app --reload --app-dir backend
```

API: `http://localhost:8000`
Documentación Swagger: `http://localhost:8000/docs`

## Ejecutar frontend
```bash
cd frontend
npm install
npm run dev
```

Frontend: `http://localhost:5173`

## Ejecutar pruebas
Desde la raíz del proyecto:
```bash
pytest -v
```

## Endpoints principales
- `GET /health`
- `POST /api/v1/tickets`
- `GET /api/v1/tickets`
- `PATCH /api/v1/tickets/{id}`

## Especificaciones Kiro
Los artefactos se encuentran en:
```text
.kiro/specs/smartdesk-ai/
```

Incluyen:
- `requirements.md`
- `design.md`
- `tasks.md`

## Flujo Git recomendado
```text
main
└── develop
    ├── feature/kiro-specs
    ├── feature/backend-api
    ├── feature/ai-classifier
    ├── feature/frontend
    ├── feature/tests
    └── docs/architecture
```

## Autor
**[NOMBRE COMPLETO]**  
Diplomado en Desarrollo de Software Inteligente: Aplicaciones con IA para Negocios Digitales.
