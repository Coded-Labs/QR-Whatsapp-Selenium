from constants import BASE_DIR
from drivers import BrowserFirefox
from drivers import BrowserChrome
from drivers import BrowserEdge
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC

# Errors
class NotSupportedBrowser(Exception): ...


# Funcionality
def driver_init(browser_web:str = "firefox") -> WebDriver:
    
    # Local Variables
    browser: BrowserFirefox | BrowserChrome | BrowserEdge
    
    match browser_web:
        
        case "firefox":
            browser = BrowserFirefox()
        case "chrome":
            browser = BrowserChrome()
        case "edge":
            browser = BrowserEdge()
        case _:
            raise NotSupportedBrowser(f"Browser not supported: {browser_web}")
            
    driver = browser.driver
    return driver


if __name__ == "__main__":
    
    def get_qr_whatsapp():
        driver = driver_init()
        driver.get("https://web.whatsapp.com")
        
        try:
            canvas = WebDriverWait(driver, 60).until( #* Wait for an element inside the DOM
                EC.presence_of_element_located((By.TAG_NAME, "canvas"))
            )
            
            qr_code = WebDriverWait(driver, 60).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/div[1]/div/div[2]/div'))
            )
            
            print(qr_code.get_attribute("data-ref"))
        except Exception as e:
            raise e
        
        driver.get_full_page_screenshot_as_file((BASE_DIR/"qr.png").__str__())
        
    get_qr_whatsapp()