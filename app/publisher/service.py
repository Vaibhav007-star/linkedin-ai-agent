from pathlib import Path
from datetime import datetime

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

            logger.success("LinkedIn session found.")

            # -----------------------------
            # Build LinkedIn Post
            # -----------------------------

            post = article.reviewed_post

            if article.hashtags:
                post += "\n\n" + article.hashtags

            # -----------------------------
            # Publish
            # -----------------------------

            client.open()

            client.upload_image(article.image_path)

            client.create_post(article.reviewed_post)

            client.publish()

            client.close()  



            # -----------------------------
            # Update Database
            # -----------------------------

            article.is_published = True
            article.published_at = datetime.utcnow()

            db.commit()

            logger.success("Database updated successfully.")

        except Exception as e:

            db.rollback()

            logger.exception(e)

        finally:

            db.close()