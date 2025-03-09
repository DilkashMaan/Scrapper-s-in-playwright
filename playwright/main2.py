from playwright.sync_api import sync_playwright 
from database import section_data
import time 
import random 

with sync_playwright() as p:
    browser=p.chromium.launch(
        headless=True,
         args=[ "--disable-blink-features=AutomationControlled", "--disable-infobars", ] )
    
    context=browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36", 
            viewport={'width': 1920, 'height': 1080}, permissions=["geolocation", "notifications"] 
    )

    page=context.new_page()

    page.goto("https://amptickets.com/calendar")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(60000)
    concerts=page.query_selector_all("//div[@class='mt-[10px] px-5 pb-16 lg:mt-[20px] lg:px-5 xl:px-[80px]']/div[@class='px-0 pt-5 pb-5 lg:pt-6 lg:pb-7']")
    length=len(concerts)
    print(length)
    for i in range(0, length):
        concerts = page.query_selector_all(f"//div[@class='mt-[10px] px-5 pb-16 lg:mt-[20px] lg:px-5 xl:px-[80px]']/div[@class='px-0 pt-5 pb-5 lg:pt-6 lg:pb-7'][{i}]")

        for concert in concerts:
            concert_name=concert.query_selector("//div/div[2]/div/div/div[1]").inner_text()
            print(concert_name)
            concert_date=concert.query_selector("//div/div[2]/div/div/div[3]/div").inner_text()
            print(concert_date)
            buy_ticketsbtn=concert.query_selector("//a[@class='w-full border-0 border-solid no-underline']")
            if buy_ticketsbtn:
                buy_ticketsbtn.click()
                print("buytickets button pressed")
                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(60000)
            else:
                print("No buy tickets button found")
            buybtn=page.query_selector("//button[@id='btn_pdp_buy_tickets']")  
            if buybtn:
                buybtn.click()
                print("buybtn pressed")
                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(60000)
            else:
                print("No buy button found")
            page.wait_for_selector("//div[@id='headlessui-tabs-panel-:r6:']/div")
            tickets=page.query_selector_all("//div[@id='headlessui-tabs-panel-:r6:']/div")
            lengtht=len(tickets)
            print(lengtht)
            for ticket in tickets:
                ticket_name=ticket.query_selector("//div/div/span").inner_text()
                print(ticket_name)
                ticket_price=ticket.query_selector("//p").inner_text()
                print(ticket_price)
            backbtn=page.query_selector("//a[@class='flex items-center']")
            if backbtn:
                backbtn.click()
                print("back button pressed")
                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(60000)
            else:
                print("No back button found")

            homebtn=page.query_selector("//a[@class='mantine-1iqrsug mantine-Breadcrumbs-breadcrumb text-xs  md:text-sm text-primary-500'][2]")
            if homebtn:
                homebtn.click()
                print("home button pressed")
                page.wait_for_load_state("networkidle")
                page.wait_for_timeout(60000)
            else:
                print("No Home button")

    context.close()
    browser.close()