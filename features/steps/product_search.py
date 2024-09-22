from behave import given, when, then
from time import sleep


# SEARCH_INPUT = (By.NAME, 'q')
# SEARCH_SUBMIT = (By.NAME, 'btnK')


# @given('Open Google page')
# def open_google(context):
#     context.driver.get('https://www.google.com/')
#
#
# @when('Input {search_word} into search field')
# def input_search(context, search_word):
#     search = context.driver.find_element(*SEARCH_INPUT)
#     search.clear()
#     search.send_keys(search_word)
#     sleep(4)
#
#
# @when('Click on search icon')
# def click_search_icon(context):
#     context.driver.find_element(*SEARCH_SUBMIT).click()
#     sleep(1)
#
#
# @then('Product results for {search_word} are shown')
# def verify_found_results_text(context, search_word):
#     assert search_word.lower() in context.driver.current_url.lower(), \
#         f'Expected query not in {context.driver.current_url.lower()}'

# SEARCH_INPUT = (By.NAME, 'q')
# SEARCH_SUBMIT = (By.NAME, 'btnK')
#
#
# @given('Open Google page')
# def open_google(context):
#     context.driver.get('https://www.google.com/')
#
#
# @when('Input {search_word} into search field')
# def input_search(context, search_word):
#     search = context.driver.find_element(*SEARCH_INPUT)
#     search.clear()
#     search.send_keys(search_word)
#     sleep(4)
#
#
# @when('Click on search icon')
# def click_search_icon(context):
#     context.driver.find_element(*SEARCH_SUBMIT).click()
#     sleep(1)
#
#
# @then('Product results for {search_word} are shown')
# def verify_found_results_text(context, search_word):
#     assert search_word.lower() in context.driver.current_url.lower(), \
#         f'Expected query not in {context.driver.current_url.lower()}'


# @given('Open Target Circle page')
# def open_target_circle(context):
#     context.driver.get('https://www.target.com/circle')
#
# @then('Verify {expected_amount} benefit cells')
# def verify_found_results_text(context, expected_amount):
#     links = context.driver.find_elements(By.CSS_SELECTOR, "[class*='fBbzFg']")
#     expected_amount = int(expected_amount)
#     assert len(links) == int(expected_amount), f'Expected {expected_amount} links but got {len(links)}'

# @given('Open Target main page')
# def open_target_circle(context):
#      context.driver.get('https://www.target.com/')
#
# @when('Search for {product}')
# def search_product(context, product):
#     # Search field => enter product
#     context.driver.find_element(By.ID, 'search').send_keys(product)
#     # Search button => click
#     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#     sleep(3)  # wait for search results page to load
#
#
# @when('Add {product} to cart')
# def add_product(context, product):
#     # Find and click the "Add to Cart" button (update selector as per page structure)
#     context.driver.find_element(By.XPATH, "//button[contains(@data-test, 'addToCart'])").click()
#     sleep(3)  # wait for the item to be added to the cart
#
#
# @then('Verify {product} in cart')
# def verify_results(context, product):
#     # Extract text from cart to verify product is added (update selector for the cart)
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, "[class='cart-class-name']").text
#     expected_result = product
#     assert expected_result in actual_result, f"Expected '{expected_result}', but got '{actual_result}'"


@given('Open Target product page')
def open_target_circle(context):
     context.driver.get('https://www.target.com/p/A-54551690')

@when('Search for {product}')
def search_product(context, product):
    # Search field => enter product
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # Search button => click
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(3)  # wait for search results page to load


@when('Add {product} to cart')
def add_product(context, product):
    # Find and click the "Add to Cart" button (update selector as per page structure)
    context.driver.find_element(By.XPATH, "//button[contains(@data-test, 'addToCart'])").click()
    sleep(3)  # wait for the item to be added to the cart


@then('Verify {product} in cart')
def verify_results(context, product):
    # Extract text from cart to verify product is added (update selector for the cart)
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[class='cart-class-name']").text
    expected_result = product
    assert expected_result in actual_result, f"Expected '{expected_result}', but got '{actual_result}'"