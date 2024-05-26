import uvicorn
import httpx
import json
from contextlib import asynccontextmanager
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from domain.face_recognition import face_recognition_router
from domain.menu import menu_router
from domain.polly import polly_router
from domain.stt import stt_router
from domain.search import search_router
from domain.ai_order import order_router
from domain.test import websocket_test


app = FastAPI()

origins = [
    "http://localhost:8080",  # 서버 도메인
    "http://localhost:3000",  # 클라이언트 도메인
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

#app.include_router(face_recognition_router.router)
app.include_router(menu_router.router)
app.include_router(polly_router.router)
app.include_router(stt_router.router)
app.include_router(search_router.router)
app.include_router(order_router.router) 
app.include_router(websocket_test.router )


# 서비 시작시 실행
@asynccontextmanager
async def lifespan(app: FastAPI):
    await fetch_menus()
    print("backup success")
    yield

app.router.lifespan_context=lifespan



#asyncio.run(fetch_menus())
# 모든 메뉴 정보를 반환
async def fetch_menus():
    async with httpx.AsyncClient() as client:
        response = await client.get('http://localhost:8080/api/menus')
        print(response.status_code)

        json_data = response.content.decode('utf-8')
        data = json.loads(json_data)