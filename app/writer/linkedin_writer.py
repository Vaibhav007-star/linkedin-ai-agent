from google import genai

from config.settings import settings
from app.writer.prompts import LINKEDIN_POST_PROMPT


class LinkedInWriter:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def write_post(self, summary):

        prompt = LINKEDIN_POST_PROMPT.format(
            summary=summary
        )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text