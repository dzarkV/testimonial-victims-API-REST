from pydantic import BaseModel
from typing import Optional


class Persona(BaseModel):
    id: Optional[int]
    personas: list
