from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

class Notes(BaseModel):
    id: int
    text: str

class NoteIn(BaseModel):
    text: str

