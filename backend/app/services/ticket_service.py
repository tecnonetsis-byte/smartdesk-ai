from sqlalchemy.orm import Session
from ..models import Ticket
from ..schemas import TicketCreate, TicketUpdate
from ..repositories.ticket_repository import TicketRepository
from .classifier import TicketClassifier, classifier


class TicketService:
    def __init__(self, repo: TicketRepository | None = None, ai: TicketClassifier | None = None):
        self.repo = repo or TicketRepository()
        self.ai = ai or classifier

    def create(self, db: Session, payload: TicketCreate) -> Ticket:
        result = self.ai.predict(f"{payload.subject}. {payload.description}")
        ticket = Ticket(
            requester_name=payload.requester_name,
            email=str(payload.email),
            subject=payload.subject,
            description=payload.description,
            predicted_category=result.category,
            predicted_priority=result.priority,
            confidence=result.confidence,
            manual_review=result.manual_review,
            status="Pendiente",
        )
        return self.repo.create(db, ticket)

    def list(self, db: Session, **filters) -> list[Ticket]:
        return self.repo.list(db, **filters)

    def update(self, db: Session, ticket_id: int, payload: TicketUpdate) -> Ticket | None:
        ticket = self.repo.get(db, ticket_id)
        if not ticket:
            return None
        changes = payload.model_dump(exclude_unset=True)
        for field, value in changes.items():
            setattr(ticket, field, value)
        if "predicted_category" in changes or "predicted_priority" in changes:
            ticket.manual_review = False
        return self.repo.save(db, ticket)


service = TicketService()
