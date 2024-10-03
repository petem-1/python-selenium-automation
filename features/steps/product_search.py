from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# Target Test Case: Searching for a Product

@given('Open Target main page')
def open_target_main_page(context):
    #context.driver.get('https://www.target.com/')
    context.app.main_page.open_main()

@when('Search for {product}')
def search_product(context, product):
    # Search field => enter tea
    # context.driver.find_element(By.ID, 'search').send_keys('tea')
    # # Search button => click
    # context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # context.app.header.search_product(product)
    context.app.header.search_product('tea')
    sleep(5)  # wait for search results page to load


@then('Verify that correct search results shown for tea')
def verify_results(context):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    expected_result = 'tea'
    assert expected_result in actual_result, f'Expected {expected_result}, got actual {actual_result}'

# @then('Verify that correct search results are shown for {product} on Target')
# def verify_target_search_results(context, product):
#     """Verify that the correct product results are shown after a search on Target."""
#     actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
#     assert product.lower() in actual_result.lower(), f"Expected {product} in results, found {actual_result}"


# # ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
# # ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
# # SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
# #
# # LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
# # PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
# # PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
#
# @when('Search for a {product}')
# def search_product(context, product):
#     context.app.header.search_product('tea')
#     sleep(5)  # wait for search results page to load
#
# @then('Verify that correct search results shown for {product}')
# def verify_results(context, product):
#     context.app.search_results_page.verify_results(product)
#
#
# @then('Verify that every product has a name and an image')
# def verify_products_name_img(context):
#     # To see ALL listings (comment out if you only check top ones):
#     context.driver.execute_script("window.scrollBy(0,2000)", "")
#     sleep(4)
#     context.driver.execute_script("window.scrollBy(0,2000)", "")
#
#
# # @then('Product results for {search_word} are shown')
# # def verify_found_results_text(context, search_word):
# #     assert search_word.lower() in context.driver.current_url.lower(), \
# #         f'Expected query not in {context.driver.current_url.lower()}'
#
# # SEARCH_INPUT = (By.NAME, 'q')
# # SEARCH_SUBMIT = (By.NAME, 'btnK')
# #
# #
# # @given('Open Google page')
# # def open_google(context):
# #     context.driver.get('https://www.google.com/')
# #
# #
# # @when('Input {search_word} into search field')
# # def input_search(context, search_word):
# #     search = context.driver.find_element(*SEARCH_INPUT)
# #     search.clear()
# #     search.send_keys(search_word)
# #     sleep(4)
# #
# #
# # @when('Click on search icon')
# # def click_search_icon(context):
# #     context.driver.find_element(*SEARCH_SUBMIT).click()
# #     sleep(1)
# #
# #
# # @then('Product results for {search_word} are shown')
# # def verify_found_results_text(context, search_word):
# #     assert search_word.lower() in context.driver.current_url.lower(), \
# #         f'Expected query not in {context.driver.current_url.lower()}'
#
#
# # @given('Open Target Circle page')
# # def open_target_circle(context):
# #     context.driver.get('https://www.target.com/circle')
# #
# # @then('Verify {expected_amount} benefit cells')
# # def verify_found_results_text(context, expected_amount):
# #     links = context.driver.find_elements(By.CSS_SELECTOR, "[class*='fBbzFg']")
# #     expected_amount = int(expected_amount)
# #     assert len(links) == int(expected_amount), f'Expected {expected_amount} links but got {len(links)}'
# #
# # @when('Search for {product}')
# # def search_product(context, product):
# #     # Search field => enter product
# #     context.driver.find_element(By.ID, 'search').send_keys(product)
# #     # Search button => click
# #     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
# #     sleep(3)  # wait for search results page to load
# #
# #
# # @when('Add {product} to cart')
# # def add_product(context, product):
# #     # Find and click the "Add to Cart" button (update selector as per page structure)
# #     context.driver.find_element(By.XPATH, "//button[contains(@data-test, 'addToCart'])").click()
# #     sleep(3)  # wait for the item to be added to the cart
# #
# #
# # @then('Verify {product} in cart')
# # def verify_results(context, product):
# #     # Extract text from cart to verify product is added (update selector for the cart)
# #     actual_result = context.driver.find_element(By.CSS_SELECTOR, "[class='cart-class-name']").text
# #     expected_result = product
# #     assert expected_result in actual_result, f"Expected '{expected_result}', but got '{actual_result}'"
#
#
# @given('Open Target product page')
# def open_target_circle(context):
#      context.driver.get('https://www.target.com/p/A-54551690')
#
# @when('Search for {product}')
# def search_product(context, product):
#     # Search field => enter product
#     context.driver.find_element(By.ID, 'search').send_keys(product)
#     # Search button => click
#     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
#     sleep(3)  # wait for search results page to load
#
# # @when('Click on Add to Cart button')
# # def side_nav_click_add_to_cart(context):
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