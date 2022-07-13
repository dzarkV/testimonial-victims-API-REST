from fastapi import APIRouter, HTTPException
from models.testimonio import Testimonio
from config.database import collection
from schemas.testimonio import testimonioEntity, testimoniosEntity

testimonio = APIRouter()

@testimonio.get('/testimonios', response_model=list[Testimonio], tags=['testimonios'])
async def find_all_testimonio()->list:
    return testimoniosEntity(collection.find())

@testimonio.get('/testimonios/{id}', response_model=Testimonio, tags=['testimonios'])
async def find_testimonio(id: int)->dict:
    if id > collection.estimated_document_count():
        raise HTTPException(status_code=404, detail = f"No hay testimonio con el id {id}.")
    return testimonioEntity(collection.find_one({"id": id}))
    