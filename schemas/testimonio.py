def testimonioEntity(item)->dict:
    return {
        "id": item["id"],
        "title": item["value"]["name"],
        "text": item["value"]["content"],
        "personas": item["value"]["persona"],
        "organizaciones": item["value"]["organizacion"],
        "lugares": item["value"]["lugar"],
        "palabras_clave": item["value"]["palabras_clave"]
    }
