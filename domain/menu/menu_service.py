# from AI_domain.functions.add_menu import Menu
import httpx
import json
from pydantic import BaseModel

from AI_domain.functions.memory_action import Add, Remove, Prompt

class Menu(BaseModel):
    id: float
    name: str
    price: float
    description: str
    categoryName: str

# 호출될 함수. menu_prompt. 메뉴 추가 프롬프트를 buffermemory내에 저장
def add_menu(menu):
    menu_prompt = Prompt.generate_menu_prompt(menu)

    return Add.menu_information(menu_prompt)

def delete_menu(id):
    # delete_prompt = Prompt.gen_delete_prompt(id)
    return Remove.one_menu(id)

async def fetch_menus():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get('http://localhost:8080/api/menus')
            print(response.status_code)
            json_data = response.content.decode('utf-8')
            data = json.loads(json_data)
            menus = [Menu(**item) for item in data]
        return menus
    except:
        return None

async def backup_on_gpt(menus):
    try:
        for menu in menus:
            try:
                add_menu(menu)
                print(f'{menu.name}가 백업되었습니다.')
            except Exception as e:
                e.with_traceback()
                print('백업이 실패했습니다.')
    except:
        return None