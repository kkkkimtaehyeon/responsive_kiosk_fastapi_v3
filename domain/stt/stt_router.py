#checked
from domain.common.user_script_dto import UserScript
from fastapi import APIRouter

router = APIRouter(
    prefix="/fast/api/stt",
    tags=["stt"]
)


#프론트에서 STT처리 후 Script

@router.post("/")
async def get_stt(user_script: UserScript):
    passed = user_script.userScript
    # gpt_text_response = GPT한테 말 거는 함수

    # gpt_voice_response_url = polly.polly_tts(user_script.userScript) gpt 응답 텍스트를 TTS 변환
    # return {
    #     "gpt_text_response": gpt_text_response,
    #     "gpt_voice_response_url" : gpt_voice_response_url,
    # }

    print(passed)
    return {"received_user_script": passed}
