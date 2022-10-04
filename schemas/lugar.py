def lugarEntity(item) -> dict:
    return {
        "id": item["id"],
        "lugares": item["value"]["lugar"],
    }


def lugaresEntity(item) -> list:
    return [lugarEntity(i) for i in item]
