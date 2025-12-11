from __future__ import annotations

from typing import List

from fastapi import APIRouter, HTTPException

from .. import db
from ..schemas import NoteCreate, NoteRead


router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("", response_model=NoteRead)
def create_note(payload: NoteCreate) -> NoteRead:
    note_id = db.insert_note(payload.content)
    note = db.get_note(note_id)
    if not note:
        raise HTTPException(status_code=500, detail="Failed to create note")
    return NoteRead(
        id=note["id"],
        content=note["content"],
        created_at=note["created_at"],
    )


@router.get("/{note_id}", response_model=NoteRead)
def get_single_note(note_id: int) -> NoteRead:
    row = db.get_note(note_id)
    if row is None:
        raise HTTPException(status_code=404, detail="note not found")
    return NoteRead(
        id=row["id"],
        content=row["content"],
        created_at=row["created_at"],
    )


@router.get("", response_model=List[NoteRead])
def list_notes() -> List[NoteRead]:
    rows = db.list_notes()
    return [
        NoteRead(
            id=row["id"],
            content=row["content"],
            created_at=row["created_at"],
        )
        for row in rows
    ]


