import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class SeleniumEnvironment:
    def __init__(self, headless=True):
        self.driver = None
        self.headless = headless

    def setup_driver(self):
        """Setup Chrome WebDriver with optional headless mode."""
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless")  # Run in headless mode
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")

        # Install ChromeDriver using ChromeDriverManager and explicitly specify the correct binary
        chromedriver_path = ChromeDriverManager().install()
        actual_chromedriver_binary = os.path.join(os.path.dirname(chromedriver_path), "chromedriver")

        self.driver = webdriver.Chrome(service=Service(actual_chromedriver_binary), options=chrome_options)

    def quit_driver(self):
        """Quit and close the WebDriver."""
        if self.driver:
            self.driver.quit()

    def run_test(self, url):
        """Navigate to a URL and return the page title."""
        if not self.driver:
            raise Exception("Driver not initialized. Call setup_driver() first.")
        self.driver.get(url)
        return self.driver.title

if __name__ == "__main__":
    selenium_env = SeleniumEnvironment(headless=True)  # Set up headless mode for GitHub Codespaces
    selenium_env.setup_driver()
    
    try:
        title = selenium_env.run_test("https://www.python.org")
        print(f"Page title: {title}")
    finally:
        selenium_env.quit_driver()  # Always ensure the driver is closed

