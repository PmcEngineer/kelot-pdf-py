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
            chrome_options.add_argument("--headless")  # Run browser in headless mode (without GUI)
            chrome_options.add_argument("--disable-gpu")  # For systems without GPU
            chrome_options.add_argument("--no-sandbox")  # Required for running as root on some systems
            chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
            chrome_options = Options()

            chrome_options.binary_location = "/usr/bin/google-chrome"  # Specify Chrome binary location

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        chrome_options.add_argument("--remote-debugging-port=9222")  # For debugging purposes

        # Automatically download and set up the correct ChromeDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

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
    # Example usage
    selenium_env = SeleniumEnvironment(headless=True)  # Set up headless mode for GitHub Codespaces
    selenium_env.setup_driver()
    
    try:
        title = selenium_env.run_test("https://www.python.org")
        print(f"Page title: {title}")
    finally:
        selenium_env.quit_driver()  # Always ensure the driver is closed
