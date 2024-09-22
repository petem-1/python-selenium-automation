from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


# @when('Search for a product')
# def search_product(context):
#     # Search field => enter tea
#     context.driver.find_element(By.ID, 'search').send_keys('tea')
#     # Search button => click
#     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#     sleep(5)  # wait for search results page to load
#
#
# @then('Verify that correct search results shown')
# def verify_results(context):
#     actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
#     expected_result = 'tea'
#     assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'
#
# @when('Click on Cart icon')
# def click_cart(context):
#         # Click on Cart
#         context.driver.find_element(By. CSS_SELECTOR, "[data-test='@web/CartIcon']").click()
#         sleep(5)  # wait for search results page to load
#
# @then('Verify “Your cart is empty” message is shown')
# def verify_results(context):
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
