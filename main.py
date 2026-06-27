import sys

from app.database.database import init_db
from app.runner.runner import ProjectRunner
from app.utils.logger import logger


def show_help():

    logger.info("")
    logger.info("Available Commands")
    logger.info("------------------------------")
    logger.info("python main.py collector")
    logger.info("python main.py summarizer")
    logger.info("python main.py writer")
    logger.info("python main.py reviewer")
    logger.info("python main.py hashtag")
    logger.info("python main.py image")
    logger.info("python main.py publisher")
    logger.info("python main.py all")
    logger.info("------------------------------")


def main():

    logger.info("🚀 LinkedIn AI Agent")

    init_db()

    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1].lower()

    commands = {
        "collector": ProjectRunner.collector,
        "summarizer": ProjectRunner.summarizer,
        "writer": ProjectRunner.writer,
        "reviewer": ProjectRunner.reviewer,
        "hashtag": ProjectRunner.hashtag,
        "image": ProjectRunner.image,
        "publisher": ProjectRunner.publisher,
        "all": ProjectRunner.all,
    }

    if command not in commands:
        logger.error(f"Unknown command: {command}")
        show_help()
        return

    commands[command]()


if __name__ == "__main__":
    main()