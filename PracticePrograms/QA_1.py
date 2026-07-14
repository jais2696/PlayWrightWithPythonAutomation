from playwright.sync_api import sync_playwright

# 1. Start the Playwright engine
with sync_playwright() as p:

    # 2. Launch a visible browser (headless=False means you can see it)
    browser = p.chromium.launch(headless=False)   #by default it was True, but to shwo the browser is open we have to make it Flase else it can't be visible to us but runs in the background.
    
    # 3. Open a new clean browser tab (Page)
    page = browser.new_page()

    # 4. Navigate to a website
    page.goto("https://www.google.com/")

    # 5. Take a picture to prove it worked
    page.screenshot(path=r"C:\Users\Jyoti Sharma\Pictures\Screenshots\example.png")

    # 6. Close the browser safely
    browser.close()
