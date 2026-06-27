from loguru import logger
import sys

# Remove the default logger
logger.remove()

# Console logger
logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
           "<level>{message}</level>",
)

# Optional: Save logs to a file
logger.add(
    "logs/app.log",
    rotation="10 MB",
    retention="7 days",
    level="INFO",
    encoding="utf-8",
)

# Export the logger
__all__ = ["logger"]