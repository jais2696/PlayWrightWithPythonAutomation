from playwright.sync_api import sync_playwright, expect, Page
import pytest

class home():

    def __init__(self, page:Page):
        self.searchBar = page.get_by_placeholder("Search Amazon.in")
        self.accountsNdList = page.get_by_text("Account & Lists")
        self.menuBtn = page.locator("#nav-hamburger-menu")
        self.searchBtn = page.locator("nav-search-submit-button")

    def validateVisibilityOfSearchbar(self):
        expect(self.searchBar).to_be_visible()    
        

    def validateVisibilityOfAccountsNdList(self):
        expect(self.accountsndList).to_be_visible()   

    def validateVisibilityOfMenuBar(self):
        expect(self.menuBtn).to_be_visible()         

    def enterSearchData(self, product):
        self.searchBar.fill(product)     

    def clickOnSearchBtn(self):
        self.searchBar.click()     