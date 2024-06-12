from fastapi import WebSocket, WebSocketDisconnect, APIRouter
from AI_domain.functions.ai_order import order
from domain.common.aws import Aws
from botocore.exceptions import BotoCoreError, ClientError
from AI_domain.functions.ai_order import order
from openai import OpenAI
from AI_domain.functions.ai_order import order 
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
# @router.websocket("/v2/polly")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text() # 웹소켓으로 텍스트 수신
        
#         gpt_response = await order(data) # GPT에게 텍스트 기반 답변 요청
        

#         if(is_json(gpt_response)): # 주문이 종료 시 GPT json으로 응답
#             await websocket.send_json(gpt_response)
#         else: 
#             await websocket.send_text(gpt_response) # 클라이언트에 답변 전송
#             try:
#                 response = Aws.polly.synthesize_speech( # AWS Polly 사용
#                     LanguageCode='ko-KR',
#                     Text=gpt_response,
#                     OutputFormat='mp3',
#                     VoiceId='Seoyeon'
#                 )
#             except (BotoCoreError, ClientError) as error:
#                 await websocket.send_text(f"Error: {error}")
#                 continue

#             buffer = io.BytesIO()
#             if "AudioStream" in response:
#                 for chunk in response['AudioStream'].iter_chunks(chunk_size=8192):
#                     buffer.write(chunk)
#                 buffer.seek(0)
#                 await websocket.send_bytes(buffer.read())
#                 print(f"buffer({len(buffer.read()) } 전송 완료!)")
#                 buffer.seek(0)
#                 buffer.truncate(0)
#             else:
#                 await websocket.send_text("오디오를 스트리밍 할 수 없습니다.")
@router.websocket("/v2/polly")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text() # 웹소켓으로 텍스트 수신

            gpt_response = await order(data) # GPT에게 답변 요청

            if is_json(gpt_response): # 주문이 종료 시 GPT json으로 응답
                await websocket.send_json(gpt_response)
            else:
                await websocket.send_text(gpt_response) # 클라이언트에 답변 전송
                await send_audio_response(websocket, gpt_response)
    except WebSocketDisconnect:
        print("웹소켓 접속 끊김.")
    except Exception as e:
        print(f"에러: {e}")
        await websocket.send_text(f"에러: {str(e)}")
    finally:
        await websocket.close()

async def send_audio_response(websocket: WebSocket, text:str):
    try:
        response = Aws.polly.synthesize_speech( # AWS Polly 사용
                    LanguageCode='ko-KR',
                    Text=text,
                    OutputFormat='mp3',
                    VoiceId='Seoyeon'
                )
    except (BotoCoreError, ClientError) as error:
                await websocket.send_text(f"Error: {error}")
                return
    
    if "AudioStream" in response:
        buffer = io.BytesIO()
        try:
            response
            for chunk in response['AudioStream'].iter_chunks(chunk_size=8192):
                buffer.write(chunk)
            buffer.seek(0)
            await websocket.send_bytes(buffer.read())
        finally:
            buffer.close()
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


from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())

key = os.getenv("OPENAI_API_KEY_EUNHAK")
client = OpenAI(api_key=key)


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
    
