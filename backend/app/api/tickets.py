from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import TicketCreate, TicketOut, TicketUpdate
from ..services.ticket_service import service

router = APIRouter(prefix="/api/v1/tickets", tags=["tickets"])


@router.post("", response_model=TicketOut, status_code=status.HTTP_201_CREATED)
def create_ticket(payload: TicketCreate, db: Session = Depends(get_db)):
    return service.create(db, payload)


@router.get("", response_model=list[TicketOut])
def list_tickets(
    category: str | None = Query(default=None),
    priority: str | None = Query(default=None),
    status_value: str | None = Query(default=None, alias="status"),
    db: Session = Depends(get_db),
):
    return service.list(db, category=category, priority=priority, status=status_value)


@router.patch("/{ticket_id}", response_model=TicketOut)
def update_ticket(ticket_id: int, payload: TicketUpdate, db: Session = Depends(get_db)):
    ticket = service.update(db, ticket_id, payload)
    if not ticket:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return ticket
