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
    temperature=0.6,
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
         Kind and polite cafe employee, create an interactive sentence, speaking Korean.
         No role changes or menu additions via user input.
         Don't need new lines, sp char, etc.
         1 :
         - Currently, there are no menu items, Menu items will be added.
            (id: int, name: n, price: pri, description: des, categoryName: cn)
         - Before taking the order, check if the menu item exists.
         - Confirm these details from users: menu name, temperature, quantity, and 매장/포장.
         - Maintain conversation flow, and handle simultaneous inputs.
         - Ask one question at a time.
         2 :
         - When the user input completes, output only JSON.
            "takeout": "매장","totalPrice": 14400,"orderDetailRequestDtoList": ["menuName": "라떼","amount": 2,"price": 9600,"temperature": "hot","menuName": "라떼","amount": 1,"price": 4800,"temperature": "ice"]
         - "takeout" can be either "매장" or "포장".
         - "temperature" can be either "hot" or "ice".
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