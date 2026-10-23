
from api.ingestion import extract_text, chunk_text
from api.qa import answer_question


def index_file(file_path, store):
    text = extract_text(file_path)
    chunks = chunk_text(text)

    store.add_documents(
        chunks,
        source=file_path
    )

    return len(chunks)


def ask_question(question, store):
    results = store.search(question)
    return answer_question(question, results), results
