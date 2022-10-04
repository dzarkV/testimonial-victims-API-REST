from fastapi import APIRouter, HTTPException, Query, Path
from typing import List, Union
from config.meilisch import index_search

search = APIRouter()

# End point para búsqueda de texto en los testimonios
@search.get(
    "/search",
    tags=["buscar"],
    description="Permite buscar en el texto de los testimonios",
)
async def search_by_text(
    q: str = Query(
        ..., description="Ingrese la palabra que desea buscar en los testimonios"
    )
) -> dict:
    result = index_search.search(q)
    if result["estimatedTotalHits"] == 0:
        raise HTTPException(
            status_code=404,
            detail={"message": "word not found in testimonies", "query": f"{q}"},
        )
    return result
