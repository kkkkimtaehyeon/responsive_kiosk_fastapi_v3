from fastapi import APIRouter, Query
from ..common.user_script_dto import UserScript
from domain.ai_order import order_service
from AI_domain.functions.ai_order import order
from domain.tts.openai_tts import text_to_speech
from fastapi.responses import StreamingResponse
from fastapi import HTTPException
import os

router = APIRouter(
    prefix="/fast/api/ai-order",
    tags=["ai-order"]
)

# @router.post("")
# async def ai_order(userScript: UserScript):
#     return order_service.order_with_ai(userScript.userScript)


@router.post("")
async def ai_order(userScript: UserScript):
    result = {}
    result['gpt_text_response'] = await order(userScript.userScript)
    result['gpt_audio_response'] = f"http://127.0.0.1:8000/fast/api/ai-order/audio?prompt={result['gpt_text_response']}"
    return result

@router.get("/audio")
async def get_audio(prompt: str = Query(...)):
    return await text_to_speech(prompt)