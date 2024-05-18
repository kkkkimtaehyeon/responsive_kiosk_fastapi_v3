from fastapi import APIRouter
from .search_keyword_dto import SearchKeywords
from .search_service import search_menu_by_keywords
from AI_domain.functions.search_menu import convert_to_searchform

router = APIRouter(
    prefix="/fast/api/search",
    tags=["face-recognition"]
)


@router.post("")
async def search_menu(search_keywords:SearchKeywords):
    result = search_menu_by_keywords(search_keywords.ingredients)
    #result = search_keywords.ingredients
    #result = convert_to_searchform(search_keywords.ingredients)

    return result




