from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from domain.order.ai_order import order

router = APIRouter(
    prefix="/fast/api/search",
    tags=["face-recognition"]
)

class SearchKeywords(BaseModel):
    ingredients: List[str]

@router.post("")
async def search_menu(search_keywords:SearchKeywords):

    ingredients_str = ','.join(search_keywords.ingredients)
    result = order('[' + ingredients_str + ']')

    return result


def generate_search_script(ingredients):
    ingredients = ', '.join(ingredients)
    return f'Return menu information including these keywords {ingredients}'

