from playwright.sync_api import sync_playwright 
from database import section_data
import time 
import random 


def random_sleep(min_time=1, max_time=3): 
    time.sleep(random.uniform(min_time, max_time)) 
with sync_playwright() as p: 
    browser=p.chromium.launch( 
            headless=False, 
            args=[ "--disable-blink-features=AutomationControlled", "--disable-infobars", ] ) 
    context = browser.new_context( 
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36", 
            viewport={'width': 1920, 'height': 1080}, permissions=["geolocation", "notifications"] ) 
    page=context.new_page() 
    slow=random.randint(1,3)*100 
    page.goto('https://chelseafc.3ddigitalvenue.com/login') 
    page.wait_for_load_state("networkidle") 
    page.wait_for_selector("input#InAccountId") 
    page.type('input#InAccountId', 'lewisjohnson9877@outlook.com',delay=slow) 
    random_sleep(1, 2) 
    page.type('input#InPassword', 'Liverpoolfc123',delay=slow) 
    random_sleep(1, 2) 
    page.wait_for_selector('button[type=submit]') 
    page.click('button[type=submit]') 
    random_sleep(1, 2) 
    page.wait_for_load_state("networkidle") 
    page.wait_for_timeout(10000)
    page.wait_for_selector("//html/body/app-root/app-layout/div/div/div/app-buy-tickets/app-events/div/div[4]")
    paths = page.query_selector_all("//html/body/app-root/app-layout/div/div/div/app-buy-tickets/app-events/div/div[4]/div")
    length = len(paths) 
    print(f"Number of paths: {length}")

    for i in range(0,length):
        paths = page.query_selector_all(f"//div[@class='pb-container container']/div[4]/div[{i}]") 
        for path in paths: 
            page.wait_for_selector("//div[2]/div[4]/button") 
            availaibility=path.query_selector("//div[2]/div[4]/button")
            if (availaibility): 
                availaibility.click() 
                print("clicked availaibility") 
                page.wait_for_load_state("networkidle") 
                page.wait_for_timeout(10000)
                page.wait_for_timeout(2000) 
            else: 
                print("no availaibility") 
                page.wait_for_load_state("networkidle") 
                page.wait_for_timeout(10000) 
            page.wait_for_selector("//div[@class='pb-container container']/div[4]/div[2]") 
            btn=page.query_selector("//div[@class='pb-container container']/div[4]/div[2]") 
            if(btn): 
                btn.click() 
                print("Button Clicked") 
                page.wait_for_timeout(2000) 
            else: 
                print("Button not found") 
            page.wait_for_selector("//div[@class='bottom-interface']/button") 
            cont=page.query_selector("//div[@class='bottom-interface']/button") 
            if(cont): 
                cont.click()
                print("Continue Button Clicked") 
                page.wait_for_timeout(2000) 
            else: 
                print("Continue Button not found")
            rates=page.query_selector_all("//div[@class='pricescales-bar']/div")
            if rates:
                hm = len(rates)
                print(hm)
                for rate in rates:
                    section = rate.query_selector("//div/div/span").inner_text()
                    print(section)
                    price = rate.query_selector("//div[2]").inner_text()
                    print(price)
                    section_data(section,price)

            else:
                print("No Rates")
            # if(rates):
            #     hm=len(rates)
            #     print(hm)
            #     for rate in rates:
            #         for j in range(0,hm):
            #             page.query_selector(f"//div[@class='pricescales-bar']/div[{j}]")
            #             section=rate.query_selector("//div/div/span").inner_text()
            #             print(section)
            #             price=rate.query_selector("//div[2]").inner_text
            #             print(price)
            # else:
            #     print("No Rates")                  
            page.wait_for_selector("//a[@class='flex center menu-link active']")
            back=page.query_selector("//a[@class='flex center menu-link active']")


            if(back):
                back.click()
                print("Back Button Clicked")
                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(10000)

    context.close() 
    browser.close()   