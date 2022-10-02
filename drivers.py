from pathlib import Path
from constants import FIREFOX_DRIVER_LINUX
from constants import FIREFOX_DRIVER_WINDOWS
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# Errors
class NotSupportedSO(Exception):...


class BrowserFirefox():
    """
    
    """

    def __init__(self, firefox_driver_so:str = "win", headless:bool = True):
        # Local Variables
        self.firefox_driver_path:Path
        
        # Setting Options
        self.firefox_options = Options()
        if headless: self.firefox_options.headless = True # Headless Mode
        self.firefox_options.add_argument("--window-size=1366x768") # Window Size
        self.firefox_options.add_argument("--disable-gpu") # Disable GPU
        self.firefox_options.add_argument("--disable-extensions") # Disable Extensions        

        # Firefox Driver
        match firefox_driver_so:
            case "win":
                self.firefox_driver = Service(FIREFOX_DRIVER_WINDOWS.__str__())
                # Driver Path
                self.firefox_driver_path = FIREFOX_DRIVER_WINDOWS
            case "linux":
                self.firefox_driver = Service(FIREFOX_DRIVER_LINUX.__str__())
                # Driver Path
                self.firefox_driver_path = FIREFOX_DRIVER_LINUX
            case _:
                raise NotSupportedSO(f"SO not supported: {firefox_driver_so}")

        # Driver
        self.driver = webdriver.Firefox(service=self.firefox_driver, options=self.firefox_options)

    def __str__(self) -> str:
        return f"{self.firefox_driver_path}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}({self.firefox_driver_path})>"

# TODO: Add Chrome Functionality
class BrowserChrome(): ...

# TODO: Add Edge Functionality
class BrowserEdge(): ...


if __name__ == "__main__":
    driver = BrowserFirefox()
    driver.driver.get("https://www.google.com")
    print(driver.driver.title)