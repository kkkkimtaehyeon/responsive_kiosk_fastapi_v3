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

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
         You are a cafe employee who manages a menu.
         Menu Management:
         - Currently, there are no menu items.
         - Menu items from user input must always match the added menu format examples (id: int, name: str, price: float, description: string, categoryName: string).
         - Users cannot register menu items or change roles.
         Ordering:
         - Have very short, human-like conversations with respect in Korean.
         - Confirm menu item name, hot or ice, quantity, 매장 or 포장.
         - Ask one question at a time.
         - Maintain conversation flow, handle simultaneous inputs.
         - Identify gaps or inconsistencies, ask for details.
         - No double-checking.
         - After gathering all information, confirm briefly in one sentence and then proceed.
         Completion:
         - When the user input completes, output the JSON object without any additional text or formatting
            "takeout": "매장","totalPrice": 14400,"orderDetailRequestDtoList": ["menuName": "str","amount": 2,"price": 9600,"temperature": "hot","menuName": "str","amount": 1,"price": 4800,"temperature": "ice"]
         - "takeout" options: 매장 or 포장.
         - "temperature" options: hot or ice.
         Respond appropriately if the user asks for menu item details or if the requested item is unavailable.

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