AI_KEYWORDS = {
    "ai",
    "artificial intelligence",
    "machine learning",
    "deep learning",
    "llm",
    "gpt",
    "openai",
    "claude",
    "gemini",
    "python",
    "automation",
    "agent",
    "agents",
    "langchain",
    "langgraph",
    "ml",
    "nlp",
    "computer vision",
    "data science",
    "transformer",
    "rag",
    "vector database",
    "embedding",
}


class TopicFilter:

    @staticmethod
    def is_relevant(article):

        text = (
            f"{article.title} "
            f"{article.summary}"
        ).lower()

        return any(keyword in text for keyword in AI_KEYWORDS)