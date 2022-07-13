from fastapi import APIRouter, HTTPException
from models.testimonio import Testimonio
from config.database import collection
from schemas.testimonio import testimonioEntity, testimoniosEntity

testimonio = APIRouter()

@testimonio.get('/testimonios', response_model=list[Testimonio], tags=['testimonios'], description="Obtiene los 42 testimonios del Libro de las anticipaciones.")
async def find_all_testimonio()->list:
    return testimoniosEntity(collection.find())

@testimonio.get('/testimonios/{id}', response_model=Testimonio, tags=['testimonios'], description="Obtiene el testimonio según su identificador. Actualmente solo hay 42 testimonios.")
async def find_testimonio(id: int)->dict:
    if id > collection.estimated_document_count():
        raise HTTPException(status_code=404, detail = f"No hay testimonio con el id {id}.")
    return testimonioEntity(collection.find_one({"id": id}))
    