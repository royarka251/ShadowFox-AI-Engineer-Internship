
import gradio as gr

from api.vector_store import SimpleVectorStore
from api.rag import index_file, ask_question

store = SimpleVectorStore()


def upload_document(file_path):
    if not file_path:
        return "Please upload a TXT or Markdown document."

    try:
        count = index_file(file_path, store)
        return f"Document indexed successfully. Chunks: {count}"
    except Exception as exc:
        return f"Could not process document: {exc}"


def query_document(question):
    if not question.strip():
        return "Please enter a question.", ""

    answer, results = ask_question(question, store)

    sources = "\n\n".join(
        f"Source: {item['source']}\n{item['text'][:500]}"
        for item in results
    )

    return answer, sources


with gr.Blocks(title="Advanced RAG Assistant Lite") as demo:
    gr.Markdown("# Advanced RAG Assistant")
    gr.Markdown("Upload a TXT or Markdown document and search its contents.")

    file_input = gr.File(
        label="Upload document",
        type="filepath",
        file_types=[".txt", ".md"]
    )
    upload_button = gr.Button("Index Document")
    upload_status = gr.Textbox(label="Upload Status")

    question = gr.Textbox(label="Your question")
    ask_button = gr.Button("Find Answer")
    answer = gr.Textbox(label="Answer", lines=6)
    sources = gr.Textbox(label="Retrieved Context", lines=8)

    upload_button.click(
        upload_document,
        inputs=file_input,
        outputs=upload_status
    )

    ask_button.click(
        query_document,
        inputs=question,
        outputs=[answer, sources]
    )


if __name__ == "__main__":
    demo.launch()
