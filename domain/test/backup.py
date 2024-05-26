import httpx
import asyncio
import json
from pydantic import BaseModel
from domain.menu.menu_service import add_menu

class Menu(BaseModel):
    id: float
    name: str
    price: float
    description: str
    categoryName: str

class BackUp():
    async def fetch_menus():
        async with httpx.AsyncClient() as client:
            response = await client.get('http://localhost:8080/api/menus')
            print(response.status_code)

            json_data = response.content.decode('utf-8')
            data = json.loads(json_data)
            menus = [Menu(**item) for item in data]
        return menus

    async def backup_on_gpt(menus):
        for menu in menus:
            try:
                add_menu(menu)
                print(f'{menu.name}가 백업되었습니다.')
            except Exception as e:
                e.with_traceback()
                print('백업이 실패했습니다.')



#asyncio.run(backup_on_gpt())