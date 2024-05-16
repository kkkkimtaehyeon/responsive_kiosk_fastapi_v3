from fastapi import APIRouter
from search_keyword_dto import SearchKeywords
from search_service import search_menu_by_keywords


from domain.ai_order.order_service import order

router = APIRouter(
    prefix="/fast/api/search",
    tags=["face-recognition"]
)



@router.post("")
async def search_menu(search_keywords:SearchKeywords):
    result = search_menu_by_keywords(search_keywords)
    # example
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




