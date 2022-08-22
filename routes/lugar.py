from fastapi import APIRouter, Response, Query, Path
from models.lugar import Lugar
from typing import List, Union
from config.database import collection
from schemas.lugar import lugaresEntity 

lugar = APIRouter()

# End point para todos los lugares, con parametro de query de limite y skip
@lugar.get('/lugares', response_model=List[Lugar], #response_model_exclude_none=True,
                 tags=['lugares'], description="Obtiene los lugares de los 42 testimonios del Libro de las anticipaciones.")
async def find_all_places(skip: int = Query(1, gt=0, le=42, description="Limite mínimo de todos los lugares"),
                            limit: int = Query(42, gt=0, le=42, description="Limite de lugares de testimonios"))->list:
    
    allPlaces = lugaresEntity(collection.find({"id": { "$gte": skip, "$lte": limit }}, { "id": 1, "value.lugar": 1 }).sort("id"))
    
    return allPlaces
