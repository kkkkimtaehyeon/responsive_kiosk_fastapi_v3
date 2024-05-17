from AI_domain.models import ai_cafe_bot, ai_key_bot

class Menu:
    
    # gpt에 전달할 메뉴 프롬프트 형식 지정
    def generate_register_prompt(menu):
        menu_prompt = f'(id: {menu.id}, name: {menu.name}, price: {menu.price}, description: {menu.description}, categoryName: {menu.categoryName})'
        return menu_prompt

    # 각 gpt에 메뉴 전달 반환값 없음
    def register_on_gpt(menu_prompt):
        ai_cafe_bot.memory.chat_memory.add_ai_message(menu_prompt)
        ai_key_bot.memory.chat_memory.add_ai_message(menu_prompt)