from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import csv

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


ALLOWED_CATEGORIES = [
    "Acceso",
    "Soporte técnico",
    "Facturación",
    "Comercial",
    "Administrativo",
    "Otros",
]
ALLOWED_PRIORITIES = ["Baja", "Media", "Alta"]


@dataclass(frozen=True)
class ClassificationResult:
    category: str
    priority: str
    confidence: float
    manual_review: bool


class TicketClassifier:
    def __init__(self, dataset_path: str | Path | None = None):
        default_path = Path(__file__).resolve().parents[3] / "data" / "training_tickets.csv"
        self.dataset_path = Path(dataset_path or default_path)
        self.category_model = self._new_pipeline()
        self.priority_model = self._new_pipeline()
        self._train()

    @staticmethod
    def _new_pipeline() -> Pipeline:
        return Pipeline(
            [
                ("tfidf", TfidfVectorizer(ngram_range=(1, 2), lowercase=True, strip_accents="unicode")),
                ("clf", LogisticRegression(max_iter=1200, random_state=42)),
            ]
        )

    def _train(self) -> None:
        rows = []
        with self.dataset_path.open("r", encoding="utf-8", newline="") as fh:
            rows = list(csv.DictReader(fh))

        texts = [row["text"] for row in rows]
        categories = [row["category"] for row in rows]
        priorities = [row["priority"] for row in rows]

        self.category_model.fit(texts, categories)
        self.priority_model.fit(texts, priorities)

    def predict(self, text: str) -> ClassificationResult:
        category = str(self.category_model.predict([text])[0])
        priority = str(self.priority_model.predict([text])[0])

        cat_prob = float(self.category_model.predict_proba([text]).max())
        pri_prob = float(self.priority_model.predict_proba([text]).max())
        confidence = round(min(cat_prob, pri_prob), 4)

        return ClassificationResult(
            category=category,
            priority=priority,
            confidence=confidence,
            manual_review=confidence < 0.60,
        )


classifier = TicketClassifier()
