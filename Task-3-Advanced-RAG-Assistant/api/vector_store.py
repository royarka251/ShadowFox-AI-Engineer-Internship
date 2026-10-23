
from pathlib import Path


class SimpleVectorStore:
    """A basic keyword-search store, not a real vector database."""

    def __init__(self):
        self.documents = []

    def add_documents(self, chunks, source="unknown"):
        for chunk in chunks:
            self.documents.append({
                "text": chunk,
                "source": source
            })

    def search(self, query, limit=3):
        terms = set(query.lower().split())

        results = []
        for document in self.documents:
            text = document["text"]
            words = set(text.lower().split())
            score = len(terms & words)

            if score:
                results.append({
                    **document,
                    "score": score
                })

        return sorted(
            results,
            key=lambda item: item["score"],
            reverse=True
        )[:limit]
