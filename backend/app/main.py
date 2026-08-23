from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .api.tickets import router as tickets_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SmartDesk AI API",
    version="1.0.0",
    description="API para registro, clasificación y priorización inteligente de solicitudes empresariales.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(tickets_router)
