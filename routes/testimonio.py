from fastapi import APIRouter, Response, Query
from models.testimonio import Testimonio
from typing import List, Union
from config.database import collection
from schemas.testimonio import testimonioEntity, testimoniosEntity

testimonio = APIRouter()

# End point para todos los testimonios, con parametro de query de limite 
@testimonio.get('/testimonios', response_model=List[Testimonio],
                 tags=['testimonios'], description="Obtiene los 42 testimonios del Libro de las anticipaciones.")
async def find_all_testimonio(limit: int = Query(42, description="Limite de testimonios"), 
                                persons: bool = Query(True, description="Personas del testimonio"))->list:
    
    if persons == False:
        return del_atribute(testimoniosEntity(collection.find({"id": { "$lte": limit }}).sort("id")), 'personas')
    return testimoniosEntity(collection.find({"id": { "$lte": limit } }).sort("id"))

# End point para testimonios según id, con parametro de path de id
@testimonio.get('/testimonios/{id}', response_model=Union[Testimonio, str], tags=['testimonios'], 
                description="Obtiene el testimonio según su identificador. Actualmente solo hay 42 testimonios.")
async def find_testimonio(id: int, response: Response)->dict:
    if id > collection.estimated_document_count():
        response.status_code=404
        return f"No hay testimonio con el id {id}."
    return testimonioEntity(collection.find_one({"id": id}))

#Borra los atributos no requeridos de los testimonios
def del_atribute(l:list, atributo:str)->list:
    for i in l:
        del i[atributo]
    return l
    
    