from AI_test.order.test_ai_order import memory

class Menu:
    
    # gpt 학습을 위한 메뉴 프롬프트 생성
    def generate_register_prompt(menu):
        menu_prompt = f'(id: {menu.id}, name: {menu.name}, price: {menu.price}, description: {menu.description}, categoryName: {menu.categoryName})'
        return menu_prompt

    # gpt에 메뉴 학습
    def register_on_gpt(menu_prompt):
        return memory.chat_memory.add_ai_message(menu_prompt)