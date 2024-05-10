import json
from domain.common.gpt_setting import chain


# json 포맷으로 변환
def convert_json(result):
    try:
        json_data = json.loads(result)
        return json_data
    except ValueError:
        ai_result = {"ai_result": result}
        return ai_result


# 호출될 함수. str 사용자 질문을 매개변수로.
def order(str):
    result = chain.predict(order = str)

    return convert_json(result)
    

