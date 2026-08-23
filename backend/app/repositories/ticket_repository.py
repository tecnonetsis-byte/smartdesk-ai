from sqlalchemy import select
from sqlalchemy.orm import Session
from ..models import Ticket


class TicketRepository:
    def create(self, db: Session, ticket: Ticket) -> Ticket:
        db.add(ticket)
        db.commit()
        db.refresh(ticket)
        return ticket

    def list(self, db: Session, *, category: str | None = None, priority: str | None = None, status: str | None = None) -> list[Ticket]:
        stmt = select(Ticket).order_by(Ticket.created_at.desc())
        if category:
            stmt = stmt.where(Ticket.predicted_category == category)
        if priority:
            stmt = stmt.where(Ticket.predicted_priority == priority)
        if status:
            stmt = stmt.where(Ticket.status == status)
        return list(db.scalars(stmt).all())

    def get(self, db: Session, ticket_id: int) -> Ticket | None:
        return db.get(Ticket, ticket_id)

    def save(self, db: Session, ticket: Ticket) -> Ticket:
        db.add(ticket)
        db.commit()
        db.refresh(ticket)
        return ticket
