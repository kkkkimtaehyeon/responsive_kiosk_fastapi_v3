from fastapi import APIRouter
from fastapi import File, UploadFile


router = APIRouter(
    prefix="/fast/api/face-recognition",
    tags=["face-recognition"]
)


@router.post("/fast/api/face-recognition")
async def face_recognition(file: UploadFile = File(...)):
    # 이미지 파일 받아서 얼굴 인식하는 함수 추가
    return {"file_name": file.filename}