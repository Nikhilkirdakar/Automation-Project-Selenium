import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser name"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode"
    )


@pytest.fixture(scope="function")
def browserInstance(request):

    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption("headless")

    if browser_name.lower() == "chrome":
        options = ChromeOptions()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-notifications")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")

        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser_name.lower() == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")

        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(5)
    try:
        driver.maximize_window()
    except Exception:
        driver.set_window_size(1920, 1080)

    yield driver

    driver.quit()
