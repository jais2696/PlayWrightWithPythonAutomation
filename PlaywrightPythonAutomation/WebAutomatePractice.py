from playwright.sync_api import sync_playwright

def automate_practice_page():
    with sync_playwright() as p:
        # Launch browser (headless=False so you can watch it fill everything out)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        print("Navigating to target automation page...")
        page.goto("https://testautomationpractice.blogspot.com/")

        # 1. Text Fields (Name, Email, Phone, Address)
        # Using get_by_label() maps cleanly to the input field next to the text label.
        page.get_by_label("Name:").fill("John Doe")
        page.get_by_label("Email:").fill("johndoe@example.com")
        page.get_by_label("Phone:").fill("1234567890")
        page.get_by_label("Address:").fill("123 Main Street, New York")

        # 2. Radio Buttons (Gender)
        # Locates by explicit ARIA role and matches the visible button text.
        page.get_by_role("radio", name="Male").check()
        print("Selected Gender: Male")

        # 3. Checkboxes (Days of the week)
        # Easily toggle specific days by checking them explicitly.
        page.get_by_role("checkbox", name="Monday").check()
        page.get_by_role("checkbox", name="Sunday").check()
        print("Checked Days: Monday and Sunday")

        # 4. Dropdowns (Country selection)
        # select_option uses the visible text of the <select> tag options.
        country_dropdown = page.get_by_label("Country:")
        country_dropdown.select_option(label="India")
        print("Selected Country Dropdown: India")

        # 5. Multi-Select Dropdowns (Colors selection)
        # Pass a list of strings to select multiple options at the exact same time.
        colors_dropdown = page.get_by_label("Colors:")
        colors_dropdown.select_option(value=["red", "blue"])
        print("Selected Colors: Red and Blue")
        page.get_by_label("Animals:").select_option(value="cheetah")

        # ==========================================================
        #  DATE PICKERS
        # ==========================================================
        print("\n--- 3. Handling Date Pickers ---")
        # Basic Datepicker field (direct typing is usually fastest/easiest)
        page.locator("#datepicker").fill("12/25/2026")
        page.keyboard.press("Escape") # Close picker popup calendar

        # Inline Datepicker (clicking calendar elements directly)
        inline_calendar = page.locator("#inline_datepicker")
        inline_calendar.scroll_into_view_if_needed()
        # Click the next month button, then select day 15
        page.locator(".ui-datepicker-next").click()
        page.locator("a.ui-state-default", has_text="15").first.click()


        # ==========================================================
        # 4. TABLES (STATIC & DYNAMIC)
        # ==========================================================
        print("\n--- 4. Interacting with Tables ---")
        # Static Table: Select checkbox for "Learn Java" row
        java_row = page.locator("table[name='BookTable'] tr").filter(has_text="Learn Java")
        # (If a checkbox exists in that row, click it; otherwise we read its price text)
        print(f"Java Book Price: {java_row.locator('td').nth(3).inner_text()}")

        # Dynamic Table: Validate Chrome CPU check
        chrome_cpu = page.locator("#HTML9 table tr").filter(has_text="Chrome").locator("td").nth(4).inner_text()
        print(f"Dynamic Check -> Chrome CPU load: {chrome_cpu}")

        # Paginated Product Table: Loop through page 1 to 3
        for page_num in ["1", "2", "3"]:
            page.locator("#pagination li").filter(has_text=page_num).click()
            # Select the checkbox on the first item in the visible paginated row
            page.locator("#productTable tbody tr td input[type='checkbox']").first.check()

         # ==========================================================
        # 5. JAVASCRIPT DIALOGS & POPUPS
        # ==========================================================
        print("\n--- 5. Triggering Alerts, Confirmations, Prompts ---")
        # Simple Alert
        page.on("dialog", lambda d: d.accept())
        page.get_by_role("button", name="Simple Alert").click()

        # Confirmation Alert (Dismiss/Cancel it)
        page.on("dialog", lambda d: d.dismiss())
        page.get_by_role("button", name="Confirmation Alert").click()

        # Prompt Alert (Type input data)
        def handle_prompt(d):
            d.accept("Master Automator")
        page.on("dialog", handle_prompt)
        page.get_by_role("button", name="Prompt Alert").click()

        # ==========================================================
        # 6. INTERACTIVE ACTIONS (MOUSE & KEYBOARD)
        # ==========================================================
        print("\n--- 6. Running Drag & Drop, Sliders, and Double Clicks ---")
        # Copy Text (Double Click)
        page.get_by_role("button", name="Copy Text").dblclick()
        copied_val = page.locator("#field2").input_value()
        print(f"Double Click Verified! Field 2 value: {copied_val}")

        # Drag and Drop
        page.locator("#draggable").drag_to(page.locator("#droppable"))

        # Sliders (Focus and slide right using keyboard buttons)
        slider = page.locator(".ui-slider-handle").first
        slider.focus()
        for _ in range(15):
            page.keyboard.press("ArrowRight")

        # Mouse Hover Menus
        page.locator(".dropbtn", has_text="Hover me").hover()
        page.locator(".dropdown-content a", has_text="Laptops").click()

        # ==========================================================
        # 7. FILE UPLOADS & IFRAMES (BOTTOM SECTIONS)
        # ==========================================================
        print("\n--- 7. Handling File Uploads and Frames ---")
        # Single and Multiple File Upload
        # Creates a dummy file locally to upload
        with open("dummy_test.txt", "w") as f:
            f.write("Hello Automation World")
            
        page.locator("#singleFileInput").set_input_files("dummy_test.txt")
        # # Clean up local file after uploading
        # os.remove("dummy_test.txt")

        # Nested iFrames / Frames
        # Switch contexts inside the frame selector to type/click internally
        frame_element = page.frame_locator("#frame-one759")
        if frame_element:
            # Inside the iframe, target inputs
            frame_element.locator("#RESULT_TextField-0").fill("Frame Data Entry")

        # ==========================================================
        # 8. SCROLL AND CHECK FOOTER
        # ==========================================================
        print("\n--- 8. Scrolling to Footer Bottom ---")
        page.locator("footer, .footer-outer").last.scroll_into_view_if_needed()
        print("Reached page bottom successfully.")

        # Tear down
        page.wait_for_timeout(3000)
        #context.close()
        browser.close()
        print("\n🏆 Execution Complete! Every single item on the page was automated successfully.")


    automate_practice_page()  

