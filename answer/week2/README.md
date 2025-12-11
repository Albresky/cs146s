# Action Item Extractor

A FastAPI application that converts free-form notes into enumerated action items. It supports both heuristic-based extraction and LLM-powered extraction using Ollama.

## Features

- **Note Taking**: Save free-form notes.
- **Action Item Extraction**: Automatically extract action items from notes.
  - **Heuristic**: Uses regex and keyword matching.
  - **LLM**: Uses Ollama (e.g., Llama 3.2) for intelligent extraction.
- **Task Management**: List action items and mark them as done.
- **History**: View past notes.

## Setup and Running

1.  **Prerequisites**:
    - Python 3.10+
    - Poetry
    - Ollama (for LLM features)

2.  **Install Dependencies**:
    ```bash
    poetry install
    ```

3.  **Run the Application**:
    ```bash
    poetry run uvicorn week2.app.main:app --reload
    ```

4.  **Access the App**:
    Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## API Endpoints

### Action Items
- `POST /action-items/extract`: Extract action items. Supports `use_llm` flag.
- `POST /action-items/extract-llm`: Extract action items using LLM.
- `GET /action-items`: List all action items.
- `POST /action-items/{id}/done`: Mark an action item as done.

### Notes
- `POST /notes`: Create a new note.
- `GET /notes`: List all notes.
- `GET /notes/{id}`: Get a specific note.

## Running Tests

To run the unit tests:

```bash
poetry run pytest week2/tests/test_extract.py
```
