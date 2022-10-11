from schemas.lugar import lugaresEntity
from schemas.persona import personasEntity
# from routes.search import search_by_text


class TestClass():

    def test_schema_lugares(self):
        testOkLugares = [{
                "id": 1,
                "lugares": ["parque", "negocio", "casa"]},
                {
                "id": 2,
                "lugares": ["edificio", "calle", "esquina"]},
                {
                "id": 3,
                "lugares": ["oficina", "cuadra", "selva"]}]
        resultTest = lugaresEntity([
                {"id": 1,
                "value":{
                "lugar": ["parque", "negocio", "casa"]}},
                {"id": 2,
                "value":{
                "lugar": ["edificio", "calle", "esquina"]}},
                {"id": 3,
                "value":{
                "lugar": ["oficina", "cuadra", "selva"]}}
                ])
        assert (resultTest == testOkLugares)

    def test_schema_personas(self):
        testOkPersonas = [{
                "id": 1,
                "personas": ["Lucas", "Margarita", "William"]},
                {
                "id": 2,
                "personas": ["Daniel", "María Sanabria"]}]
        resultTest = personasEntity([
                {"id": 1,
                "value":{
                "persona": ["Lucas", "Margarita", "William"]}},
                {"id": 2,
                "value":{
                "persona": ["Daniel", "María Sanabria"]}}])
        assert (resultTest == testOkPersonas)

#     async def test_routes_search(self):
#         testOkSearch2 = {"detail": {
#                             "message": "word not found in testimonies",
#                             "query": "00000000"}
#                         }
#         resultTest2 = await search_by_text(q="00000000")
#         assert (resultTest2 == testOkSearch2)