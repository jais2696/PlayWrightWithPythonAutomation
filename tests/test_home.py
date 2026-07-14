from playwright.sync_api import sync_playwright, expect, Page
import pytest

from pages.homePage import home


@pytest.mark.home
@pytest.mark.smoke
@pytest.mark.regression
#def test_validatingTheHomeScreenElement  #camel case formate name
def test_validating_the_home_screen_element(page:Page,navigateToAmazon):
    homePageObj = home(page)
    homePageObj.validateVisibilityOfSearchbar()
    homePageObj.validateVisibilityOfAccountsNdList()
    homePageObj.validateVisibilityOfMenuBar()