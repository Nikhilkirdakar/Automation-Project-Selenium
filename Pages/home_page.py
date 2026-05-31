from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.base_page import BasePage
from Pages.checkout_page import CheckoutPage

class ShopPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.menu = (By.ID, "react-burger-menu-btn")
        self.close = (By.CSS_SELECTOR, "#react-burger-cross-btn")
        self.item = (By.CLASS_NAME, "inventory_item")
        self.cart = (By.CLASS_NAME, "shopping_cart_link")

    def cart_page(self):
        self.driver.find_element(*self.menu).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.close)).click()

    def add_to_cart(self, product_name):
        products = self.driver.find_elements(*self.item)
        for product in products:
            product_title = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            if product_title == product_name:
                product.find_element(By.TAG_NAME, "button").click()
                break

        self.driver.find_element(*self.cart).click()
        checkout = CheckoutPage(self.driver)
        self.take_screenshot("cart_page")
        return checkout
