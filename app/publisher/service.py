from pathlib import Path

from app.database.database import SessionLocal
from app.database.models import Article
from app.publisher.playwright_client import PlaywrightClient
from app.utils.logger import logger


class PublisherService:

    def run(self):

        db = SessionLocal()

        try:

            article = (
                db.query(Article)
                .filter(
                    Article.is_reviewed == True,
                    Article.is_published == False
                )
                .order_by(Article.score.desc())
                .first()
            )

            if article is None:
                logger.warning("No approved articles available.")
                return

            logger.success(f"Selected Article: {article.title}")

            logger.info("=" * 60)
            logger.info(article.reviewed_post)
            logger.info("=" * 60)

            state = Path("storage/linkedin_state.json")

            client = PlaywrightClient()

            if not state.exists():

                logger.warning("LinkedIn login required.")

                client.login()

            else:

                logger.success("LinkedIn session found.")

                # Playwright publishing will be added next.

        finally:

            db.close()