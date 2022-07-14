from pydantic import BaseModel

class Persona(BaseModel):
    title: str
    personas: list
