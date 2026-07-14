from playwright.sync_api import Page, sync_playwright, expect, Page
import pytest


@pytest.fixture()
def navigateToAmazon(page: Page):
    page.goto("https://www.amazon.in/") 