from pathlib import Path

import requests

from app.config.settings import settings
from app.utils.logger import logger


class PexelsDownloader:

    BASE_URL = "https://api.pexels.com/v1/search"

    def __init__(self):

        Path("storage/images").mkdir(
            parents=True,
            exist_ok=True
        )

    def download(
        self,
        query: str,
        article_id: int
    ):

        logger.info(f"Searching image for: {query}")

        headers = {
            "Authorization": settings.PEXELS_API_KEY
        }

        params = {
            "query": query,
            "per_page": 1,
            "orientation": "landscape"
        }

        response = requests.get(
            self.BASE_URL,
            headers=headers,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        if not data.get("photos"):
            logger.warning("No image found.")
            return None

        image_url = data["photos"][0]["src"]["large"]

        image = requests.get(
            image_url,
            timeout=30
        )

        image_path = f"storage/images/article_{article_id}.jpg"

        with open(image_path, "wb") as file:
            file.write(image.content)

        logger.success(f"Image saved: {image_path}")

        return image_path