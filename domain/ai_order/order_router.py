from fastapi import APIRouter
from ..common.user_script_dto import UserScript
from domain.ai_order import order_service

router = APIRouter(
    prefix="/fast/api/ai-order",
    tags=["ai-order"]
)

@router.post("")
async def ai_order(userScript: UserScript):
    return order_service.order_with_ai(userScript.userScript)
