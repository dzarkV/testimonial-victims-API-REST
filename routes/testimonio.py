from fastapi import APIRouter, Response, Query, Path
from models.testimonio import Testimonio
from typing import List, Union
from config.database import collection
from schemas.testimonio import testimonioEntity, testimoniosEntity

testimonio = APIRouter()

# End point para todos los testimonios, con parametro de query de limite 
@testimonio.get('/testimonios', response_model=List[Testimonio],
                 tags=['testimonios'], description="Obtiene los 42 testimonios del Libro de las anticipaciones.")
async def find_all_testimonio(limit: int = Query(42, gt=0, le=42, description="Limite de testimonios"), 
                                persons: bool = Query(True, description="Personas del testimonio"),
                                organizations: bool = Query(True, description="Organizaciones del testimonio"),
                                locations: bool = Query(True, description="Lugares del testimonio"),
                                keyWords: bool = Query(True, description="Palabras clave del testimonio"))->list:
    
    allTestimonies = testimoniosEntity(collection.find({"id": { "$lte": limit }}).sort("id"))
    if persons == False:
        del_atribute(allTestimonies, 'personas')
    if organizations == False:
        del_atribute(allTestimonies, 'organizaciones')
    if locations == False:
        del_atribute(allTestimonies, 'lugares')
    if keyWords == False:
        del_atribute(allTestimonies, 'palabras_clave')
    return allTestimonies

# End point para testimonios según id, con parametro de path de id
@testimonio.get('/testimonios/{id}', response_model=Union[Testimonio, str], tags=['testimonios'], 
                description="Obtiene el testimonio según su identificador. Actualmente solo hay 42 testimonios.")
async def find_testimonio(id: int = Path(..., gt=0, le=42),
                            persons: bool = Query(True, description="Personas del testimonio"),
                            organizations: bool = Query(True, description="Organizaciones del testimonio"),
                            locations: bool = Query(True, description="Lugares del testimonio"),
                            keyWords: bool = Query(True, description="Palabras clave del testimonio"))->dict:

    selectedTestimony = testimonioEntity(collection.find_one({"id": id}))
    if persons == False:
        del selectedTestimony['personas']
    if organizations == False:
        del selectedTestimony['organizaciones']
    if locations == False:
        del selectedTestimony['lugares']
    if keyWords == False:
        del selectedTestimony['palabras_clave']
    return selectedTestimony

#Borra los atributos no requeridos de los testimonios
def del_atribute(l:list, atribute:str)->list:
    for i in l:
        del i[atribute]
    return l
    
    