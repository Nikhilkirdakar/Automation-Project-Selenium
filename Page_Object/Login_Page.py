from selenium.webdriver.common.by import By
from Utilities.BasePage import BasePage
from Page_Object.Shop_Page import Shop_Page


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.User_name = (By.ID, "user-name")
        self.Password = (By.CSS_SELECTOR, "input[type='password']")
        self.submit_button = (By.XPATH, "//input[@type='submit']")

    def login(self, username, password):

        self.driver.find_element(*self.User_name).send_keys(username)
        self.take_screenshot("username_entered")

        self.driver.find_element(*self.Password).send_keys(password)
        self.take_screenshot("password_entered")

        self.driver.find_element(*self.submit_button).click()
        self.take_screenshot("login_clicked")

        return Shop_Page(self.driver)