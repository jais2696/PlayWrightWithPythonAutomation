from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser1 = p.firefox.launch(headless=False)
    browser2 = p.firefox.launch(headless=False)
    browser3 = p.webkit.launch(headless=False)

    page1 = browser1.new_page()
    page2 = browser2.new_page()
    page3 = browser3.new_page()

    page1.goto("https://www.google.com/")
    page2.goto("https://www.gmail.com/")
    page3.goto("https://facebook.com/")

    page1.screenshot(path=r"C:\Users\Jyoti Sharma\Pictures\Screenshots\example1.png")
    page2.screenshot(path=r"C:\Users\Jyoti Sharma\Pictures\Screenshots\example2.png")
    page3.screenshot(path=r"C:\Users\Jyoti Sharma\Pictures\Screenshots\example3.png")

browser1,browser2,browser3.close()


    