from __future__ import annotations

from typing import Any, Dict, List, Optional

from fastapi import APIRouter, HTTPException

from .. import db
from ..services.extract import extract_action_items, extract_action_items_llm
from ..schemas import ExtractRequest, ExtractResponse, ActionItemRead, MarkDoneRequest


router = APIRouter(prefix="/action-items", tags=["action-items"])


@router.post("/extract", response_model=ExtractResponse)
def extract(payload: ExtractRequest) -> ExtractResponse:
    text = payload.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="text is required")

    note_id: Optional[int] = None
    if payload.save_note:
        note_id = db.insert_note(text)

    if payload.use_llm:
        items = extract_action_items_llm(text)
    else:
        items = extract_action_items(text)

    ids = db.insert_action_items(items, note_id=note_id)
    
    response_items = []
    for i, item_text in zip(ids, items):
        response_items.append(ActionItemRead(
            id=i,
            text=item_text,
            note_id=note_id,
            done=False,
            created_at=None # In a real app, we'd fetch this or return what we have
        ))

    return ExtractResponse(note_id=note_id, items=response_items)


@router.post("/extract-llm", response_model=ExtractResponse)
def extract_llm(payload: ExtractRequest) -> ExtractResponse:
    payload.use_llm = True
    return extract(payload)


@router.get("", response_model=List[ActionItemRead])
def list_all(note_id: Optional[int] = None) -> List[ActionItemRead]:
    rows = db.list_action_items(note_id=note_id)
    return [
        ActionItemRead(
            id=r["id"],
            note_id=r["note_id"],
            text=r["text"],
            done=bool(r["done"]),
            created_at=r["created_at"],
        )
        for r in rows
    ]


@router.post("/{action_item_id}/done", response_model=ActionItemRead)
def mark_done(action_item_id: int, payload: MarkDoneRequest) -> ActionItemRead:
    db.mark_action_item_done(action_item_id, payload.done)
    row = db.get_action_item(action_item_id)
    if not row:
        raise HTTPException(status_code=404, detail="Action item not found")
    return ActionItemRead(
        id=row["id"],
        note_id=row["note_id"],
        text=row["text"],
        done=bool(row["done"]),
        created_at=row["created_at"],
    )


