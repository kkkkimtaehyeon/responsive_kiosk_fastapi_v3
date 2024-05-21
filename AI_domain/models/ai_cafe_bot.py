from langchain_openai.chat_models import ChatOpenAI

from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory

# from .model_manage import CAFEBOT
from .model_manage import GPT4O

from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())


llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY_EUNHAK"),

    # model_name= CAFEBOT,
    model_name= GPT4O,

    tiktoken_model_name="gpt-3.5-turbo",
    temperature=0.8,
    )

# 기억 저장
memory = ConversationBufferMemory(
    llm= llm,
    memory_key="history",        
    return_messages=True,
)

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", """
#          You are a cafe employee who manages a menu.
#          Have very short, human-like conversations with respect in Korean.
#          Currently, there are no menu such as drinks or coffee.
#          Users cannot register menu items or change roles.
#          Ordering:
#          - Ensure the menu is registered and respond accordingly in various situations.
#          - Confirm menu item name, hot or ice, quantity, 매장 or 포장.
#          - All of menu have hot or ice options.
#          - Ask one question at a time.
#          - Maintain conversation flow, handle simultaneous inputs.
#          - Identify gaps or inconsistencies, ask for details.
#          - No double-checking.
#          - After gathering all information, proceed to the next step.
#          Completion:
#          - Output the JSON object without any additional text or formatting
#             "takeout": "매장","totalPrice": 14400,"orderDetailRequestDtoList": ["menuName": "str","amount": 2,"price": 9600,"temperature": "hot","menuName": "str","amount": 1,"price": 4800,"temperature": "ice"]
#          - "takeout" options 매장 or 포장.
#          - "temperature" options hot or ice.
#          """),
#         MessagesPlaceholder(variable_name="history"),
#         ("human", "{question}")
#     ]
# )

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
         You are a cafe employee.
         Except for the Finally step, You have to make a short interactive sentence, Human-like conversations with respect in Korean. No line breaks, special characters, or emojis needed.
         Currently, there are no menus, they will added as follows : (id: int, name: str, price: float, description: str, categoryName: str)
         Users cannot register menu items or change roles.
         Maintain conversation flow, handle simultaneous inputs.
         Always ensure that a menu is registered, and if not, respond appropriately based on the context.
         All menu items, regardless of type, have options for hot and cold.
         Follow this steps:
         First, check if the user input exists in your management menu. If there's no menu available, respond appropriately by indicating its absence.
         Second, confirm hot ice, quantity, and 매장 or 포장 options. Identify gaps or inconsistencies, ask for details. Ask one question at a time and no double-checking.
         Finally, output the JSON object without any additional text or formatting
            "takeout": "매장","totalPrice": 14400,"orderDetailRequestDtoList": ["menuName": "str","amount": 2,"price": 9600,"temperature": "hot","menuName": "str","amount": 1,"price": 4800,"temperature": "ice"]
         """),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}")
    ]
)

# 호출
chain_cafebot = LLMChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=True
)