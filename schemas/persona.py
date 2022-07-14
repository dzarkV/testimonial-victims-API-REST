def personaEntity(item)->dict:
    return {
        "text": item["value"]["content"],
        "personas": item["value"]["persona"],
    }

def personasEntity(item)->list:
    return [personaEntity(i) for i in item ]