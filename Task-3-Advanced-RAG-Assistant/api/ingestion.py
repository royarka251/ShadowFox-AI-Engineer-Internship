
from pathlib import Path


def extract_text(file_path):
    """Extract text from a supported text or Markdown file."""
    path = Path(file_path)
    suffix = path.suffix.lower()

    if suffix in {".txt", ".md"}:
        return path.read_text(encoding="utf-8", errors="ignore")

    raise ValueError(
        "This basic version supports TXT and Markdown files only."
    )


def chunk_text(text, chunk_size=500, overlap=50):
    """Split text into overlapping chunks."""
    if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
        raise ValueError("Invalid chunk_size or overlap.")

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return [chunk for chunk in chunks if chunk.strip()]
