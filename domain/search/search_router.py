from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix="/fast/api/search",
    tags=["face-recognition"]
)

class SearchKeywords(BaseModel):
    ingredients: List[str]

@router.post("")
async def search(searchKeywords: SearchKeywords):
    search_script = generate_search_script(searchKeywords.ingredients)

    #received_menus = search_script로 gpt에서 메뉴 데이터 받아오는 함수

    return dummy_data


def generate_search_script(ingredients):
    ingredients = ', '.join(ingredients)
    return f'return menu infos include these keywords {ingredients}'

dummy_data = [
    {
        "id": 1,
        "name": "아메리카노",
        "price": 3000
    },
    {
        "id": 2,
        "name": "카페라떼",
        "price": 3500
    },
    {
        "id": 3,
        "name": "바닐라라떼",
        "price": 3700
    }
]
