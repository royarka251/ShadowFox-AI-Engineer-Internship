
def answer_question(question, search_results):
    """Return a response grounded in retrieved document text."""
    if not question.strip():
        return "Please enter a question."

    if not search_results:
        return "No relevant information was found in the uploaded documents."

    context = "\n\n".join(
        item["text"] for item in search_results
    )

    return (
        "Relevant information from your documents:\n\n"
        + context
        + "\n\nNote: This basic version retrieves text; "
          "it does not generate an LLM-based answer."
    )
