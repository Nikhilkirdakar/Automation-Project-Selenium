from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.config import BASE_URL


def test_purchase_product(browserInstance):

    driver = browserInstance
    driver.get(BASE_URL)

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Open & Close Menu
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    # Wait until the close button is clickable (avoid click interception)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "react-burger-cross-btn"))
    ).click()

    # Add Sauce Labs Backpack to Cart
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")

    for product in products:
        product_name = product.find_element(
            By.CLASS_NAME,
            "inventory_item_name"
        ).text

        if product_name == "Sauce Labs Backpack":
            product.find_element(By.TAG_NAME, "button").click()
            break

    # Open Cart
    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    # Checkout
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(
        By.ID,
        "first-name"
    ).send_keys("Nikhil")

    driver.find_element(
        By.ID,
        "last-name"
    ).send_keys("Kirdakar")

    driver.find_element(
        By.ID,
        "postal-code"
    ).send_keys("413118")

    driver.find_element(By.ID, "continue").click()


    WebDriverWait(driver, 10).until(
        EC.url_contains("checkout-step-two")
    )
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "finish"))
    )
    # Finish Order
    driver.find_element(By.ID, "finish").click()

    # Validation
    success_message = driver.find_element(
        By.CLASS_NAME,
        "complete-header"
    ).text

    assert success_message == "Thank you for your order!"
