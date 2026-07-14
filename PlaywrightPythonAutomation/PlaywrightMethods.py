from playwright.sync_api import sync_playwright, expect

# p = sync_playwright().start() # to start playwright engin
# page.wait_for_timout(10000)
# p.stop  to stop browser page.


#p = sync_playwright().start()
def browserLaunch():   #created function to use entire code for browser launch later
    with sync_playwright() as p: # this is used for open and stop the browser launch
        browser = p.chromium.launch(headless=False)
        # for launching browser
        context = browser.new_context() # context is browsers, to create multiple tabs in 1 browser need to create faces with context, here context we are opening 2 tabs and context 2 we have opening 1 tab
        context2 = browser.new_context()
        # for launching a tabs
        page = context.new_page()
        page2 = context2.new_page()
        page3 = context.new_page()
        page.wait_for_timeout(1000)
#browserLaunch()
# p.stop()




def pageNavigations():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.go_back()
        page.wait_for_timeout(3000) 
        page.go_forward()
        page.wait_for_timeout(3000)
        page.reload()
        page.wait_for_timeout(3000)
        print(page.title())
        print(page.url)
#pageNavigations()   


def locators1():  #get_by
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/") 
        #class, id, placeholder, maxlength, type
        page.get_by_placeholder("Enter Name").fill("Jyoti")
        page.get_by_placeholder("Enter EMail").fill("jyoti@gmail.com")
        page.wait_for_timeout(3000)
        
        ##get_by_placeholder
        ##get_by_label
        ##get_by_alt_text
        ##get_by_text
        ##get_by_test-id
        ##get_by_role
        ##get_by_title
#locators1()


def locators2(): #get_by_role
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/") 
        page.get_by_role("textbox", name = "Enter Phone").fill("1234567898")
        page.get_by_role("textbox", name = "Address:").fill("Noida UP 201301")
        #page.get_by_role("button",name="Submit").nth(0).click() we can use any nth index value if there is multiple values
        #page.get_by_role("radio", name = "Male").click()
        page.wait_for_timeout(3000)
#locators2()


def methods1(): #get_by_locators     xpath: relative/absolute/css
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/") 
        page.locator("#name").fill("jyoti")
        page.locator("#name").type("playwright")
        page.locator('[value="female"]').click()
        page.locator('[value="sunday"]').check()   #if we use click then it will click 2 times,,,,, check is use if there is unchecked item.
        page.locator('[value="sunday"]').uncheck()
        
        #Relative xpath:
        #1- //tagname[@attribute='value']                                    ex: //input[@id="Wikipedia1_wikipedia-search-input"]
        #2- //tagname[text()='value']                                        ex: //button[text() = 'Point M']
        #3- //tagname[contains(text(),'value')]                              ex://span[contains(text(),'Accounts & List')]
        #4- //tagname[contains(@attribute,'value')]                          ex://input[contains(@placeholder,"Enter")]
        #5- (//tagname[contains(@attribute,'value')])[1]                     ex:(//input[contains(@placeholder,"Enter")])[3]
        #6- //tagname[@attribute='value' and contains(text(),'value')]       ex: both should match values
        #7- //tagname[@attribute='value' or contains(),'value')]             ex: any one match
        #8- //*[@attribute='value']                                          ex: any node with any tags
        
        #absolute xpath:
        #child:               (//div[@class="form-group"])[1]/input[@id="name"]
        #grandchild:          //div[@id="HTML10"]//input[@id="field1"]            //is used for any location 
        #parent:              //input[@id="field2"]/parent::div                   (:: means going upward) going from child to parent
        #ancestor:            //input[@id="field2"]/ancestor::div[@id="HTML10"]
        #followingSibling:    //input[@id="field1"]/following-Sibling::input[1]
        #Preceding_Sibling:   //label[text()="Email:"]/preceding-sibling::input[1]
        
        #CSS:
        #id:     #value   or     tagname#value
        #class:  .value   or     tagname.value

        #1- #name  or input[#name]       #is uses for ID
        #2- .start  or button.start      .is uses for class
        #3- .sidebar.section             if there is space between 2 words then need to add . in between
        #4- parent  child
        #5- [attribute='value']

        #limitations: 
        #1- no text
        #2- contains
        #3- it only goes from parent to child but not child to parent
        #4- it only goes from ancestor to child but not child to ancestor
        #5- bottom to topis not supported
        #6- in css indexing not supports

        # child                 ex: .sidebar.section>#sWikipedia1                         >symbol using for immediate child
        # grandchild            ex: .sidebar.section .title                                add space for granchild ex before .title have space
        # followingSibling      ex: #Wikipedia1~#HTML11  or #Wikipedia1+#HTML5            ~ and +  uses to final all possible siblings

        page.wait_for_timeout(3000)
#methods1()      




def dropDown(): #select and options elements
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/") 
        page.locator("#country").select_option("india")         #dropdown
        #page.locator("#country").select_option(value="india")  #dropdown
        #page.locator("#country").select_option(label="India")  #dropdown
        #page.locator("#country").select_option(index=9)        #dropdown
        
        page.locator("#colors").select_option(["green","yellow"])  #if we need to select multiple values in dropdown then we cna pass it in list.
        #page.locator("#colors").select_option(index=[1,2])        #we can pass using index as well for multiple values selection

        page.wait_for_timeout(3000)
#dropDown()


def uploadFile():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")

        file1 = "C:\\Users\Jyoti Sharma\Pictures\Screenshots\Screenshot (1).png"
        file2 =  "PlaywrightPythonAutomation\locators.txt"
        page.locator("#multipleFilesInput").set_input_files(file1)
        page.locator("#multipleFilesInput").set_input_files([file1,file2])  #adding multiple files

        #page.locator("#singleFileInput").set_input_files("PlaywrightPythonAutomation\locators.txt")  #to upload files from our project

        #page.locator("#singleFileInput").set_input_files("C:\Users\Jyoti Sharma\Pictures\Screenshots\Screenshot (1).png") #to upload files from system folder
        #alway need to add \\ or single forward slash ()"C:Users/Jyoti Sharma/Pictures/Screenshots/Screenshot (1).png")
    
        page.wait_for_timeout(3000)
#uploadFile()



def getMethods():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        print(page.locator("button.start").text_content())
        print(page.locator("button.start").inner_text())
        print(page.locator("#name").input_value())       #if we have added something during inspect that value we can fetch/capture through input_value
        print(page.locator("#name").get_attribute("placeholder"))   #we can also fetch placeholder value by using get_attribute
#getMethods()




def table():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")

        #print(page.locator("//table[@name='BookTable']/tbody/tr[1]/td[1]").all_inner_texts())

        l1=[]  #create empty list to store table data
        for i in range(1,5): # it traverse 1 to 5 to store all values
            text = page.local_storage(f'//table[@name="BookTable"]/tbody/tr[2]/td[${i}]').text_contant()  #$ AND f is use for to convert to string.
            l1.append(text) #to print list data we use append
            page.wait_for_timeout(3000)

#table()

def mouseEvents():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.get_by_text("Poin Me").hover()
        page.locator('[ondblclick = "myFunction1()"]').dblclick()
        # page.locator('[ondblclick = "myFunction1()"]').click(click_count=3) #for multiple clicks
        # page.locator('[ondblclick = "myFunction1()"]').click(botton="right")
        page.locator("div#draggable").drag_to(page.locator("div#droppable"))
        #page.drag_and_drop("div#draggable","div#droppable")
        page.wait_for_timeout(4000)
#mouseEvents()


def keyBoardEvents():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.locator("#name").fill("Jyoti")
        page.keyboard.press("Control+A")
        page.keyboard.press("Control+C")
        page.keyboard.press("Tab")
        page.keyboard.press("Control+V")
        page.wait_for_timeout(4000)
#keyBoardEvents()


def Assertions():
      with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        actualTtile = page.title()
        actualUrl = page.url
        #assert actualTtile == "Automation Testing Practice"
        # expect(page).to_have_title("Automation Testing Practice", timeout=10000)
        # expect(page.locator("button.start")).to_be_visible(timeout=10000)
        expect(page.locator("button.start")).not_to_be_visible(timeout=10000)
#Assertions()


def autoWaits():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        page.locator("button.start123").click()   #default autowait is 30sec
#autoWaits()

def alerts():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")

        def handle(dialog):
            page.wait_for_timeout(2000)
            print(dialog.message)
            dialog.accept("Jyoti")   #this is promt alert where we have wright something then click on ok or cancle so we can add text and accept

            #dialog.accept()    #this is use to click ok or have only 1 option
            #dialog.dismiss()  #use this to accept or cancel alert
            
        #page.on("dialog", lambda dialog:dialog.accept("jyoti")) in place of def handle we can directly wright in this way

        page.on("dialog",handle)
        page.locator('[id="alertBtn"]').click()
        page.locator('[id="promptBtn"]').click()
        page.wait_for_timeout(2000)
#alerts()


def childTab():  #these were use for if when click on button or link and it opening new tab and have to type somethingin that
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        with page.expect_popup() as newChildPage:
            page.locator('[onclick="myFunction()"]').click()

        page2 = newChildPage.value
        page2.locator('(//input[@title="search"])[1]').fill("testing")
        page.wait_for_timeout(4000) 
childTab()   


    



