from app.database.database import SessionLocal
from app.database.models import Article
from app.reviewer.reviewer import Reviewer
from app.utils.logger import logger


class ReviewerService:

    def __init__(self):
        self.reviewer = Reviewer()

    def run(self):

        db = SessionLocal()

        try:

            articles = (
                db.query(Article)
                .filter(
                    Article.is_post_generated == True,
                    Article.is_reviewed == False
                )
                .limit(1)
                .all()
            )

            logger.info(f"Found {len(articles)} posts to review")

            for article in articles:

                logger.info(f"Reviewing: {article.title}")

                reviewed = self.reviewer.review(
                    article.linkedin_post
                )

                article.reviewed_post = reviewed
                article.is_reviewed = True

                db.commit()

                logger.success("Post reviewed successfully")

        except Exception as e:

            db.rollback()
            logger.error(e)

        finally:

            db.close()