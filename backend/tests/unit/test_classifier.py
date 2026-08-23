from app.services.classifier import ALLOWED_CATEGORIES, ALLOWED_PRIORITIES, TicketClassifier


def test_classifier_returns_valid_category():
    classifier = TicketClassifier()
    result = classifier.predict("No puedo iniciar sesión en mi cuenta")
    assert result.category in ALLOWED_CATEGORIES


def test_classifier_returns_valid_priority():
    classifier = TicketClassifier()
    result = classifier.predict("El sistema dejó de funcionar y necesito enviar un informe urgente")
    assert result.priority in ALLOWED_PRIORITIES


def test_confidence_is_normalized():
    classifier = TicketClassifier()
    result = classifier.predict("Tengo una consulta general")
    assert 0.0 <= result.confidence <= 1.0
    assert result.manual_review == (result.confidence < 0.60)
