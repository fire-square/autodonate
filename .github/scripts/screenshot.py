"""Script for generating screenshots of the main page in ``.github/workflows/screenshot.yml``."""

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main() -> None:
    """Main function of the script."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("http://localhost:8000/")
    driver.set_window_size(1920, 1080)
    sleep(10)
    driver.save_screenshot("screen.png")
    driver.close()


if __name__ == "__main__":
    main()
