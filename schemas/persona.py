def personaEntity(item)->dict:
    return {
        "id": item["id"],
        "personas": item["value"]["persona"],
    }

def personasEntity(item)->list:
    return [personaEntity(i) for i in item ]