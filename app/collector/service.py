from sqlalchemy.exc import IntegrityError

from app.database.database import SessionLocal
from app.database.models import Article
from app.collector.schemas import ArticleSchema
from app.utils.logger import logger


class ArticleService:

    @staticmethod
    def save(article: ArticleSchema):

        db = SessionLocal()

        try:

            existing = db.query(Article).filter(
                Article.url == article.url
            ).first()

            if existing:
                logger.warning(f"Already exists: {article.title}")
                return

            db_article = Article(
                title=article.title,
                source=article.source,
                url=article.url,
                summary=article.summary,
            )

            db.add(db_article)
            db.commit()

            logger.success(f"Saved: {article.title}")

        except IntegrityError:

            db.rollback()

        finally:

            db.close()