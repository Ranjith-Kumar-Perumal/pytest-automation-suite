import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """
    Setup and teardown logic for ChromeDriver
    - scope="function": Creates a new driver for each test
    - Setup: Initializes ChromeDriver with options
    - Teardown: Closes the browser and quits the driver
    """
    
    # Setup: Initialize ChromeDriver with options
    chrome_options = webdriver.ChromeOptions()
    
    # Optional: Add Chrome options for better performance and stability
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Initialize the ChromeDriver from venv or webdriver-manager
    chromedriver_path = r"C:\Work\Setup\Selenium\venv\Scripts\chromedriver.exe"
    
    if os.path.exists(chromedriver_path):
        driver = webdriver.Chrome(
            service=Service(chromedriver_path),
            options=chrome_options
        )
    else:
        # Fallback to webdriver-manager if venv chromedriver not found
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
    
    # Set implicit wait
    driver.implicitly_wait(10)
    
    yield driver
    
    # Teardown: Close the browser and quit the driver
    driver.quit()


@pytest.fixture(scope="session")
def chrome_options():
    """
    Provides Chrome options configuration that can be reused across tests
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return options


@pytest.fixture(scope="session")
def login_url():
    """Provide the login page URL for tests."""
    # Update this value to match your application login page.
    return os.getenv("LOGIN_URL", "https://practicetestautomation.com/practice-test-login/")
