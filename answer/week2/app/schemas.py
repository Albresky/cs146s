from pydantic import BaseModel
from typing import List, Optional

class NoteBase(BaseModel):
    content: str

class NoteCreate(NoteBase):
    pass

class NoteRead(NoteBase):
    id: int
    created_at: Optional[str] = None

class ActionItemBase(BaseModel):
    text: str
    done: bool = False

class ActionItemCreate(BaseModel):
    text: str
    note_id: Optional[int] = None

class ActionItemRead(ActionItemBase):
    id: int
    note_id: Optional[int] = None
    created_at: Optional[str] = None

class ExtractRequest(BaseModel):
    text: str
    save_note: bool = True
    use_llm: bool = False

class ExtractResponse(BaseModel):
    note_id: Optional[int] = None
    items: List[ActionItemRead]

class MarkDoneRequest(BaseModel):
    done: bool
