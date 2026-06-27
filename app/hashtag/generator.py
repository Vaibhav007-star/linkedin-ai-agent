from app.ai.client import AIClient
from app.hashtag.prompts import HASHTAG_PROMPT


class HashtagGenerator:

    def __init__(self):
        self.ai = AIClient()

    def generate(self, post: str):

        prompt = HASHTAG_PROMPT.format(
            post=post
        )

        return self.ai.generate(prompt)