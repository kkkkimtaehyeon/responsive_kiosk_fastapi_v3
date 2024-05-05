#checked
from domain.common.user_script_dto import UserScript
from domain.order.ai_order import order
from domain.polly.polly_service import get_tts_url
from fastapi import APIRouter

router = APIRouter(
    prefix="/fast/api/script-order",
    tags=["stt"]
)


#프론트에서 STT처리 후 Script

@router.post("/")
async def get_stt(user_script: UserScript):
    gpt_script = order(user_script.userScript)
    gpt_audio_url = get_tts_url(gpt_script)

    return {
        "gptScript": gpt_script,
        "gptAudioUrl": gpt_audio_url
    }
    # gpt_text_response = GPT한테 말 거는 함수

    # gpt_voice_response_url = polly.polly_tts(user_script.userScript) gpt 응답 텍스트를 TTS 변환
    # return {
    #     "gpt_text_response": gpt_text_response,
    #     "gpt_voice_response_url" : gpt_voice_response_url,
    # }

    # print(passed)
    # return {"received_user_script": passed}
