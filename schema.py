from pydantic import BaseModel


class Notes(BaseModel):
    text: str

    class Config:
        orm_mode = True