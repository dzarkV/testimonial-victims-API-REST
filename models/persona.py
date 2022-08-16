from pydantic import BaseModel
from typing import Optional, List

class Persona(BaseModel):
    id: Optional[int]
    personas: list
