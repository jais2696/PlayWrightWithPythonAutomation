from playwright.sync_api import sync_playwright, expect, Page
import pytest

from pages.homePage import home
from pages.loginPage import loginPage


@pytest.mark.login
def test_positiveLogin(page,navigateToAmazon):
    homePageObj = home(page)
    loginPageObj = loginPage(page)

    homePageObj.clickOnAccountsndList()
    loginPageObj.enterEmailValue("trainingplaywright@gmail.com")
    loginPageObj.clickOnContinueBtn()
    loginPageObj.enterPw("Welcome@04")
    loginPageObj.clickOnContinueBtn()
    homePageObj.validateVisibilityOfSearchBox()