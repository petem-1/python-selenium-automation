from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    EMPTY_CART_MESSAGE = (By. CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def verify_results(self, product):
        self.verify_partial_text(product ,*self.SEARCH_RESULTS_HEADER)

    def verify_results_of_url(self, product):
        self.verify_partial_url(product)

    def verify_cart_message(self):
            self.verify_text('Your cart is empty', *self.EMPTY_CART_MESSAGE)

    # def verify_text(self, expected_text, *locator):
    #     actual_text = self.find_element(*locator).text
    #     assert actual_text == expected_text, f'Expected {expected_text} did not match actual {actual_text}'
