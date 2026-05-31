import pytest

from Utilities.utiliy import get_login_data


@pytest.mark.parametrize(

    "data",
    get_login_data()
)
def test_login(browserInstance, data):

    login.login(
        data["username"],
        data["password"]
    )