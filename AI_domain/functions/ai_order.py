import json
from AI_domain.models.ai_cafe_bot import chain_cafebot

# -------노년층 대화 입력, 지정된 JSON 답변


# str 사용자 질문 / gpt 답변
def order(str):
    result = chain_cafebot.predict(order = str)

    return convert_json(result)


# json 포맷으로 변환
def convert_json(result):
    try:
        json_data = json.loads(result)
        return json_data
    
    # 일반 답변일 때
    except ValueError:
        ai_result = {"ai_result": result}
        return ai_result