from pathlib import Path

from playwright.sync_api import sync_playwright

from app.utils.logger import logger


class PlaywrightClient:

    STORAGE_STATE = "storage/linkedin_state.json"

    # -------------------------
    # Login
    # -------------------------
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
            logger.info("Login to LinkedIn")
            logger.info("After LinkedIn Home opens, press ENTER")
            logger.info("=" * 60)

            input()

            context.storage_state(path=self.STORAGE_STATE)

            logger.success("Session Saved Successfully")

            browser.close()

    # -------------------------
    # Open LinkedIn
    # -------------------------
    def open(self):

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=False,
            slow_mo=500
        )

        self.context = self.browser.new_context(
            storage_state=self.STORAGE_STATE
        )

        self.page = self.context.new_page()

        self.page.goto("https://www.linkedin.com/feed")

        self.page.wait_for_timeout(5000)

        logger.success("LinkedIn opened successfully.")

    # -------------------------
    # Upload Image
    # -------------------------
    def upload_image(self, image_path: str):

        if not image_path:
            logger.warning("No image available.")
            return

        logger.info("Waiting for image dialog...")

        input("Click 'Start a post', then 'Add media', then press ENTER...")

        file_input = self.page.locator("input[type='file']").first

        file_input.set_input_files(image_path)

        self.page.wait_for_timeout(5000)

        logger.success("Image uploaded successfully.")

    # -------------------------
    # Create Post
    # -------------------------
    def create_post(self, post: str):

        editor = self.page.locator("div[role='textbox']").first

        editor.fill(post)

        logger.success("Post inserted successfully.")

    # -------------------------
    # Publish
    # -------------------------
    def publish(self):

        logger.info("=" * 60)
        logger.info("Review the post.")
        logger.info("Press ENTER to publish.")
        logger.info("=" * 60)

        input()

        self.page.get_by_role(
            "button",
            name="Post"
        ).click()

        self.page.wait_for_timeout(5000)

        logger.success("Post published successfully!")

    # -------------------------
    # Close
    # -------------------------
    def close(self):

        self.context.close()

        self.browser.close()

        self.playwright.stop()