# checked
from fastapi import APIRouter
from domain.menu.menu_dto import Menu
from domain.order.ai_order import add_history
from domain.menu.menu_service import generate_menu_prompt

router = APIRouter(
    prefix="/fast/api/menu-register",
    tags=["stt"]
)


# 메뉴 추가
@router.post("")
async def add_menu(menu:Menu):
    # 원래 메뉴객체 불러들여올것
    # 관리자 페이지에서 메뉴 등록느낌의, 메뉴 객체 생성
    # menu = Menu("americano", 5500, "쓰지 않은 커피입니다.", "커피")

    # 등록된 메뉴 가져와서 프롬프트로 입력
    menu_prompt = generate_menu_prompt(menu)
    # 메뉴 프롬프트 order의 매개변수로.
    # openai api사용한 langchain의 buffermemory내에 입력시킴.
    add_history(menu_prompt)

    return {"message" : f"{menu} has been successfuly added!!"}



