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

    id = Column(Integer, primary_key=True, index=True)

    # Original Article
    title = Column(String(500), nullable=False)
    source = Column(String(200))
    url = Column(String(1000), unique=True)
    summary = Column(Text)
    category = Column(String(100))
    published_at = Column(DateTime, default=datetime.utcnow)

    # Classification
    score = Column(Integer, default=0)

    # AI Summary
    ai_summary = Column(Text, nullable=True)
    is_summarized = Column(Boolean, default=False)

    # LinkedIn Post
    linkedin_post = Column(Text, nullable=True)
    is_post_generated = Column(Boolean, default=False)

    # Review
    reviewed_post = Column(Text, nullable=True)
    is_reviewed = Column(Boolean, default=False)

    # Hashtags
    hashtags = Column(Text, nullable=True)

    # Image
    image_prompt = Column(Text, nullable=True)
    image_url = Column(Text, nullable=True)

    # Publishing
    is_published = Column(Boolean, default=False)
    published_url = Column(Text, nullable=True)

    # Analytics
    likes = Column(Integer, default=0)
    comments = Column(Integer, default=0)
    impressions = Column(Integer, default=0)

    # Workflow
    used = Column(Boolean, default=False)

    created_at = Column(DateTime, default=datetime.utcnow)