from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By

class Cart(Page):
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")

    def click_cart(self, text):
        self.wait_to_be_clickable_click(*self.CART_ICON)
        # self.click(*self.CART_ICON)
        sleep(6)