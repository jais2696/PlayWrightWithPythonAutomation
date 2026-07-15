from playwright.sync_api import sync_playwright, expect, Page

class home():
    
    def __init__(self, page: Page):
        self.searchBar = page.get_by_placeholder("Search Amazon.in")
        self.accountsndList = page.get_by_text("Account & Lists")
        self.menuBtn = page.locator("#nav-hamburger-menu")
        self.searchBtn = page.locator("#nav-search-submit-button")
        self.searchBox = page.locator("input#twotabsearchtextbox")
        self.menuIcon = page.get_by_label("Open All Categories Menu")
        self.accountsndList = page.locator("//span[contains(text(),'Account & Lists')]")

    def validateVisibilityOfSearchbar(self):
        expect(self.searchBar).to_be_visible()

    def validateVisibilityOfAccountsNdList(self):
        expect(self.accountsndList).to_be_visible()

    def validateVisibilityOfMenuBar(self):
        expect(self.menuBtn).to_be_visible()

    def enterSearchData(self, product):
        self.searchBar.fill(product)
    
    def clickOnsearchBtn(self):
        self.searchBtn.click()
    
    def waitingForSearchBoxToBeVisible(self):
        self.searchBox.wait_for(state="visible", timeout=50000)
    
    def validateVisibilityOfSeachBox(self):
         expect(self.searchBox).to_be_visible()
    
    def verifyTitle(self):
        expect(self.page).to_have_title("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
    
    def validateThevisibityOfMenu(self):
        expect(self.menuIcon).to_be_visible()
    
    def clickOnAccountsndList(self):
        self.accountsndList.click()
    
    def enterSearchText(self, text):
        self.searchBox.fill(text)

    def clickOnSearchBtn(self):
        self.searchBox.press("Enter")