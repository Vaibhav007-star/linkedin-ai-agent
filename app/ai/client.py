from google import genai

from config.settings import settings
from app.ai.models import GEMINI_FLASH


class AIClient:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate(self, prompt):

        response = self.client.models.generate_content(
            model=GEMINI_FLASH,
            contents=prompt
        )

        return response.text