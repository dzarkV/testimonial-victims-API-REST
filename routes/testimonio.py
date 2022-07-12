from fastapi import APIRouter
from config.database import collection
from schemas.testimonio import testimonioEntity, testimoniosEntity

testimonio = APIRouter()

@testimonio.get('/all')
async def find_all_testimonio()->list:
    return testimoniosEntity(collection.find())

@testimonio.get('/all/{id}')
async def find_testimonio(id: int)->dict:
    print(id)
    return testimonioEntity(collection.find_one({"id": id}))