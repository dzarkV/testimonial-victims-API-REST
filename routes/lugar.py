from fastapi import APIRouter, Response, Query, Path
from models.lugar import Lugar
from typing import List, Union
from config.database import collection
from schemas.lugar import lugaresEntity 

lugar = APIRouter()

# End point para todos los lugares, con parametro de query de limite 
@lugar.get('/lugares', response_model=List[Lugar], #response_model_exclude_none=True,
                 tags=['lugares'], description="Obtiene los lugares de los 42 testimonios del Libro de las anticipaciones.")
async def find_all_places(limit: int = Query(42, gt=0, le=42, description="Limite de lugares de testimonios"))->list:
    print('entra a la funcion')
    allPlaces = lugaresEntity(collection.find({"id": { "$lte": limit }}, { "id": 1, "value.lugar": 1 }).sort("id"))
    
    return allPlaces
