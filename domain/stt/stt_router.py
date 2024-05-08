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