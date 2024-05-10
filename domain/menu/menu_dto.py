from pydantic import BaseModel


class Menu(BaseModel):
    name: str
    price: float
    description: str
    categoryName: str
    imagePath: str
