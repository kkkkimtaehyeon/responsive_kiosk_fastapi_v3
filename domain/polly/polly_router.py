#checked
from domain.common.user_script_dto import UserScript
from domain.polly.polly_service import get_tts_url
from fastapi import APIRouter

router = APIRouter(
    prefix="/fast/api/polly",
    tags=["polly"]
)

#프론트에서 userScript 입력받고 s3에 저장, 저장된 객체 url 반환
@router.post("/")
async def get_tts(user_script: UserScript):
    return {"tts_url" : get_tts_url(user_script.userScript)}