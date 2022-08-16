from typing import Optional, List
from pydantic import BaseModel

class Lugar(BaseModel):
    id: Optional[int]
    lugares: List[str]