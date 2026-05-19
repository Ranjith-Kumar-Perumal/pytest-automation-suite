from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:
    """
    Base Page class with common actions for all page objects
    Connected to conftest driver fixture
    """
    
    def __init__(self, driver):
        """
        Initialize BasePage with driver from conftest fixture
        
        Args:
            driver: WebDriver instance from conftest
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    # ==================== Navigation ====================
    def navigate_to(self, url):
        """Navigate to a specific URL"""
        self.driver.get(url)
    
    def get_current_url(self):
        """Get the current URL"""
        return self.driver.current_url
    
    def refresh_page(self):
        """Refresh the current page"""
        self.driver.refresh()
    
    def go_back(self):
        """Go back to previous page"""
        self.driver.back()
    
    def go_forward(self):
        """Go forward to next page"""
        self.driver.forward()
    
    # ==================== Element Locators ====================
    def find_element(self, locator):
        """
        Find an element using the given locator
        
        Args:
            locator: Tuple of (By, value) e.g., (By.ID, "element_id")
        
        Returns:
            WebElement
        """
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        """Find multiple elements matching the locator"""
        return self.driver.find_elements(*locator)
    
    # ==================== Wait Actions ====================
    def wait_for_element_presence(self, locator, timeout=10):
        """Wait for element to be present in DOM"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def wait_for_element_visibility(self, locator, timeout=10):
        """Wait for element to be visible"""
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_for_element_clickability(self, locator, timeout=10):
        """Wait for element to be clickable"""
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def wait_for_element_invisibility(self, locator, timeout=10):
        """Wait for element to become invisible"""
        self.wait.until(EC.invisibility_of_element_located(locator))
    
    def wait_for_text_in_element(self, locator, text, timeout=10):
        """Wait for specific text to appear in element"""
        self.wait.until(EC.text_to_be_present_in_element(locator, text))
    
    # ==================== Click Actions ====================
    def click_element(self, locator):
        """Click on an element"""
        element = self.wait_for_element_clickability(locator)
        element.click()
    
    def double_click_element(self, locator):
        """Double click on an element"""
        element = self.find_element(locator)
        ActionChains(self.driver).double_click(element).perform()
    
    def right_click_element(self, locator):
        """Right click (context menu) on an element"""
        element = self.find_element(locator)
        ActionChains(self.driver).right_click(element).perform()
    
    # ==================== Text Actions ====================
    def send_keys(self, locator, text):
        """Send text to an input field"""
        element = self.wait_for_element_visibility(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator):
        """Get text from an element"""
        element = self.wait_for_element_visibility(locator)
        return element.text
    
    def get_attribute(self, locator, attribute):
        """Get an attribute value from an element"""
        element = self.find_element(locator)
        return element.get_attribute(attribute)
    
    # ==================== Dropdown Actions ====================
    def select_dropdown_by_value(self, locator, value):
        """Select option from dropdown by value"""
        from selenium.webdriver.support.select import Select
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_value(value)
    
    def select_dropdown_by_visible_text(self, locator, text):
        """Select option from dropdown by visible text"""
        from selenium.webdriver.support.select import Select
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)
    
    # ==================== State Checks ====================
    def is_element_present(self, locator):
        """Check if element is present in DOM"""
        try:
            self.find_element(locator)
            return True
        except:
            return False
    
    def is_element_visible(self, locator):
        """Check if element is visible"""
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False
    
    def is_element_enabled(self, locator):
        """Check if element is enabled"""
        element = self.find_element(locator)
        return element.is_enabled()
    
    def is_element_selected(self, locator):
        """Check if element is selected (checkbox/radio)"""
        element = self.find_element(locator)
        return element.is_selected()
    
    # ==================== Scroll Actions ====================
    def scroll_to_element(self, locator):
        """Scroll to an element"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def scroll_to_top(self):
        """Scroll to the top of the page"""
        self.driver.execute_script("window.scrollTo(0, 0);")
    
    def scroll_to_bottom(self):
        """Scroll to the bottom of the page"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # ==================== Window/Tab Actions ====================
    def switch_to_new_tab(self):
        """Switch to the latest opened tab/window"""
        self.driver.switch_to.window(self.driver.window_handles[-1])
    
    def switch_to_tab(self, tab_index):
        """Switch to a specific tab by index"""
        self.driver.switch_to.window(self.driver.window_handles[tab_index])
    
    def close_current_tab(self):
        """Close the current tab"""
        self.driver.close()
    
    def get_window_title(self):
        """Get the current window title"""
        return self.driver.title
    
    # ==================== Alert Actions ====================
    def accept_alert(self):
        """Accept an alert"""
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
    
    def dismiss_alert(self):
        """Dismiss/cancel an alert"""
        alert = self.wait.until(EC.alert_is_present())
        alert.dismiss()
    
    def get_alert_text(self):
        """Get text from an alert"""
        alert = self.wait.until(EC.alert_is_present())
        return alert.text
    
    def send_text_to_alert(self, text):
        """Send text to an alert prompt"""
        alert = self.wait.until(EC.alert_is_present())
        alert.send_keys(text)
    
    # ==================== JavaScript Execution ====================
    def execute_script(self, script, *args):
        """Execute JavaScript code"""
        return self.driver.execute_script(script, *args)
    
    def highlight_element(self, locator):
        """Highlight an element (useful for debugging)"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].style.border='3px solid red';", element)
    
    # ==================== Keyboard Actions ====================
    def press_enter(self):
        """Press Enter key"""
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
    
    def press_escape(self):
        """Press Escape key"""
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
    
    def press_tab(self):
        """Press Tab key"""
        ActionChains(self.driver).send_keys(Keys.TAB).perform()
