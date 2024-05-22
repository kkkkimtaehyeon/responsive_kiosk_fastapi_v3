# checked
from fastapi import APIRouter, HTTPException
from domain.menu.menu_dto2 import Menu2
from domain.menu import menu_service

router = APIRouter(
    prefix="/fast/api/menus",
    tags=["stt"]
)


# 메뉴 추가
@router.post("")
async def add_menu(menu:Menu2):

    menu_service.add_menu(menu)
    return {"message" : f"{menu} has been successfuly added!!"}

#메뉴 삭제
@router.delete("/{id}")
async def delete_menu(id: int):
    try:
        #menu_service.delete_menu(id)
        return {"message": f"menu id: {id} has been successfully deleted!!"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


