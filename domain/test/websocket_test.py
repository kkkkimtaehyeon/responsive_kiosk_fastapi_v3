from fastapi import FastAPI, WebSocket, APIRouter
from AI_domain.functions.ai_order import order

app = FastAPI()

router = APIRouter(
    prefix="/websocket"
)

@router.websocket("/ws")
async def websocket_endpoint(websocket:WebSocket):
    print("Accecpting Connection")
    await websocket.accept()
    print("Accepted")
    while True:
        try:
            recieved_data = await websocket.receive_text()
            print(recieved_data)
            #await websocket.send_text(recieved_data)

            gpt_response = await order(recieved_data)
            await websocket.send_json(gpt_response)
        except:
            print("error!")
            break
