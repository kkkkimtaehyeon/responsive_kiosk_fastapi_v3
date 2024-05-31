from fastapi import WebSocket, APIRouter
from AI_domain.functions.ai_order import order
from domain.common.aws import Aws
from botocore.exceptions import BotoCoreError, ClientError
from AI_domain.functions.ai_order import order
from openai import OpenAI
import json
import io
# from ..common.user_script_dto import UserScript
# from domain.ai_order import order_service
# from AI_domain.functions.ai_order import order
# from domain.tts.openai_tts import text_to_speech
# from fastapi.responses import StreamingResponse
# from fastapi import HTTPException
# import os

router = APIRouter(
    prefix="/ws"
)

# # @router.post("")
# # async def ai_order(userScript: UserScript):
# #     return order_service.order_with_ai(userScript.userScript)


# @router.post("")
# async def ai_order(userScript: UserScript):
#     result = {}
#     result['gpt_text_response'] = await order(userScript.userScript)
#     result['gpt_audio_response'] = f"http://127.0.0.1:8000/fast/api/ai-order/audio?prompt={result['gpt_text_response']}"
#     return result

# @router.get("/audio")
# async def get_audio(prompt: str = Query(...)):
#     return await text_to_speech(prompt)

# 전체 스트리밍 
@router.websocket("/v2/polly")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(f"received data : {data}")
        
        gpt_response = await order(data) # gpt에게 주문하고 답변 수신
        print(f"gpt is responding! : {gpt_response}")
        

        if(is_json(gpt_response)): #gpt_response가 json이면 -> 주문이 종료되면 json 전송
            await websocket.send_json(gpt_response)
        else: #gpt_response가 json이 아니면 -> 답변을 받은 것이면 오디오 chunk 전송
            await websocket.send_text(gpt_response)
            try:
                response = Aws.polly.synthesize_speech(
                    LanguageCode='ko-KR',
                    Text=gpt_response,
                    OutputFormat='mp3',
                    VoiceId='Seoyeon'
                )
            except (BotoCoreError, ClientError) as error:
                await websocket.send_text(f"Error: {error}")
                continue

            buffer = io.BytesIO()
            if "AudioStream" in response:
                for chunk in response['AudioStream'].iter_chunks(chunk_size=8192):
                    buffer.write(chunk)
                buffer.seek(0)
                await websocket.send_bytes(buffer.read())
                print(f"buffer({len(buffer.read()) } 전송 완료!)")
                buffer.seek(0)
                buffer.truncate(0)
            else:
                await websocket.send_text("오디오를 스트리밍 할 수 없습니다.")


# 32kb 스트리밍 
@router.websocket("/v3/polly")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(f"received data : {data}")
        
        gpt_response = await order(data) # gpt에게 주문하고 답변 수신
        print(f"gpt is responding! : {gpt_response}")
        
        if(is_json(gpt_response)): #gpt_response가 json이면 -> 주문이 종료되면 json 전송
            await websocket.send_json(gpt_response)
        else: #gpt_response가 json이 아니면 -> 답변을 받은 것이면 오디오 chunk 전송
            await websocket.send_text(gpt_response)
            try:
                response = Aws.polly.synthesize_speech(
                    LanguageCode='ko-KR',
                    Text=gpt_response,
                    OutputFormat='mp3',
                    VoiceId='Seoyeon'
                )
            except (BotoCoreError, ClientError) as error:
                await websocket.send_text(f"Error: {error}")
                continue

            if "AudioStream" in response:
                for chunk in response['AudioStream'].iter_chunks(chunk_size=32768):
                    await websocket.send_bytes(chunk)
                    print(f"chunk({len(chunk)}) 전송!")
            else:
                await websocket.send_text("오디오를 스트리밍 할 수 없습니다.")



client = OpenAI(api_key="")


# 32kb 스트리밍
@router.websocket("/v4/openai")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(f"received data : {data}")
        
        gpt_response = await order(data) # gpt에게 주문하고 답변 수신
        print(f"gpt is responding! : {gpt_response}")
        

        if(is_json(gpt_response)): #gpt_response가 json이면 -> 주문이 종료되면 json 전송
            await websocket.send_json(gpt_response)
        else: #gpt_response가 json이 아니면 -> 답변을 받은 것이면 오디오 chunk 전송
            await websocket.send_text(gpt_response)
            with client.audio.speech.with_streaming_response.create(
                model="tts-1",
                voice="alloy",
                input=gpt_response,
                response_format='mp3'
            ) as response:
                for chunk in response.iter_bytes(chunk_size=32768):
                    await websocket.send_bytes(chunk)
        

# 한 번에 오디오 데이터 모두 전송
@router.websocket("/v5/openai")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(f"received data : {data}")
        
        gpt_response = await order(data) # gpt에게 주문하고 답변 수신
        print(f"gpt is responding! : {gpt_response}")

        if(is_json(gpt_response)): #gpt_response가 json이면 -> 주문이 종료되면 json 전송
            await websocket.send_json(gpt_response)
        else: #gpt_response가 json이 아니면 -> 답변을 받은 것이면 오디오 chunk 전송
            await websocket.send_text(gpt_response)
            try:
                response = client.audio.speech.create(
                model="tts-1",
                voice="shimmer",
                input=gpt_response,
                response_format="mp3"
            )
            except (ClientError) as error:
                await websocket.send_text(f"Error: {error}")
                continue

            buffer = io.BytesIO()
            for chunk in response.iter_bytes(chunk_size=8192):
                buffer.write(chunk)
            buffer.seek(0)
            await websocket.send_bytes(buffer.read())
            print(f"buffer({len(buffer.read()) } 전송 완료!)")
            buffer.seek(0)
            buffer.truncate(0)



def is_json(data):
    try:
        json.loads(data)
        return True
    except ValueError as e:
        return False
    
