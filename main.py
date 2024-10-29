from playwright.async_api import async_playwright
import time



class ChatGpt:
    
    def __init__(self) -> None:
        

        self.url =  "https://chatgpt.com"

        self.sleep =  6


    async def get_response(self, payload  :  str ):
        args = []
        
        # disable navigator.webdriver:true flag
        args.append("--disable-blink-features=AutomationControlled")

        playwright = await async_playwright().start()
        browser = await playwright.chromium.launch(headless=False,
                                                args=args)
        page = await browser.new_page()
        await page.goto("https://chatgpt.com")

        await page.wait_for_selector("textarea#prompt-textarea")
        await page.fill("textarea#prompt-textarea", payload)

        await page.wait_for_selector('button[data-testid="send-button"]')
        await page.click('button[data-testid="send-button"]')


        await page.wait_for_selector("code.hljs.language-json")

        time.sleep(self.sleep)
        
        div_text = await page.text_content("code.hljs.language-json")
        await browser.close()
        await playwright.stop()
        return div_text


if __name__ == "__main__":
    app =  ChatGpt()
    text  =  input("search text")
    print(app.get_response(text))
