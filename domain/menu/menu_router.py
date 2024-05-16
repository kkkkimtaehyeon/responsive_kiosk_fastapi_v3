# checked
from fastapi import APIRouter
from domain.menu.menu_dto2 import Menu2
from domain.menu import menu_service

router = APIRouter(
    prefix="/fast/api/menu-register",
    tags=["stt"]
)


# 메뉴 추가
@router.post("")
async def add_menu(menu:Menu2):

    menu_service.add_menu(menu)
    return {"message" : f"{menu} has been successfuly added!!"}



