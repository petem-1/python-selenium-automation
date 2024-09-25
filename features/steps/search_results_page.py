# from selenium.webdriver.common.by import By
# from behave import given, when, then
# from time import sleep
#
# ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
# ADD_TO_CART_BTN_SIDE_NAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
# SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
#
# LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
# PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
# PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
#
# # @given('Open Target main page')
# # def open_target_circle(context):
# #     #context.driver.get('https://www.target.com/')
# #     context.app.main_page.open_main()
#
#
# # @when('Click on Add to Cart button')
# # def side_nav_click_add_to_cart(context):
# # @when('Search for a {product}')
# # def search_product(context, product):
# #     # Search field => enter tea
# #     context.driver.find_element(By.ID, 'search').send_keys('tea')
# #     # # Search button => click
# #     context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
# #     sleep(5)  # wait for search results page to load
# #     context.app.header.search_product(product)
#
# # @then('Verify that correct search results shown for {product}')
# # def verify_results(context, product):
# #     # actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
# #     # assert product in actual_result, f'Expected {product}, got actual {actual_result}'
# #     context.app.search_results_page.verify_results(product)
# #
# # @then('Verify that every product has a name and an image')
# # def verify_products_name_img(context):
# #     # To see ALL listings (comment out if you only check top ones):
# #     context.driver.execute_script("window.scrollBy(0,2000)", "")
# #     sleep(4)
# #     context.driver.execute_script("window.scrollBy(0,2000)", "")
# #
# #     all_products = context.driver.find_elements(*LISTINGS)  # [WebEl1, WebEl2, WebEl3, WebEl4]