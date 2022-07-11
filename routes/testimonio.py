from fastapi import APIRouter

testimonio = APIRouter()

@testimonio.get('/all')
async def find_all_testimonio()->list:
    return "Sirve el get all"

@testimonio.get('/id')
async def find_one_testimonio()->dict:
    return "Sirve el get one"