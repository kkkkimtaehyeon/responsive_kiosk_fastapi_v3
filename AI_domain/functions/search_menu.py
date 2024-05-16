import json
from AI_test.order.test_ai_order import chain


# 호출될 함수. str 사용자 질문을 매개변수로.
def search_menu(ingredients):
    menu_id_list = chain.predict(convert_to_searchform(ingredients))

    return convert_json(menu_id_list)


# order는 말그대로 주문시 사용하는 함수
# 키워드 검색할 때 검색된 메뉴를 반환하는 함수 따로 만들 필요

# json 포맷으로 변환(json 변환, 주문 종료 검증하는 기능이 한 함수에 들어가 있음 -> 분리 필요)
def convert_json(result):
    try:
        json_data = json.loads(result)
        return json_data
    except ValueError:
        # 키워드에 해당되는 메뉴가 없을 때 
        return None
    

def convert_to_searchform(ingredients):
    ingredients_str = ', '.join(ingredients)
    return f'[${ingredients_str}]'