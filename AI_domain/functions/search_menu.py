import json
from AI_domain.models.ai_key_bot import chain_keybot

# -------중년층 Keywords 입력, 지정된 JSON 답변


# ingredients 키워드 질문 / gpt 답변
def search_menu(ingredients):
    menu_id_list = chain_keybot.predict(convert_to_searchform(ingredients))

    return convert_json(menu_id_list)


# 콤마로 구분, 대괄호로 묶인 문자열 반환
def convert_to_searchform(ingredients):
    ingredients_str = ', '.join(ingredients)
    return f'[${ingredients_str}]'


# JSON 포맷으로 변환 시도
def convert_json(result):
    try:
        json_data = json.loads(result)
        return json_data
    
    # JSON 답변이 아닐때
    except ValueError:
        return None