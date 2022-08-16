from fastapi import APIRouter, HTTPException, Query
from models.persona import Persona
from typing import List
from config.database import collection
from schemas.persona import personasEntity

persona = APIRouter()

# End point para todas las personas, con parametro de query de limite 
@persona.get('/personas', response_model=List[Persona], 
                tags=['personas'], description="Obtiene las personas de los testimonios del Libro")
async def find_all_people(limit: int = Query(42, gt=0, le=42, description="Limite de las personas en los testimonios"))->list:
    allPeople = personasEntity(collection.find({"id": { "$lte": limit }}, { "id": 1, "value.persona": 1 }).sort("id"))
    return allPeople

# @persona.get('/testimonios/{id}', response_model=Persona, tags=['personas'], description="Obtiene el testimonio según su identificador. Actualmente solo hay 42 testimonios.")
# async def find_persona(id: int)->dict:
    # if id > collection.estimated_document_count():
        # raise HTTPException(status_code=404, detail = f"No hay personas en el testimonio con el id {id}.")
    # return personaEntity(collection.find_one({"id": id}))