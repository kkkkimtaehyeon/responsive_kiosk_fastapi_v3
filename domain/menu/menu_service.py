from AI_domain.functions.add_menu import Menu

# 호출될 함수. menu_prompt. 메뉴 추가 프롬프트를 buffermemory내에 저장
def add_menu(menu):
    menu_prompt = Menu.generate_register_prompt(menu)

    return Menu.register_on_gpt(menu_prompt)

def delete_menu(id):
    delete_prompt = Menu.generate_delete_prompt(id)

    return Menu.delete_on_gpt(delete_prompt)

    