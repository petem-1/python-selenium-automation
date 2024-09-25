from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    search_results_header = (By.XPATH, "//div[@data-test='resultsHeading']")
    empty_cart_message = (By. CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def verify_results(self, product):
        self.verify_partial_text(product ,*self.search_results_header)

    def verify_results_of_url(self, product):
        self.verify_partial_url(product)

    def verify_cart_message(self):
            self.verify_text('Your cart is empty', *self.empty_cart_message)

    # def verify_text(self, expected_text, *locator):
    #     actual_text = self.find_element(*locator).text
    #     assert actual_text == expected_text, f'Expected {expected_text} did not match actual {actual_text}'
