
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.BasePage import BasePage


class Checkout_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.name_field = (By.ID, "first-name")
        self.last_name_field =(By.CSS_SELECTOR, "#last-name")
        self.pincode= (By.CSS_SELECTOR, "#postal-code")
        self.submit = (By.ID, "continue")
        self.finish = (By.ID, "finish")
        self.text = (By.XPATH, "//h2[@class='complete-header']")


    def finalize(self,first_name,last_name,pincode):

        self.driver.find_element(*self.checkout_button).click()
        self.take_screenshot("checkout_information")
        self.driver.find_element(*self.name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.pincode).send_keys(pincode)
        self.driver.find_element(*self.submit).click()

        self.take_screenshot("order_overview")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish)
        )
        self.take_screenshot("before_finish")
        self.driver.find_element(*self.finish).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.text)
        )

        self.take_screenshot("order_success")

        success_text = self.driver.find_element(*self.text).text
        assert "Thank you " in success_text
