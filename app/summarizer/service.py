import time

from app.database.database import SessionLocal
from app.database.models import Article
from app.summarizer.ai_summarizer import AISummarizer
from app.utils.logger import logger


class SummarizerService:

    def __init__(self):
        self.ai = AISummarizer()

    def run(self):

        db = SessionLocal()

        try:
            articles = (
                db.query(Article)
                .filter(Article.is_summarized == False)
                .order_by(Article.score.desc())
                .limit(5)
                .all()
            )

            logger.info("=" * 60)
            logger.info(f"Found {len(articles)} articles to summarize")
            logger.info("=" * 60)

            if not articles:
                logger.warning("No articles found for summarization.")
                return

            for index, article in enumerate(articles, start=1):

                logger.info(f"[{index}/{len(articles)}] Summarizing:")
                logger.info(article.title)

                max_retries = 3

                for attempt in range(max_retries):

                    try:

                        summary = self.ai.summarize(article)

                        article.ai_summary = summary
                        article.is_summarized = True

                        db.commit()

                        logger.success("✅ Summary saved successfully")

                        # Wait a little before the next API call
                        time.sleep(3)

                        break

                    except Exception as e:

                        db.rollback()

                        error = str(e)

                        # Handle Gemini rate limit
                        if "429" in error or "RESOURCE_EXHAUSTED" in error:

                            wait_time = 20 * (attempt + 1)

                            logger.warning(
                                f"Rate limit reached. Waiting {wait_time} seconds..."
                            )

                            time.sleep(wait_time)

                        else:

                            logger.error(f"Error: {error}")

                            break

        except Exception as e:

            logger.error(f"Summarizer Service Error: {e}")

        finally:

            db.close()