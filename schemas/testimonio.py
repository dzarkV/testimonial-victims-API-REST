def testimonioEntity(item)->dict:
    return {
        "id": item["id"],
        "titulo": item["value"]["name"],
        "texto": item["value"]["content"],
        "personas": item["value"]["persona"],
        "organizaciones": item["value"]["organizacion"],
        "lugares": item["value"]["lugar"],
        "palabras_clave": item["value"]["palabra_clave"]
    }

def testimoniosEntity(item)->list:
    return [testimonioEntity(i) for i in item ]