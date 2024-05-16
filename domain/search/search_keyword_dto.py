from pydantic import BaseModel
from typing import List

class SearchKeywords(BaseModel):
    ingredients: List[str]