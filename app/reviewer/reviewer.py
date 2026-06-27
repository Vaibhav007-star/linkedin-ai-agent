from app.ai.client import AIClient
from app.reviewer.prompts import REVIEW_PROMPT


class Reviewer:

    def __init__(self):
        self.ai = AIClient()

    def review(self, post: str):

        prompt = REVIEW_PROMPT.format(
            post=post
        )

        return self.ai.generate(prompt)