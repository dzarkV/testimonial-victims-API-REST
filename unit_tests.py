from schemas.lugar import lugaresEntity
from routes.search import search_by_text


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

    async def test_routes_search(self):
        testOkSearch = {"hits": [
                          {"id": 32,
                            "titulo": "Tomar la delantera",
                            "texto": "Ya hacía tres años que había construido mi rancho allá... Por llegar más rápido, yo siempre me iba por un camino de atajo que dicen; y ahí estaba la bomba. Cuando nosotros llegamos ahí no había ni el perro, solo polvo. \nY ya, no nos siguió más el perrito. \n\n"
                          }
                        ],
                        "estimatedTotalHits": 1,
                        "query": "ELN",
                        "limit": 20,
                        "offset": 0,
                        "processingTimeMs": 81
                        }
        resultTest = await search_by_text(q="ELN")
        assert (resultTest == testOkSearch)

    async def test_routes_search2(self):
        testOkSearch2 = {"detail": {
                            "message": "word not found in testimonies",
                            "query": "00000000"}
                        }
        resultTest2 = await search_by_text(q="00000000")
        assert (resultTest2 == testOkSearch2)