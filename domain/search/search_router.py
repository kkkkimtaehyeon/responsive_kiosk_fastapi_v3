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
    return search_script


def generate_search_script(ingredients):
    ingredients = ', '.join(ingredients)
    return f'return menu infos include these keywords {ingredients}'

dummy_data = {
    "id": 1,
    "name" : "americano",
    "price": 3000,
    "imagePath": "https://responsive-bucket.s3.ap-northeast-2.amazonaws.com/americano.jpg"
}