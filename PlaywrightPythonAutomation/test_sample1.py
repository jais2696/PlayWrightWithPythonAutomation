from playwright.sync_api import sync_playwright, expect
import pytest


def test_childTab():  #these were use for if when click on button or link and it opening new tab and have to type somethingin that
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        with page.expect_popup() as newChildPage:
            page.locator('[onclick="myFunction()"]').click()

        page2 = newChildPage.value
        page2.locator('(//input[@title="search"])[1]').fill("testing")
        page.wait_for_timeout(4000) 

@pytest.mark.smoke   
#@pytest.mark.sample1
@pytest.mark.skip  #it will skip the nearest one
def test_m1():
    a=[1,2]
     
    print("hello test case..")
