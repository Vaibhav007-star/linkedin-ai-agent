from app.collector.rss_collector import RSSCollector
from app.database.database import init_db
from app.summarizer.service import SummarizerService
from app.utils.logger import logger
from config.settings import settings
from app.writer.service import WriterService


def main():

    logger.info("🚀 LinkedIn AI Agent Started")
    logger.info(f"Database: {settings.DATABASE_URL}")

    init_db()

    logger.success("Database Initialized Successfully")

    # Collect RSS articles
    collector = RSSCollector()
    collector.collect()

    # Summarize articles with Gemini
    summarizer = SummarizerService()
    summarizer.run()
    writer = WriterService()
    writer.run()

    logger.success("Project Finished Successfully")


if __name__ == "__main__":
    main()