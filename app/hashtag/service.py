import time

from app.database.database import SessionLocal
from app.database.models import Article
from app.hashtag.generator import HashtagGenerator
from app.utils.logger import logger


class HashtagService:

    def __init__(self):
        self.generator = HashtagGenerator()

    def run(self):

        db = SessionLocal()

        try:

            articles = (
                db.query(Article)
                .filter(
                    Article.is_reviewed == True,
                    Article.is_hashtag_generated == False
                )
                .limit(1)
                .all()
            )

            logger.info(f"Found {len(articles)} posts")

            for article in articles:

                logger.info(f"Generating hashtags for: {article.title}")

                try:

                    hashtags = self.generator.generate(
                        article.reviewed_post
                    )

                    article.hashtags = hashtags
                    article.is_hashtag_generated = True

                    db.commit()

                    logger.success("Hashtags generated")

                    time.sleep(5)

                except Exception as e:

                    db.rollback()

                    logger.error(e)

        finally:

            db.close()