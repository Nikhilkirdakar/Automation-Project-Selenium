from datetime import datetime
import os


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, step):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        os.makedirs("Screenshots", exist_ok=True)
        path = os.path.join("Screenshots", f"{step}_{timestamp}.png")

        self.driver.save_screenshot(path)