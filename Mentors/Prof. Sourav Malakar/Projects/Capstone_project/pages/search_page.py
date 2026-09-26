from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn-default.btn-lg")
    SEARCH_RESULTS_HEADER = (By.XPATH, "//h2[normalize-space()='Products meeting the search criteria']")
    PRODUCT_TITLES = (By.CSS_SELECTOR, "div.product-thumb h4 a")
    NO_PRODUCT_MESSAGE = (By.XPATH, "//p[contains(text(),'There is no product that matches')]")

    def search_product(self, product_name):
        self.enter_text(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def get_search_results_titles(self):
        elements = self.driver.find_elements(*self.PRODUCT_TITLES)
        return [el.text for el in elements]

    def has_no_product_message(self):
        return self.is_visible(self.NO_PRODUCT_MESSAGE)