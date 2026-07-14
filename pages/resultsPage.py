from playwright.sync_api import sync_playwright, expect, Page

class results():
    def __init__(self, page: Page):
        self.resultsText = page.get_by_text("Results")

    def validateVisibilityOfResultsText(self):
        expect(self.resultsText).to_be_visible()    
    