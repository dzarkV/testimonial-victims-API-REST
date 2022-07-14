from fastapi import APIRouter, HTTPException
from models.persona import Persona
from config.database import collection
from schemas.persona import personaEntity, personasEntity

persona = APIRouter()

@persona.get('/testimonios', response_model=list[Persona], tags=['personas'], description="Obtiene los 42 testimonios del Libro de las anticipaciones.")
async def find_all_persona()->list:
    return personasEntity(collection.find())

@persona.get('/testimonios/{id}', response_model=Persona, tags=['personas'], description="Obtiene el testimonio según su identificador. Actualmente solo hay 42 testimonios.")
async def find_persona(id: int)->dict:
    if id > collection.estimated_document_count():
        raise HTTPException(status_code=404, detail = f"No hay personas en el testimonio con el id {id}.")
    return personaEntity(collection.find_one({"id": id}))