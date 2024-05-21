from fastapi import WebSocket, APIRouter
from AI_domain.functions.ai_order import order
from domain.common.aws import Aws
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
from tempfile import gettempdir

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


@router.websocket("/v2/ws")
async def websocket_endpoint_v2(websocket: WebSocket):
    await websocket.accept()
    print("웹 소켓 정상 연결")

    try:
        while True:
            data = await websocket.receive_text()
            print(f"received text: {data}")
            try:
                response = Aws.polly.synthesize_speech(
                    LanguageCode='ko-KR',
                    Text=data,
                    OutputFormat='mp3',
                    VoiceId='Seoyeon'
                )
            except (BotoCoreError, ClientError) as error:
                await websocket.send_text(f"Error: {error}")
                await websocket.close()
                return
            
            if "AudioStream" in response:
                with closing(response["AudioStream"]) as stream:
                    try:
                        while True:
                            chunk = stream.read(4096)
                            if not chunk:
                                break
                            await websocket.send_bytes(chunk)
                            print(f"Sending chunk of size {len(chunk)}")
                    except IOError as error:
                        await websocket.send_text(f"Error: {error}")
            else:
                await websocket.send_text("오디오를 스트리밍 할 수 없습니다.")
            print("모든 chunk가 전송되었습니다.")
    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        await websocket.close()


@router.websocket("/v3/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(f"received data : {data}")
        try:
            response = Aws.polly.synthesize_speech(
                LanguageCode='ko-KR',
                Text=data,
                OutputFormat='mp3',
                VoiceId='Seoyeon'
            )
        except (BotoCoreError, ClientError) as error:
            await websocket.send_text(f"Error: {error}")
            continue

        if "AudioStream" in response:
            for chunk in response['AudioStream'].iter_chunks(chunk_size=8192):
                await websocket.send_bytes(chunk)
                print("chunk 전송")
        else:
            await websocket.send_text("오디오를 스트리밍 할 수 없습니다.")