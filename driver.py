from pathlib import Path
from constants import CHROME_DRIVER
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class BrowserChrome():

    def __init__(self, chrome_driver:str = CHROME_DRIVER.__str__(), headless:bool = True):

        # Setting Options
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--window-size=1920x1080")
        # Driver Path
        self.chrome_driver_path = chrome_driver
        # Chrome Driver
        self.chrome_driver = Service(chrome_driver)

        # Driver
        self.driver = webdriver.Chrome(service=self.chrome_driver, options=self.chrome_options)

    def __str__(self) -> str:
        return f"Path Driver: {self.chrome_driver_path}"

    def __repr__(self) -> str:
        return f""

if __name__ == "__main__":
    brow = BrowserChrome()
    print(type(brow))
    