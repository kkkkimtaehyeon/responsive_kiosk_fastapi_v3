from pydantic import BaseModel
from typing import List
# Pydantic 모델들 정의


# 메뉴 저장
class TestMenu2(BaseModel):
    id: int
    name: str
    price: float
    description: str
    categoryName: str


# 사용자 질문
class UserScript(BaseModel):
    userScript: str


# 키워드 리스트
class TestSearchKeywords(BaseModel):
    ingredients: List[str]