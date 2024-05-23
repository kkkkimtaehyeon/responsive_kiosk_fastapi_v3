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
    temperature=0,
    
    tiktoken_model_name="gpt-3.5-turbo",
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
#          Currently, there are no menu items, and the following will be registered.
#          : (id: int, name: n, price: pri, description: des, categoryName: cn)
#          Square brackets with keywords as input, find all relevant items from currently registered menus, then gen JSON.
#          : "menuList": [("id": int,"name": "n"),("id": int,"name": "n")]
#          Output only the JSON object without any additional text or formatting.
#          If no matching menu item is found, output 'n' word.
#          """),
#         MessagesPlaceholder(variable_name="history"),
#         ("human", "{question}")
#     ]
# )

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", """
         Currently no menu items available.
         Do not include any formatting or code block syntax.
         You MUST select registered menu items matching the keyword, including all related menu items, and you MUST respond only with a JSON object containing a 'menuList' array. Each item in the array should have an 'id' int and a 'name' str.
         If no matches, respond only "n" word not json.
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