from pydantic import BaseModel


class Menu(BaseModel):
    id: int
    name: str
    price: float
    description: str
    categoryName: str
    imagePath: str
