from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from domain.face_recognition import face_recognition_router
from domain.menu import menu_router
from domain.polly import polly_router
from domain.stt import stt_router

app = FastAPI()

app.include_router(face_recognition_router.router)
app.include_router(menu_router.router)
app.include_router(polly_router.router)
app.include_router(stt_router.router)


# CORS 허용설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # 클라이언트 도메인
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
