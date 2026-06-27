from pydantic import BaseModel
from typing import Optional


class ArticleSchema(BaseModel):
    title: str
    source: str
    url: str
    summary: Optional[str] = None
    published: Optional[str] = None