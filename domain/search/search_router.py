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
    result = order(convert_to_searchform(search_keywords.ingredients))
    # result = [
    #     {
    #         "id": 1
    #     },
    #     {
    #         "id": 2
    #     },
    #     {
    #         "id":3
    #     }
    # ]

    return result


def convert_to_searchform(ingredients):
    ingredients_str = ', '.join(ingredients)
    return f'[${ingredients_str}]'

