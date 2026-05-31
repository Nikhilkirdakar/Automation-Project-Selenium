from selenium.webdriver.common.by import By

from Page_Object.Checkout_Page import Checkout_Page
from Utilities.BasePage import BasePage


class Shop_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.menu = (By.ID, "react-burger-menu-btn")
        self.close = (By.CSS_SELECTOR, "#react-burger-cross-btn")
        self.item = (By.CLASS_NAME, "inventory_item")
        self.cart = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_button= (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")



    def cart_page(self):
        self.driver.find_element(*self.menu).click()
        self.driver.find_element(*self.close).click()

    def add_to_cart(self, product_name):

        products = self.driver.find_elements(*self.item)

        for product in products:
            product_title = product.find_element(
                By.CLASS_NAME,
                "inventory_item_name"
            ).text

            if product_title == product_name:
                product.find_element(By.TAG_NAME, "button").click()
                break

        self.driver.find_element(*self.cart).click()
    
        checkout = Checkout_Page(self.driver)
        self.take_screenshot("cart_page")
        return checkout

