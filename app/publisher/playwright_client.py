from pathlib import Path

from playwright.sync_api import sync_playwright
from app.utils.logger import logger


class PlaywrightClient:

    STORAGE_STATE = "storage/linkedin_state.json"

    def login(self):

        Path("storage").mkdir(exist_ok=True)

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=False,
                slow_mo=500
            )

            context = browser.new_context()

            page = context.new_page()

            page.goto("https://www.linkedin.com/login")

            logger.info("=" * 60)
            logger.info("Login to LinkedIn.")
            logger.info("After LinkedIn Home Page opens, press ENTER.")
            logger.info("=" * 60)

            input()

            context.storage_state(
                path=self.STORAGE_STATE
            )

            logger.success("Session Saved Successfully")

            browser.close()