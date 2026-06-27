import feedparser

from app.collector.rss_feeds import RSS_FEEDS
from app.collector.parser import RSSParser
from app.collector.service import ArticleService
from app.collector.filters import TopicFilter
from app.utils.logger import logger


class RSSCollector:

    def collect(self):

        logger.info("Starting RSS Collection")

        total = 0
        saved = 0
        skipped = 0

        for feed in RSS_FEEDS:

            logger.info(f"Reading {feed['name']}")

            parsed = feedparser.parse(feed["url"])

            logger.info(f"Found {len(parsed.entries)} articles")

            for entry in parsed.entries[:5]:

                total += 1

                article = RSSParser.parse(
                    entry,
                    feed["name"]
                )

                if TopicFilter.is_relevant(article):

                    ArticleService.save(article)
                    saved += 1

                else:

                    logger.warning(f"Skipped: {article.title}")
                    skipped += 1

        logger.info("=" * 50)
        logger.info(f"Articles Read : {total}")
        logger.info(f"Saved         : {saved}")
        logger.info(f"Skipped       : {skipped}")
        logger.info("=" * 50)