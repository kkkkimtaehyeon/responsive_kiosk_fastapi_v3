#checked
from domain.common.user_script_dto import UserScript
from domain.tts.openai_tts import text_to_speech
from fastapi import APIRouter
import os
from fastapi.responses import StreamingResponse

router = APIRouter(
    prefix="/fast/api/openai-tts",
    tags=["openai-tts"]
)

#프론트에서 userScript 입력받고 s3에 저장, 저장된 객체 url 반환
# @router.post("/")
# async def get_tts(user_script: UserScript):
#     return text_to_speech(user_script.userScript)

@router.post("/")
async def generate_audio(user_script: UserScript):
    prompt = user_script.userScript
    
    # 텍스트를 음성으로 변환하는 함수 호출
    file_path = text_to_speech(prompt)
    
    # 변환된 파일을 스트리밍 응답으로 반환
    if os.path.exists(file_path):
        file_like = open(file_path, mode="rb")

        return {
            "gpt_text_resoponse": prompt,
            "gpt_audio_resposne": StreamingResponse(file_like, media_type="audio/wav")
        }