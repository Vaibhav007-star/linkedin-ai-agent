from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///database/posts.db"
    )

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()