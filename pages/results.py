from playwright.sync_api import sync_playwright, expect, Page

class results():
     def __init__(self, page: Page):
          self.resultsText = page.get_by_text("Results")
          self.page = page
          self.addToCart  = lambda product: page.locator(f'(//*[contains(@aria-label,"{product}")])[1]/ancestor::div[@class="a-section a-spacing-small a-spacing-top-small"]//button[@aria-label="Add to cart"]')
          # self.addToCart1Tb = page.locator('(//*[contains(@aria-label,"iPhone Air 1 TB")])[1]/ancestor::div[@class="a-section a-spacing-small a-spacing-top-small"]//button[@aria-label="Add to cart"])

     def validateVisibilityOfResultsText(self):
        expect(self.resultsText).to_be_visible()

     def clickOnAddToCart(self, product):
         print(self.addToCart(product).count)
         self.addToCart(product).click()

     # def addToCart(self, product):
     #     return self.page.locator(f'(//*[contains(@aria-label,"{product}")])[1]/ancestor::div[@class="a-section a-spacing-small a-spacing-top-small"]//button[@aria-label="Add to cart"]')
         