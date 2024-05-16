from fastapi import APIRouter
from domain.common import user_script_dto as UserScript
from domain.ai_order import order_service 

router = APIRouter(
    prefix="/fast/api/ai-order",
    tags=["ai-order"]
)

@router.post("")
async def ai_order(userScript: UserScript):
    return order_service.order_with_ai(userScript)
