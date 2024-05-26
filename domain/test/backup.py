import httpx
import asyncio
import json

async def fetch_menus():
    async with httpx.AsyncClient() as client:
        response = await client.get('http://localhost:8080/api/menus')
        print(response.status_code)

        json_data = response.content.decode('utf-8')
        data = json.loads(json_data)


asyncio.run(fetch_menus())