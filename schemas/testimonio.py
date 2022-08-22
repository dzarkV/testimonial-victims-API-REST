def testimonioEntity(item)->dict:
    if len(item["value"].keys()) > 2: # Check si las llaves de item[value] son más de dos para devolver query param all_ner
        return {
            "id": item["id"],
            "titulo": item["value"]["name"],
            "texto": item["value"]["content"],
            "personas": item["value"]["persona"],
            "organizaciones": item["value"]["organizacion"],
            "lugares": item["value"]["lugar"],
            "palabras_clave": item["value"]["palabra_clave"]
        }
    else:
        return {
            "id": item["id"],
            "titulo": item["value"]["name"],
            "texto": item["value"]["content"]
        }

def testimoniosEntity(item)->list:
    return [testimonioEntity(i) for i in item ]