from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Go to a dummy practice login page
    page.goto("https://testautomationpractice.blogspot.com/")
    
    
    # Finds a main heading (<h1>, <h2>) that says "Welcome Back"
    #page.get_by_role("heading", name="Welcome Back").is_visible()

    page.get_by_role("textbox",name ="Enter Name").fill("Jyoti Sharma")
    #page.get_by_role("textbox",name ="Last Name").fill("Sharma")
    page.get_by_placeholder("Enter EMail").fill("jyoti123@gmail.com")

    # 1. Select the radio button
    #page.get_by_label("Female").check()
    # 2. Assert/Verify that it is actually selected
    #expect(page.get_by_label("Female")).to_be_checked()

    page.locator("//*[@id='phone']").fill("8329564699")
    page.locator("//*[@id='textarea']").fill("Noida, 201301, UP")
    page.get_by_role("radio",name = "Female").check()
    page.locator("//*[@id='sunday']").check()
    page.locator("//*[@id='country']/option[10]").select_option("India")


    # Wait 3 seconds so we can see the result before closing
    page.wait_for_timeout(5000)
    browser.close()