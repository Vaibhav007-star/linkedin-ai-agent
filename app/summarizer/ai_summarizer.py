from app.ai.client import AIClient
from app.summarizer.prompts import SUMMARY_PROMPT


class AISummarizer:

    def __init__(self):
        self.ai = AIClient()

    def summarize(self, article):

        prompt = SUMMARY_PROMPT.format(
            title=article.title,
            content=article.summary
        )

        return self.ai.generate(prompt)