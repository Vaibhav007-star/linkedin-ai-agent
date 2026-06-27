from app.collector.schemas import ArticleSchema


class RSSParser:

    @staticmethod
    def parse(entry, source):

        return ArticleSchema(
            title=entry.get("title", ""),
            source=source,
            url=entry.get("link", ""),
            summary=entry.get("summary", ""),
            published=entry.get("published", ""),
        )