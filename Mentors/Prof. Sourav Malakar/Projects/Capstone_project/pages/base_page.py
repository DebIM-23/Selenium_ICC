import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.step_delay = 1.5  # Pause duration to comfortably view actions

    def open(self, url):
        self.driver.get(url)
        time.sleep(self.step_delay)

    # Alias so any call to open_url also works seamlessly
    open_url = open

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        time.sleep(self.step_delay)
        element.click()
        time.sleep(self.step_delay)

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        time.sleep(self.step_delay / 2)
        element.clear()
        element.send_keys(text)
        time.sleep(self.step_delay)

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_visible(self, locator):
        try:
            return bool(self.wait.until(EC.visibility_of_element_located(locator)))
        except TimeoutException:
            return False