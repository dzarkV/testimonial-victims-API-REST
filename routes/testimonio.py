from fastapi import APIRouter, Response
from models.testimonio import Testimonio
from typing import List, Union
from config.database import collection
from schemas.testimonio import testimonioEntity, testimoniosEntity

testimonio = APIRouter()

@testimonio.get('/testimonios', response_model=List[Testimonio],
                 tags=['testimonios'], description="Obtiene los 42 testimonios del Libro de las anticipaciones.")
async def find_all_testimonio(limit: int = 42)->list:
    if limit:
        return testimoniosEntity(collection.find({"id": { "$lte": limit } } )) 
    return testimoniosEntity(collection.find())

@testimonio.get('/testimonios/{id}', response_model=Union[Testimonio, str], tags=['testimonios'], 
                description="Obtiene el testimonio según su identificador. Actualmente solo hay 42 testimonios.")
async def find_testimonio(id: int, response: Response)->dict:
    if id > collection.estimated_document_count():
        response.status_code=404
        return f"No hay testimonio con el id {id}."
    return testimonioEntity(collection.find_one({"id": id}))
    