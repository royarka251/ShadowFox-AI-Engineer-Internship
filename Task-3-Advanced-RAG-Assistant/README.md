# ShadowFox AI Engineer Internship
## Task 3: Advanced RAG Document Assistant

A document question-answering application designed to retrieve relevant
information from uploaded PDF, TXT, and Markdown files.

### Planned Features
- Multi-format document ingestion
- Text extraction and chunking
- Embedding generation and vector search
- Document-grounded question answering
- Retrieved source context and relevance scores
- FastAPI backend and Streamlit user interface
- Input validation and reproducible setup

### Project Structure
```text
Task-3-Advanced-RAG-Assistant/
├── api/
│   ├── __init__.py
│   ├── ingestion.py
│   ├── vector_store.py
│   ├── qa.py
│   ├── main.py
│   └── ui.py
├── requirements.txt
├── README.md
├── Dockerfile
└── tests/
```

### Installation
```bash
pip install -r requirements.txt
```

### Running the Application
Start the FastAPI backend:
```bash
uvicorn api.main:app --reload
```

Start the Streamlit interface in a separate terminal:
```bash
streamlit run api/ui.py
```

### Testing
Test document upload, retrieval, question answering, source display,
invalid file handling, and questions unsupported by the document.

### Notes
The actual implemented features and configuration should be verified
before deployment. Localhost URLs require a running backend.
