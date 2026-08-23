from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app

engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def test_create_ticket():
    payload = {
        "requester_name": "Juan Pérez",
        "email": "juan@example.com",
        "subject": "No puedo ingresar",
        "description": "El sistema rechaza mi contraseña y necesito trabajar hoy",
    }
    response = client.post("/api/v1/tickets", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] is not None
    assert data["status"] == "Pendiente"
    assert data["predicted_category"] is not None
    assert data["predicted_priority"] is not None


def test_list_tickets():
    response = client.get("/api/v1/tickets")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
