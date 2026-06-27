from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.settings import settings
from app.database.models import Base

# Ensure the database folder exists
Path("database").mkdir(exist_ok=True)

engine = create_engine(
    settings.DATABASE_URL,
    echo=False,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def init_db():
    Base.metadata.create_all(bind=engine)