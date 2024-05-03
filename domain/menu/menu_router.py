# checked
from fastapi import APIRouter
from domain.menu.menu_dto import Menu

router = APIRouter(
    prefix="/fast/api/menu-register",
    tags=["stt"]
)


# 메뉴 등록 시 GPT 학습
@router.post("/")
async def register_menu(menu: Menu):
    menu_prompt = generate_menu_prompt(menu=menu)
    #GPT한테 메뉴 학습 시키는 함수 추가
    return {"menu_prompt": menu_prompt}


def generate_menu_prompt(menu):
    menu_prompt = f'다음 메뉴를 등록해줘 메뉴명: {menu.name}, 메뉴 가격: {menu.price}, 메뉴 설명: {menu.description}, 메뉴 카테고리: {menu.categoryName}'
    return menu_prompt
