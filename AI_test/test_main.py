import sys
import os

# 프로젝트의 루트 디렉토리를 sys.path에 추가
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from fastapi import FastAPI

from data_models import UserScript, TestSearchKeywords, TestMenu2

from AI_domain.functions.add_menu import Menu
from AI_domain.functions.search_menu import search_menu
from AI_domain.functions.ai_order import order

app = FastAPI()


# 각 gpt에 메뉴 저장
@app.post("/tadd-menu")
async def tadd_menu(menu:TestMenu2):

    menu_prompt = Menu.generate_register_prompt(menu)

    Menu.register_on_gpt(menu_prompt)

    return {"message" : "add success"}



# 중년층, AI search 후 응답
@app.post("/tsearch")
async def tsearch_menu(search_keywords:TestSearchKeywords):



    result = search_menu(search_keywords.ingredients)

    return result


# 노년층, 자연어 처리 후 응답
@app.post("/torder-ai")
async def torder_ai(userscr_question:UserScript):

    # user_question = userscr_question.userScript

    # ai에 전달
    result = order(userscr_question.userScript)

    return result