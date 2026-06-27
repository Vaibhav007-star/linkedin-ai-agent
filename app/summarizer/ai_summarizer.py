from google import genai

from config.settings import settings
from app.summarizer.prompts import SUMMARY_PROMPT


class AISummarizer:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def summarize(self, article):

        prompt = SUMMARY_PROMPT.format(
            title=article.title,
            content=article.summary
        )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text