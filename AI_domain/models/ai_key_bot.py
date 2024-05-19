from langchain_openai.chat_models import ChatOpenAI

from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory

# from .model_manage import KEYBOT
from .model_manage import GPT4O

from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())


llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY_EUNHAK"),
    
    # model_name= KEYBOT,
    model_name= GPT4O,
    
    tiktoken_model_name="gpt-3.5-turbo",
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
         Items enclosed in parentheses signify menu registration. 
         ex: (id: 3, name: 딸기주스, price: 5500, description: 딸기를 갈아 넣은 주스, categoryName: 주스)
         If a sentence containing square brackets with keywords is input, please select all relevant items from the registered menus based on the keywords, and then provide the IDs in ascending order and format it into JSON. 
         ex: ("menuList": [("id": 1,"name": "아메리카노"),("id": 2,"name": "라떼")])
         When you gen answer, you don't need new lines, special characters, etc.
         """),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}")
    ]
)

# 호출
chain_keybot = LLMChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=True
)