import sys
import os

# 프로젝트의 루트 디렉토리를 sys.path에 추가
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from fastapi import FastAPI, UploadFile, File

from data_models import UserScript, TestSearchKeywords, TestMenu2

from AI_domain.functions.add_menu import Menu
from AI_domain.functions.search_menu import search_menu
from AI_domain.functions.ai_order import order
from AI_domain.functions.face_recognition import recognize_face


app = FastAPI()

from PIL import Image
import io
import numpy as np


def convert_jpg_to_np(data):
    image = Image.open(io.BytesIO(data))
    return np.array(image)

def get_age_from_image(image_np):
    result = recognize_face(image_np)
    age = result[0]['age']
    return age


def determine_generation(age):
    if 0 <= age <= 40:
        return 'young'
    elif 40 < age <= 60:
        return 'middle'
    return 'old'


# 얼굴 인식
@app.post("/trecog")
async def face_recognition_service(image_file: UploadFile = File(...)):
    
    image_data = await image_file.read()
    image_np = convert_jpg_to_np(image_data)

    age = get_age_from_image(image_np)
    generation = determine_generation(age)
    
    return {
        "file name": image_file.filename,
        "age": age,
        "generation": generation
    }

# 각 gpt에 메뉴 저장
@app.post("/tadd-menu")
async def tadd_menu(menu:TestMenu2):

    menu_prompt = Menu.generate_register_prompt(menu)

    Menu.register_on_gpt(menu_prompt)

    return {"message" : "add success"}



# 중년층, AI search 후 응답
@app.post("/tsearch")
async def tsearch_menu(search_keywords:TestSearchKeywords):


    result = search_menu(search_keywords.ingredients)

    return result


# 노년층, 자연어 처리 후 응답
@app.post("/torder-ai")
async def torder_ai(userscr_question:UserScript):


    result = order(userscr_question.userScript)

    return result