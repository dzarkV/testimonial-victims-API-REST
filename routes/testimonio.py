from fastapi import APIRouter

testimonio = APIRouter()

@testimonio.get('/all')
async def find_all_testimonio()->list:
    return "Sirve el get all"

@testimonio.get('/all/{id}')
async def find_testimonio()->dict:
    return "Sirve el get one"