from datetime import datetime


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, step):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        path = f"Screenshots/{step}_{timestamp}.png"

        self.driver.save_screenshot(path)