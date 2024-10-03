from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#Target
@when('Click on Cart icon')
def click(context):
    context.app.cart_page.click_cart(context.driver)
#         # Click on Cart
#         context.driver.find_element(By. CSS_SELECTOR, "[data-test='@web/CartIcon']").click()
#         sleep(5)  # wait for search results page to load
#
@then('Verify “Your cart is empty” message is shown')
def verify_text(context):
    context.app.search_results_page.verify_cart_message()
#         actual_result = context.driver.find_element(By. CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
#         expected_result = 'Your cart is empty'
#         assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'
#
#
# @when('Click Sign In')
# def click_sign_in(context):
#         context.driver.find_element(By.CSS_SELECTOR, "[class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()
#         sleep(2)  # wait for search results page to load
#
# @when('Click Sign In From Side Menu')
# def click_signin_nav(context):
#         context.driver.find_element(By. CSS_SELECTOR, "[class='sc-859e7637-0 hHZPQy']").click()
#         sleep(2)  # wait for search results page to load
#
# @then('Verify Sign In form opened')
# def verify_results(context):
#         actual_result = context.driver.find_element(By. CSS_SELECTOR, ".WObnm").text
#         expected_result = 'Sign into your Target account'
#         assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'
#
