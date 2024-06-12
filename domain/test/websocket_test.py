# from fastapi import WebSocket, APIRouter
# from AI_domain.functions.ai_order import order
# from domain.common.aws import Aws
# from botocore.exceptions import BotoCoreError, ClientError
# from contextlib import closing
# # gpt를 사용한 주문 기능을 위해 import
# from AI_domain.functions.ai_order import order
# import json

# router = APIRouter(
#     prefix="/websocket"
# )

# @router.websocket("/ws")
# async def websocket_endpoint(websocket:WebSocket):
#     print("Accecpting Connection")
#     await websocket.accept()
#     print("Accepted")
#     while True:
#         try:
#             recieved_data = await websocket.receive_text()
#             print(recieved_data)
#             #await websocket.send_text(recieved_data)

#             gpt_response = await order(recieved_data)
#             await websocket.send_json(gpt_response)
#         except:
#             print("error!")
#             break


# @router.websocket("/v2/ws")
# async def websocket_endpoint_v2(websocket: WebSocket):
#     await websocket.accept()
#     print("웹 소켓 정상 연결")

#     try:
#         while True:
#             data = await websocket.receive_text()
#             print(f"received text: {data}")
#             try:
#                 response = Aws.polly.synthesize_speech(
#                     LanguageCode='ko-KR',
#                     Text=data,
#                     OutputFormat='mp3',
#                     VoiceId='Seoyeon'
#                 )
#             except (BotoCoreError, ClientError) as error:
#                 await websocket.send_text(f"Error: {error}")
#                 await websocket.close()
#                 return
            
#             if "AudioStream" in response:
#                 with closing(response["AudioStream"]) as stream:
#                     try:
#                         while True:
#                             chunk = stream.read(4096)
#                             if not chunk:
#                                 break
#                             await websocket.send_bytes(chunk)
#                             print(f"Sending chunk of size {len(chunk)}")
#                     except IOError as error:
#                         await websocket.send_text(f"Error: {error}")
#             else:
#                 await websocket.send_text("오디오를 스트리밍 할 수 없습니다.")
#             print("모든 chunk가 전송되었습니다.")
#     except Exception as e:
#         print(f"Connection error: {e}")
#     finally:
#         await websocket.close()

# # polly
# @router.websocket("/v3/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         print(f"received data : {data}")
        
#         gpt_response = await order(data) # gpt에게 주문하고 답변 수신
#         print(f"gpt is responding! : {gpt_response}")
        

#         if(is_json(gpt_response)): #gpt_response가 json이면 -> 주문이 종료되면 json 전송
#             await websocket.send_json(gpt_response)
#         else: #gpt_response가 json이 아니면 -> 답변을 받은 것이면 오디오 chunk 전송
#             await websocket.send_text(gpt_response)
#             try:
#                 response = Aws.polly.synthesize_speech(
#                     LanguageCode='ko-KR',
#                     Text=gpt_response,
#                     OutputFormat='mp3',
#                     VoiceId='Seoyeon'
#                 )
#             except (BotoCoreError, ClientError) as error:
#                 await websocket.send_text(f"Error: {error}")
#                 continue

#             if "AudioStream" in response:
#                 for chunk in response['AudioStream'].iter_chunks(chunk_size=8192):
#                     await websocket.send_bytes(chunk)
#                     print(f"chunk({len(chunk)}) 전송!")
#             else:
#                 await websocket.send_text("오디오를 스트리밍 할 수 없습니다.")

# # openAi tts

# client = OpenAI()

# @router.websocket("/v4/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         print(f"received data : {data}")
        
#         gpt_response = await order(data) # gpt에게 주문하고 답변 수신
#         print(f"gpt is responding! : {gpt_response}")
        

#         if(is_json(gpt_response)): #gpt_response가 json이면 -> 주문이 종료되면 json 전송
#             await websocket.send_json(gpt_response)
#         else: #gpt_response가 json이 아니면 -> 답변을 받은 것이면 오디오 chunk 전송
#             await websocket.send_text(gpt_response)
#             try:
#                 response = client.audio.speech.create(
#                 model="tts-1",
#                 voice="shimmer",
#                 input=gpt_response,
#                 response_format="mp3"
#             )
#             except (ClientError) as error:
#                 await websocket.send_text(f"Error: {error}")
#                 continue

#             buffer = io.BytesIO()
#             for chunk in response.iter_bytes(chunk_size=8192):
#                 buffer.write(chunk)
#             buffer.seek(0)
#             await websocket.send_bytes(buffer.read())
#             print(f"buffer({len(buffer.read()) } 전송 완료!)")
#             buffer.seek(0)
#             buffer.truncate(0)

# import io
# @router.websocket("/v5/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         print(f"received data : {data}")
        
#         gpt_response = await order(data) # gpt에게 주문하고 답변 수신
#         print(f"gpt is responding! : {gpt_response}")

#         if(is_json(gpt_response)): #gpt_response가 json이면 -> 주문이 종료되면 json 전송
#             await websocket.send_json(gpt_response)
#         else: #gpt_response가 json이 아니면 -> 답변을 받은 것이면 오디오 chunk 전송
#             await websocket.send_text(gpt_response)
#             with client.audio.speech.with_streaming_response.create(
#                 model="tts-1",
#                 voice="shimmer",
#                 input=gpt_response,
#                 response_format='mp3'
#             ) as response:
#                 for chunk in response.iter_bytes(chunk_size=32768):
#                     await websocket.send_bytes(chunk)
        

# def is_json(data):
#     try:
#         json.loads(data)
#         return True
#     except ValueError as e:
#         return False
    