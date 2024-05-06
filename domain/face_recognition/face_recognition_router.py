from fastapi import APIRouter
from fastapi import File, UploadFile
from domain.face_recognition.face_recognition_service import determine_generation, get_age_from_image, convert_jpg_to_np
from fastapi.responses import JSONResponse
from PIL import Image
import io
import numpy as np

router = APIRouter(
    prefix="/fast/api/face-recognition",
    tags=["face-recognition"]
)


@router.post("")
async def face_recognition_service(image_file: UploadFile = File(...)):
    contents = await image_file.read()
    image = Image.open(io.BytesIO(contents))
    image_np = np.array(image)

    age = get_age_from_image(image_np)
    generation = determine_generation(age)
    
    return {
        "file name": image_file.filename,
        "age": age,
        "generation": generation
    }
