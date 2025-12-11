import os
import pytest
from unittest.mock import patch, MagicMock

from ..app.services.extract import extract_action_items, extract_action_items_llm


def test_extract_bullets_and_checkboxes():
    text = """
    Notes from meeting:
    - [ ] Set up database
    * implement API extract endpoint
    1. Write tests
    Some narrative sentence.
    """.strip()

    items = extract_action_items(text)
    assert "Set up database" in items
    assert "implement API extract endpoint" in items
    assert "Write tests" in items


@patch("week2.app.services.extract.chat")
def test_extract_llm(mock_chat):
    mock_response = MagicMock()
    mock_response.message.content = '{"items": ["Buy milk", "Walk the dog"]}'
    mock_chat.return_value = mock_response

    text = "I need to buy milk and walk the dog."
    items = extract_action_items_llm(text)

    assert "Buy milk" in items
    assert "Walk the dog" in items
    mock_chat.assert_called_once()


def test_extract_llm_empty():
    text = ""
    items = extract_action_items_llm(text)
    assert items == []


@patch("week2.app.services.extract.chat")
def test_extract_llm_failure(mock_chat):
    mock_chat.side_effect = Exception("Ollama error")

    text = "- [ ] Task 1"
    items = extract_action_items_llm(text)
    assert "Task 1" in items
