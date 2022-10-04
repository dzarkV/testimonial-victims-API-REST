from typing import Optional
from pydantic import BaseModel


class Testimonio(BaseModel):
    id: Optional[int]
    titulo: str
    texto: str
    personas: Optional[list]
    organizaciones: Optional[list]
    lugares: Optional[list]
    palabras_clave: Optional[list]
