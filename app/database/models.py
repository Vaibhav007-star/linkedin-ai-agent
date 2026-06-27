from datetime import datetime

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Article(Base):
    __tablename__ = "articles"

    # ==========================
    # Primary Key
    # ==========================
    id = Column(Integer, primary_key=True, index=True)

    # ==========================
    # Original RSS Article
    # ==========================
    title = Column(String(500), nullable=False)
    source = Column(String(200))
    url = Column(String(1000), unique=True)
    summary = Column(Text)
    category = Column(String(100))
    score = Column(Integer, default=0)

    # ==========================
    # AI Generated Content
    # ==========================
    ai_summary = Column(Text, nullable=True)

    linkedin_post = Column(Text, nullable=True)

    reviewed_post = Column(Text, nullable=True)

    hashtags = Column(Text, nullable=True)

    image_prompt = Column(Text, nullable=True)

    image_url = Column(Text, nullable=True)

    # ==========================
    # Workflow Status
    # ==========================
    used = Column(Boolean, default=False)

    is_summarized = Column(Boolean, default=False)

    is_post_generated = Column(Boolean, default=False)

    is_reviewed = Column(Boolean, default=False)

    is_hashtag_generated = Column(Boolean, default=False)

    is_image_prompt_generated = Column(Boolean, default=False)

    is_published = Column(Boolean, default=False)

    # ==========================
    # Publishing
    # ==========================
    published_url = Column(Text, nullable=True)

    # ==========================
    # Analytics
    # ==========================
    likes = Column(Integer, default=0)

    comments = Column(Integer, default=0)

    impressions = Column(Integer, default=0)

    # ==========================
    # Dates
    # ==========================
    created_at = Column(DateTime, default=datetime.utcnow)

    published_at = Column(DateTime, nullable=True)