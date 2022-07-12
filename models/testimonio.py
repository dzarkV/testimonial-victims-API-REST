from typing import Optional
from pydantic import BaseModel

class Testimonio(BaseModel):
    id: Optional[int]
    title: str
    text: str
    personas: list
    organizaciones: list
    lugares: list
    palabras_clave: list