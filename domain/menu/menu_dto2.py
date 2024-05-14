from pydantic import BaseModel


class Menu2(BaseModel):
    id: int
    name: str
    price: float
    description: str
    categoryName: str
