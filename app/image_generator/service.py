import time

from app.database.database import SessionLocal
from app.database.models import Article
from app.image_generator.downloader import PexelsDownloader
from app.utils.logger import logger


class ImagePromptService:

    def __init__(self):

        self.downloader = PexelsDownloader()

    def run(self):

        db = SessionLocal()

        try:

            articles = (
                db.query(Article)
                .filter(
                    Article.is_hashtag_generated == True,
                    Article.is_image_prompt_generated == False
                )
                .limit(1)
                .all()
            )

            logger.info(f"Found {len(articles)} posts")

            for article in articles:

                logger.info(f"Downloading image for: {article.title}")

                try:

                    image_path = self.downloader.download(
                        article.title,
                        article.id
                    )

                    if image_path is None:
                        continue

                    article.image_path = image_path
                    article.is_image_prompt_generated = True

                    db.commit()

                    logger.success("Image downloaded successfully.")

                    time.sleep(2)

                except Exception as e:

                    db.rollback()

                    logger.exception(e)

        finally:

            db.close()