from fastapi import APIRouter
from fastapi import File, UploadFile
from domain.face_recognition.face_recognition_service import determine_generation, get_age_from_image
from PIL import Image
import io
import numpy as np

router = APIRouter(
    prefix="/fast/api/face-recognition",
    tags=["face-recognition"]
)


# @router.post("/")
# async def face_recognition_service(file: UploadFile = File(...)):
#
#     image_np_data = convert_file_to_np(file)
#     age = get_age_from_image(image_np_data)
#     generation = determine_generation(age)
#
#     return {"generation": generation}

@router.post("")
async def analyze_image(file: UploadFile):
    # post요청으로 file(이미지 파일) 받아옴
    # file을 byte형태로 읽어서 contents에 저장.
    contents = await file.read()

    # byte형태의 contents를 읽어 이미지파일 형태로 image에 저장
    image = Image.open(io.BytesIO(contents))

    # Pillow image를 numpy array로 변환
    image_np = np.array(image)

    age = get_age_from_image(image_np)
    generation = determine_generation(age)
    return generation
