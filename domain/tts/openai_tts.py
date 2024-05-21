from openai import OpenAI
from fastapi.responses import StreamingResponse
from fastapi import Response
from io import BytesIO

client = OpenAI(api_key="")

async def text_to_speech(prompt):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=prompt,
    )
    
    audio_data = response.iter_bytes

    # 스트리밍 응답 생성
    return StreamingResponse(iter([audio_data]), media_type="audio/wav")
    
    