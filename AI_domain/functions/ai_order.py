import json
from AI_domain.models.ai_cafe_bot import chain_cafebot

# -------노년층 대화 입력, 지정된 JSON 답변


# str 사용자 질문 / gpt 답변
async def order(str):
    result = chain_cafebot.predict(question = str)

    return convert_json(result)


# json 포맷으로 변환
def convert_json(result):
    try:
        json_data = json.loads(result)
        return json_data
    except ValueError:
        return {
            "gpt_text_response": result,
            "gpt_audio_response": None
        }
