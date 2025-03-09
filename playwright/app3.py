import asyncio
from playwright.async_api import async_playwright
from database import section_data
import time
import random

def random_sleep(min_time=1, max_time=3):
    time.sleep(random.uniform(min_time, max_time))

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-infobars",
                "--disable-http2",
                "--ignore-certificate-errors",
                "--no-sandbox",
                "--disable-dev-shm-usage",
            ]
        )

        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            extra_http_headers={
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
            },
            viewport={'width': 1920, 'height': 1080},
            permissions=["geolocation", "notifications"],
            # ignoreHTTPSErrors= True,
            # acceptDownloads= True,
        )

        await context.set_offline(False)
        await context.route("**/*", lambda route, request: route.continue_())

        page = await context.new_page()
        slow = random.randint(1, 3) * 100

        try:
            await page.goto('https://chelseafc.3ddigitalvenue.com/login', wait_until='load', timeout=180000)
            await page.wait_for_load_state("domcontentloaded")
            await page.mouse.move(100, 100)
            await page.mouse.click(100, 100)
            await page.wait_for_selector("input#InAccountId", timeout=60000)
            await page.type('input#InAccountId', 'lewisjohnson9877@outlook.com', delay=slow)
            random_sleep(1, 2)
            await page.type('input#InPassword', 'Liverpoolfc123', delay=slow)
            random_sleep(1, 2)
            await page.wait_for_selector('button[type=submit]', timeout=60000)
            await page.click('button[type=submit]')
            random_sleep(1, 2)
            await page.wait_for_load_state("networkidle")
            await page.wait_for_timeout(10000)
            await page.wait_for_selector("//html/body/app-root/app-layout/div/div/div/app-buy-tickets/app-events/div/div[4]")
            paths = await page.query_selector_all("//html/body/app-root/app-layout/div/div/div/app-buy-tickets/app-events/div/div[4]/div")
            length = len(paths)
            print(f"Number of paths: {length}")

            for i in range(0, length):
                paths = await page.query_selector_all(f"//div[@class='pb-container container']/div[4]/div[{i}]")
                for path in paths:
                    await page.wait_for_selector("//div[2]/div[4]/button")
                    availability = await path.query_selector("//div[2]/div[4]/button")
                    if availability:
                        await availability.click()
                        print("clicked availability")
                        await page.wait_for_load_state("networkidle")
                        await page.wait_for_timeout(10000)
                        await page.wait_for_timeout(2000)
                        await page.mouse.click(100, 100)
                    else:
                        print("no availability")
                        await page.wait_for_load_state("networkidle")
                        await page.wait_for_timeout(10000)
                    await page.wait_for_selector("//div[@class='pb-container container']/div[4]/div[2]")
                    btn = await page.query_selector("//div[@class='pb-container container']/div[4]/div[2]")
                    if btn:
                        await btn.click()
                        print("Button Clicked")
                        await page.wait_for_timeout(2000)
                    else:
                        print("Button not found")
                    await page.wait_for_selector("//div[@class='bottom-interface']/button")
                    cont = await page.query_selector("//div[@class='bottom-interface']/button")
                    if cont:
                        await cont.click()
                        print("Continue Button Clicked")
                        await page.wait_for_timeout(2000)
                    else:
                        print("Continue Button not found")
                    rates = await page.query_selector_all("//div[@class='pricescales-bar']/div")
                    if rates:
                        hm = len(rates)
                        print(hm)
                        for rate in rates:
                            section = await rate.query_selector("//div/div/span").inner_text()
                            print(section)
                            price = await rate.query_selector("//div[2]").inner_text()
                            print(price)
                            section_data(section, price)
                    else:
                        print("No Rates")
                    await page.wait_for_selector("//a[@class='flex center menu-link active']")
                    back = await page.query_selector("//a[@class='flex center menu-link active']")
                    if back:
                        await back.click()
                        print("Back Button Clicked")
                        await page.wait_for_load_state("networkidle")
                        await page.wait_for_timeout(10000)

        except Exception as e:
            print(f"An error occurred: {e}")
        
        await context.close()
        await browser.close()

# Run the main function
asyncio.run(main())



