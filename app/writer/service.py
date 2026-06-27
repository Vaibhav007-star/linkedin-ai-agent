import time

from app.database.database import SessionLocal
from app.database.models import Article
from app.utils.logger import logger
from app.writer.linkedin_writer import LinkedInWriter


class WriterService:

    def __init__(self):
        self.writer = LinkedInWriter()

    def run(self):

        db = SessionLocal()

        try:

            articles = (
                db.query(Article)
                .filter(
                    Article.is_summarized == True,
                    Article.is_post_generated == False
                )
                .limit(5)
                .all()
            )

            logger.info("=" * 60)
            logger.info(f"Found {len(articles)} articles for LinkedIn posts")
            logger.info("=" * 60)

            for article in articles:

                logger.info(f"Writing post: {article.title}")

                try:

                    post = self.writer.write_post(
                        article.ai_summary
                    )

                    article.linkedin_post = post
                    article.is_post_generated = True

                    db.commit()

                    logger.success("LinkedIn post saved")

                    time.sleep(3)

                except Exception as e:

                    db.rollback()

                    logger.error(e)

        finally:

            db.close()