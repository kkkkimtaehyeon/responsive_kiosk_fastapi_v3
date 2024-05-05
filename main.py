import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from domain.face_recognition import face_recognition_router
from domain.menu import menu_router
from domain.polly import polly_router
from domain.stt import stt_router

from domain.common.aws import Aws

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 허용할 출처 설정
    allow_credentials=True,
    allow_methods=["*"],  # 허용할 HTTP 메서드 설정
    allow_headers=["*"],  # 모든 헤더 허용
)

#app.include_router(face_recognition_router.router)
app.include_router(menu_router.router)
app.include_router(polly_router.router)
app.include_router(stt_router.router)

# @app.post("/generation")
# async def face_recognition_service(file: UploadFile = File(...)):

#     contents = await file.read()
#     image = Image.open(io.BytesIO(contents))
#     image_np = np.array(image)

#     age = get_age_from_image(image_np)
#     generation = determine_generation(age)
#     return JSONResponse(
#         headers={"Access-Control-Allow-Origin": "*"},
#         content={
#             "file name": file.filename,
#             "age": age,
#             "generation": generation
#         }
#     )
@app.post("/generation")
async def face_recognition_service(file: UploadFile = File(...)):

    return file.filename