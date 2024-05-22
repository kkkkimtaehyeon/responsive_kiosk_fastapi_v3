# from AI_domain.functions.add_menu import Menu

from AI_domain.functions.memory_action import Add, Remove, Prompt

# 호출될 함수. menu_prompt. 메뉴 추가 프롬프트를 buffermemory내에 저장
def add_menu(menu):
    menu_prompt = Prompt.gen_register_prompt(menu)

    return Add.menu_info(menu_prompt)

def delete_menu(id):
    # delete_prompt = Prompt.gen_delete_prompt(id)

    return Remove.one_menu(id)

    