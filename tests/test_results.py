from playwright.sync_api import sync_playwright, expect, Page
import pytest

from pages.homePage import home
from pages.results import results

@pytest.mark.results
@pytest.mark.smoke
@pytest.mark.regression
def test_validate_the_navigation_to_results_page(page:Page,navigateToAmazon):
    homePageObj = home(page)
    resultsPageObj = results(page)
    homePageObj.enterSearchData("iphone")
    homePageObj.clickOnsearchBtn()    
    resultsPageObj.validateVisibilityOfResultsText()

@pytest.mark.regression1
def test_validate_the_add_to_cart(page:Page,navigateToAmazon):
    homePageObj = home(page)
    resultsPageObj = results(page)
    homePageObj.enterSearchData("iphone 17 pro")
    homePageObj.clickOnsearchBtn()    
    page.wait_for_timeout(5000)
    resultsPageObj.clickOnAddToCart("iPhone Air 1 TB")
    
    # resultsPageObj.clickOnAddToCart("iPhone Air 256 GB")
    page.wait_for_timeout(5000)