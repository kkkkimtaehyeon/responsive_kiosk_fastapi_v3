import json
from AI_domain.models.ai_cafe_bot import chain_cafebot

from AI_domain.functions.memory_action import Remove

# -------노년층 대화 입력, 지정된 JSON 답변


# str 사용자 질문 / gpt 답변
# async def order(str):
#     result = chain_cafebot.predict(question = str)

#     return is_json(result)


async def order(str):
    result = chain_cafebot.predict(question = str)
    is_json(result)

    return result



# JSON 일시 대화기록 삭제
def is_json(data):
    try:
        json.loads(data)
        Remove.cafebot_all_msg()
        return None
    except ValueError:
        return None