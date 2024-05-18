from langchain_openai.chat_models import ChatOpenAI

from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory

from .model_manage import KEYBOT

from dotenv import load_dotenv, find_dotenv
import os

_ = load_dotenv(find_dotenv())


llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY_EUNHAK"),
    
    model_name= KEYBOT,
    
    tiktoken_model_name="gpt-3.5-turbo",
    temperature=0.2,
    )

# 기억 저장
memory = ConversationBufferMemory(
    llm= llm,
    memory_key="history",        
    return_messages=True,
)

prompt = ChatPromptTemplate.from_messages(
    [
        (f"system", """As a coffee shop bot responding to customer orders, 
         if a sentence containing square brackets with keywords is input, please select all relevant items from the registered menus based on the keywords. 
         Provide the ids in ascending order and format it into JSON. Items enclosed in parentheses signify menu registration. 
         For any other input without brackets, handle the order conversationally as a human would.
         """),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{order}")
    ]
)

# 호출
chain_keybot = LLMChain(
    llm=llm,
    memory=memory,
    prompt=prompt,
    verbose=True
)