from AI_domain.models import ai_cafe_bot, ai_key_bot

class Prompt:
    # 메뉴 저장을 위한 프롬프트 생성 함수
    def generate_menu_prompt(menu):
        menu_prompt = f'(id: {menu.id}, name: {menu.name}, price: {menu.price}, description: {menu.description}, categoryName: {menu.categoryName})'
        return menu_prompt


class Add:

    # 각 gpt에 메뉴 전달 반환값 없음
    def menu_information(menu_prompt):
        ai_cafe_bot.memory.chat_memory.add_ai_message(menu_prompt)
        ai_key_bot.memory.chat_memory.add_ai_message(menu_prompt)


class Remove:

    # 등록된 메뉴 제외한 모든 메시지 삭제
    def cafebot_all_massage():
        history = ai_cafe_bot.memory.chat_memory.messages
        menu_msg = [msg for msg in history if msg.type == "ai" and "(id" in msg.content.lower()]

        ai_cafe_bot.memory.chat_memory.messages = menu_msg

    def keybot_all_massage():
        history = ai_key_bot.memory.chat_memory.messages
        menu_msg = [msg for msg in history if msg.type == "ai" and "(id" in msg.content.lower()]

        ai_key_bot.memory.chat_memory.messages = menu_msg


    # 등록된 지정 메뉴 삭제
    def one_menu(id):
        cafebot_history = ai_cafe_bot.memory.chat_memory.messages
        keybot_history = ai_key_bot.memory.chat_memory.messages

        cb_rm_menu_history = [msg for msg in cafebot_history if not (msg.type == "ai" and f"(id: {id}" in msg.content.lower())]
        kb_rm_menu_history = [msg for msg in keybot_history if not (msg.type == "ai" and f"(id: {id}" in msg.content.lower())]

        ai_cafe_bot.memory.chat_memory.messages = cb_rm_menu_history
        ai_key_bot.memory.chat_memory.messages = kb_rm_menu_history
