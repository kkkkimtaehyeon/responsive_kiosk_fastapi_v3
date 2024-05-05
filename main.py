import uvicorn
from fastapi import FastAPI, File, UploadFile
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

origins = {
    "http://localhost:8000",
    "http://localhost:3000"

}
# CORS 허용설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins],  # 모든 출처를 허용하도록 설정 (실제 제품 환경에서는 필요에 따라 수정)
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    filename = file.filename
    return {"filename": filename}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001,reload=True)