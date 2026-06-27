from app.collector.rss_collector import RSSCollector
from app.summarizer.service import SummarizerService
from app.writer.service import WriterService
from app.reviewer.service import ReviewerService
from app.utils.logger import logger
from app.hashtag.service import HashtagService
from app.image_generator.service import ImagePromptService
from app.publisher.service import PublisherService

class ProjectRunner:

    @staticmethod
    def collector():
        logger.info("Running Collector...")
        RSSCollector().collect()

    @staticmethod
    def summarizer():
        logger.info("Running Summarizer...")
        SummarizerService().run()

    @staticmethod
    def writer():
        logger.info("Running Writer...")
        WriterService().run()

    @staticmethod
    def reviewer():
        logger.info("Running Reviewer...")
        ReviewerService().run()

     
    @staticmethod
    def hashtag():
        logger.info("Running Hashtag Generator...")
        HashtagService().run()

    @staticmethod
    def image():
        logger.info("Running Image Prompt Generator...")
        ImagePromptService().run()


    @staticmethod
    def publisher():
        logger.info("Running Publisher...")
        PublisherService().run()

    @staticmethod
    def all():
        logger.info("Running Full Pipeline...")

        RSSCollector().collect()
        SummarizerService().run()
        WriterService().run()
        ReviewerService().run()
        HashtagService().run()
        ImagePromptService().run()
        PublisherService().run()

  
    
    logger.success("Pipeline Completed Successfully")