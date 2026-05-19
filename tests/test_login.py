from pages.login_page import LoginPage
from utils.logger import get_logger
from utils.screenshot import take_screenshot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = get_logger()

def test_login(driver):
    driver = driver
    login_page = LoginPage(driver)

    try:
        logger.info("Starting login test")

        login_page.login("admin", "1234")
        logger.info("Login attempted")

        # Wait up to 10s for the URL to contain 'dashboard'
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
        assert "dashboard" in driver.current_url

        logger.info("Login successful")

    except Exception:
        # logs traceback and preserves original exception when re-raising
        logger.exception("Test failed")
        screenshot_path = take_screenshot(driver, "login_failure")
        logger.error(f"Screenshot saved at {screenshot_path}")
        raise
