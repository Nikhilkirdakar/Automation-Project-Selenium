import pytest

from Pages.login_page import LoginPage


@pytest.mark.smoke
def test_commerce(browserInstance):


    browserInstance.get("https://www.saucedemo.com/")

    login_page = LoginPage(browserInstance)

    shop_page = login_page.login(
        "standard_user",
        "secret_sauce"
    )

    checkout_page = shop_page.add_to_cart(
        "Sauce Labs Backpack"
    )

    checkout_page.finalize(
        "Nikhil",
        "Kirdakar",
        "413118"
    )