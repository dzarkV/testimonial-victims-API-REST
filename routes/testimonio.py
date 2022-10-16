from fastapi import APIRouter, Query, Path
from models.testimonio import Testimonio
from typing import List, Union
from config.database import collection
from schemas.testimonio import testimonioEntity, testimoniosEntity

testimonio = APIRouter()

# End point para todos los testimonios, con parametro de query de limite y skip
@testimonio.get(
    "/testimonios",
    response_model=List[Testimonio],
    response_model_exclude_none=True,
    tags=["testimonios"],
    description="Obtiene los 42 testimonios del Libro de las anticipaciones.",
)
async def find_all_testimonio(
    skip: int = Query(1, gt=0, le=42, description="Limite mínimo de testimonios"),
    limit: int = Query(42, gt=0, le=42, description="Limite máximo de testimonios"),
    all_ner: bool = Query(False, description="Testimonios con todos los atributos NER"),
) -> list:
    if all_ner:
        return testimoniosEntity(
            collection.find({"id": {"$gte": skip, "$lte": limit}}).sort("id")
        )
    else:
        return testimoniosEntity(
            collection.find(
                {"id": {"$gte": skip, "$lte": limit}},
                {"id": 1, "value.content": 1, "value.name": 1},
            ).sort("id")
        )


# End point para testimonios según id, con parametro de path de id
@testimonio.get(
    "/testimonios/{id}",
    response_model=Union[Testimonio, str],
    tags=["testimonios"],
    response_model_exclude_none=True,
    description="Obtiene el testimonio según su identificador. Actualmente solo hay 42 testimonios.",
)
async def find_testimonio(
    id: int = Path(..., gt=0, le=42),
    persons: bool = Query(True, description="Personas del testimonio"),
    organizations: bool = Query(True, description="Organizaciones del testimonio"),
    locations: bool = Query(True, description="Lugares del testimonio")
) -> dict:

    selectedTestimony = testimonioEntity(collection.find_one({"id": id}))
    if persons == False:
        del selectedTestimony["personas"]
    if organizations == False:
        del selectedTestimony["organizaciones"]
    if locations == False:
        del selectedTestimony["lugares"]
    return selectedTestimony


# Borra los atributos no requeridos de los testimonios
def del_atribute(l: list, atribute: str) -> list:
    for i in l:
        del i[atribute]
    return l
