from domain.common.gpt_setting import memory

def generate_menu_prompt(menu):
    menu_prompt = f'다음 메뉴를 등록해줘 메뉴명: {menu.name}, 메뉴 가격: {menu.price}, 메뉴 설명: {menu.description}, 메뉴 카테고리: {menu.categoryName}'
    return menu_prompt

# 호출될 함수. menu_prompt. 메뉴 추가 프롬프트를 buffermemory내에 저장
def add_history(menu_prompt):
    memory.chat_memory.add_ai_message(menu_prompt)