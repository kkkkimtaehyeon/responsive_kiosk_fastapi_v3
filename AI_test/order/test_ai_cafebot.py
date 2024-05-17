from langchain_openai.chat_models import ChatOpenAI

from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory

import json
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

from .model_manage import CAFEBOT

llm = ChatOpenAI(
    api_key=os.getenv("SERV_KEY"),

    model_name= CAFEBOT,
    
    # get_num_tokens_from_messages() 오류 해결
    # tiktoken_model_name 토큰수 계산될 모델
    tiktoken_model_name="gpt-3.5-turbo",
    temperature=0.2,
    )


memory = ConversationBufferMemory(
    llm= llm,
    memory_key="history",        
    return_messages=True,
)

prompt = ChatPromptTemplate.from_messages(
    [
        (f"system", """As a coffee shop bot responding to customer orders
         """),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{order}")
    ]
)

chain = LLMChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=True
)


# json 포맷으로 변환 함수
def convert_json(result):
    try:
        json_data = json.loads(result)
        return json_data
    except ValueError:
        ai_result = {"ai_result": result}
        return ai_result


# fastapi에서 호출될 함수. 생성한 답변 반환
def cafebot_order(str):

    result = chain.predict(order = str)

    return convert_json(result)
    

# fastapi에서 호출될 함수. menu_prompt를 buffermemory내에 저장
def add_message_cafebot(menu_prompt):

    memory.chat_memory.add_ai_message(menu_prompt)