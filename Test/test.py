import pytest

from Utilities.utiliy import get_login_data
from Pages.login_page import LoginPage


@pytest.mark.parametrize(
    "data",
    get_login_data()
)
def test_login(browserInstance, data):

    login_page = LoginPage(browserInstance)
    shop_page = login_page.login(
        data["username"],
        data["password"]
    )

    # Basic validation: inventory page should load after login
    assert "inventory.html" in browserInstance.current_url