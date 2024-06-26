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
from domain.menu.menu_service import backup_on_gpt, fetch_menus

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
#app.include_router(websocket_test.router )
app.include_router(face_recognition_router.router)


# #서비스 시작시 실행
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     menus = await fetch_menus()
#     await backup_on_gpt(menus)
#     yield

# app.router.lifespan_context=lifespan


