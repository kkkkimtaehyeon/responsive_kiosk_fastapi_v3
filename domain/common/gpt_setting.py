from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from langchain.chains import LLMChain
from langchain.prompts import MessagesPlaceholder
from langchain.memory import ConversationSummaryBufferMemory

# langchain은 프롬프트 템플릿을 만들고 작업할 수 있는 도구를 제공함. =>Template
# 빠른 참조. 프롬프트를 생성하기 위한 사전 정의 된 레시피. for 언어모델


import os
from dotenv import load_dotenv, find_dotenv

# 현 폴더에 없으면 상위폴더로 찾아가면서 .env 파일찾으면 로드
_ = load_dotenv(find_dotenv())

# import os 노출 안되게끔 윈도우 환경변수 OPENAI_API_KEY로 키값 넣기 가능
llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY_EUNHAK"),
    # model_name="gpt-3.5-turbo", default값
    # fine tuning된 모델을 사용. 
    # venv\Lib\site-packages\langchain_openai\chat_models\base.py
    # get_num_tokens_from_messages에 새로운 모델 이름 추가해야할것.
    # 패키지를 수정하는 일은, 배포에 알맞지 않은 방식
    model_name="ft:gpt-3.5-turbo-0125:personal:cafebot:9Ly4475o",
    temperature=0.2,
    # max_tokens=40
    )


memory = ConversationSummaryBufferMemory(
    llm= llm,
    max_token_limit=400,
    memory_key="history",        
    return_messages=True,
)


prompt = ChatPromptTemplate.from_messages(
    [
        (f"system", """You're a coffee shop attendant. Respond to customer orders."""),
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