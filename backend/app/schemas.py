from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, EmailStr, Field

Category = Literal["Acceso", "Soporte técnico", "Facturación", "Comercial", "Administrativo", "Otros"]
Priority = Literal["Baja", "Media", "Alta"]
Status = Literal["Pendiente", "En atención", "Resuelto"]


class TicketCreate(BaseModel):
    requester_name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    subject: str = Field(min_length=3, max_length=200)
    description: str = Field(min_length=5, max_length=4000)


class TicketUpdate(BaseModel):
    predicted_category: Category | None = None
    predicted_priority: Priority | None = None
    status: Status | None = None


class TicketOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    requester_name: str
    email: str
    subject: str
    description: str
    predicted_category: Category
    predicted_priority: Priority
    confidence: float
    manual_review: bool
    status: Status
    created_at: datetime
    updated_at: datetime
