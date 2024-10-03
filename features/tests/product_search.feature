#Feature: Test Scenarios for Search functionality

#  Scenario: User can search for a product
#    Given Open Google page
#    When Input Car into search field
#    When Click on search icon
#    Then Product results for Car are shown

#  Scenario: open the Target Circle page
#    Given Open Target Circle page
#    Then Verify 10 benefit cells
#
Feature: Testing for the search product

  Scenario: User search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify that correct search results shown for coffee
    Then Verify product coffee in URL

  Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify that correct search results shown for tea

  Scenario Outline: User can search for product
    Given Open target main page
    When Search for <search_word>
    Then Verify that correct search results shown for <search_result>
    Examples:
    |search_word  |search_result |
    |coffee       |coffee        |
    |tea          |tea           |
    |mug          |mug           |
    |sugar        |sugar         |

  Scenario: User can add a product to cart
    Given Open target main page
    When Search for mug
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation

