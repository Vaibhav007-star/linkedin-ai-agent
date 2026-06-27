from app.ai.client import AIClient
from app.writer.prompts import LINKEDIN_POST_PROMPT


class LinkedInWriter:

    def __init__(self):
        self.ai = AIClient()

    def write_post(self, summary):

        prompt = LINKEDIN_POST_PROMPT.format(
            summary=summary
        )

        return self.ai.generate(prompt)