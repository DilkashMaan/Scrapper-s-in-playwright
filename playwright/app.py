from playwright.sync_api import sync_playwright
from database import event_data
import time
import random


def random_sleep(min_time=1, max_time=3):
    time.sleep(random.uniform(min_time, max_time))


with sync_playwright() as p:
  
    browser = p.chromium.launch(
        headless=False, 
        args=[
            "--disable-blink-features=AutomationControlled",  
            "--disable-infobars",  
        ]
    )

   
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",  
        viewport={'width': 1920, 'height': 1080},  
        permissions=["geolocation", "notifications"]
    )

    page = context.new_page()
    slow=random.randint(1,3)*100
    
  
    page.goto('https://chelseafc.3ddigitalvenue.com/login')
    page.wait_for_load_state("networkidle")
    page.wait_for_selector('input#InAccountId')
    page.type('input#InAccountId', 'lewisjohnson9877@outlook.com',delay=slow)
    random_sleep(1, 2)
    

    page.type('input#InPassword', 'Liverpoolfc123',delay=slow)
    random_sleep(1, 2)

 
    page.wait_for_selector('button[type=submit]')
    page.click('button[type=submit]')
    random_sleep(1, 2)

    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(10000)
    paths = page.query_selector_all("//div[@class='pb-container container']/div[4]/div")
   
    
    
    for path in paths:
        # EventName = path.query_selector("//div[2]/div[1]/span[1]").inner_text()
        # page.wait_for_timeout(2000)
        
        # Venue=path.query_selector("//div[2]/div[2]/span[1]").inner_text()
        # page.wait_for_timeout(2000)
        
        # date=path.query_selector("//div[2]/div[3]/span[1]").inner_text()
        # page.wait_for_timeout(2000)
        page.wait_for_selector('//div[2]/div[4]/button')
        Avialability=path.query_selector("//div[2]/div[4]/button")
        if Avialability:
            Avialability.click()
            page.wait_for_timeout(2000)
        else:
            print("No tickets available1")

        page.wait_for_selector("//div[@class='list-element-container rounded-block'][2]")
        newbtn=page.query_selector("//div[@class='list-element-container rounded-block'][2]")
        if newbtn:
            newbtn.click()
        else:
            print("No tickets available2")
            page.wait_for_timeout(1000)

        cont=page.query_selector("//div[@class='bottom-interface']/button")
        if cont:
            cont.click()
        else:
            print("No tickets available3")
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1000)
        
        page.wait_for_selector("//div[@class='pricescale-element rounded-block mb16']/div/div/span[1]")
        section=page.query_selector("//div[@class='pricescale-element rounded-block mb16']/div/div/span[1]").inner_text()
        if section:
            print(section)
            page.wait_for_timeout(2000)
        page.wait_for_selector("//div[@class='pricescale-element rounded-block mb16']/div[2]")
        
        price=page.query_selector("//div[@class='pricescale-element rounded-block mb16']/div[2]").inner_text()
        if price:
            print(price)
        else:
            print("No price available")
            page.wait_for_timeout(2000)
        page.wait_for_selector("//div[@class='pricescale-element rounded-block mb16']/div/div[2]/span[1]")
        section2=page.query_selector("//div[@class='pricescale-element rounded-block mb16'][2]/div/div/span").inner_text()
        if section2:
            print(section2)
        else:
            print("No section2 available")
            page.wait_for_timeout(2000)



        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1000)
       
        page.wait_for_selector("//div[@class='content-subinfo font-size-14']")
        price2=page.query_selector("//div[@class='content-subinfo font-size-14']").inner_text()
        if price2:
            print(price2)
            page.wait_for_timeout(2000)
        else:
            print("No price2 available")

        page.wait_for_selector("//a[@class='flex center menu-link active']")
        back=page.query_selector("//a[@class='flex center menu-link active']")
        back.click()
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1000)        

        # page.wait_for_timeout(2000)
        # print(Avialability)
        
        # info=path.query_selector("//div[3]/div[2]")
        # page.wait_for_timeout(2000)
        # event_data(EventName,Venue,date,Avialability,info)
        # matches.append({
        #     "Event Name":EventName,
        #     "Venue":Venue,
        #     "Date":date,
        #     "Availability":Avialability,
        #     "Information":info})
    # print(matches)
    # print("Data Saved Successfully")
    browser.close()

sync_playwright()


# from playwright.sync_api import sync_playwright
# import time
# import random

# def random_sleep(min_time=1, max_time=3):
#     time.sleep(random.uniform(min_time, max_time))

# with sync_playwright() as  p:
#     browser = p.chromium.launch(
#         headless=False, 
#         args=[
#             "--disable-blink-features=AutomationControlled",  
#             "--disable-infobars",  
#         ]
#     )
#     context = browser.new_context(
#         user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",  
#         viewport={'width': 1920, 'height': 1080},  
#         permissions=["geolocation", "notifications"]
#     )
#     page = context.new_page()

#     page.goto('https://www.website.com/sign-in/?source=SC&country=IN')
    
#     slow=random.randint(1,3)*100

#     page.wait_for_selector('input#username')
#     page.type('input#username','demo17',delay=slow)
#     random_sleep(1,2)
  

#     page.wait_for_selector('input#password')
#     page.type('input#password','Deadlydemo7')
#     random_sleep(1,3)


#     page.wait_for_timeout(4000)
#     button=page.query_selector('//*[@id="recaptcha-anchor"]')
#     button.click()

#     page.wait_for_selector('button#signin-submit2')
#     page.click('button#signin-submit2')
#     random_sleep(1,2)

#     context.close() 
#     browser.close()
