from playwright.sync_api import sync_playwright

#to start playwright engin
#p = sync_playwright().start()
with sync_playwright() as p:
      broswer = p.chromium.launch(headless=False)
#for launching a session
      context= broswer.new_context()

#for launching a tab 
      page = context.new_page() 
      page.wait_for_timeout(10000)
#p.stop()
#chromium launch
#session/context
#tab
