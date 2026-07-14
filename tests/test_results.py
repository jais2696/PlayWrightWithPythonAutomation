from playwright.sync_api import sync_playwright, expect, Page
import pytest

from pages.homePage import home
from pages.resultsPage import results


@pytest.mark.results
@pytest.mark.smoke
@pytest.mark.regression
def test_validate_the_navigation_to_results_page(page:Page,navigateToAmazon):
    homePageObj = home(page)
    resultsPageObj = results(page)
    homePageObj.enterSearchData("iphone")
    homePageObj.clickOnSearchBtn()
    resultsPageObj.validateVisibilityOfResultsText()