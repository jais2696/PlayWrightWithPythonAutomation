from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page

# @pytest.fixture()
# def navigation(page):
#       page.goto("https://testautomationpractice.blogspot.com/")


@pytest.mark.smoke1
def test_Assertions(page):
        page.goto("https://testautomationpractice.blogspot.com/")
        actualTtile = page.title()
        actualUrl = page.url
        #assert actualTtile == "Automation Testing Practice"
        # expect(page).to_have_title("Automation Testing Practice", timeout=10000)
        # expect(page.locator("button.start")).to_be_visible(timeout=10000)
        expect(page.locator("button.start")).not_to_be_visible(timeout=10000)
#Assertions()


@pytest.mark.smoke1
def test_Assertions2(page):
        page.goto("https://testautomationpractice.blogspot.com/")
        actualTtile = page.title()
        actualUrl = page.url
        #assert actualTtile == "Automation Testing Practice"
        # expect(page).to_have_title("Automation Testing Practice", timeout=10000)
        # expect(page.locator("button.start")).to_be_visible(timeout=10000)
        expect(page.locator("button.start")).to_be_visible(timeout=10000)
#Assertions()


@pytest.mark.smoke1
def test_Assertions3(page):
        page.goto("https://testautomationpractice.blogspot.com/")
        actualTtile = page.title()
        actualUrl = page.url
        #assert actualTtile == "Automation Testing Practice"
        # expect(page).to_have_title("Automation Testing Practice", timeout=10000)
        # expect(page.locator("button.start")).to_be_visible(timeout=10000)
        expect(page.locator("button.start")).to_be_visible(timeout=10000)
#Assertions()