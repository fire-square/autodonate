"""Script for generating screenshots of the main page in ``.github/workflows/screenshot.yml``."""

from sys import argv
from time import sleep
from random import randint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main() -> None:
    """Main function of the script."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("http://localhost:8000" + argv[1])
    driver.set_window_size(1920, 1080)
    sleep(5)
    driver.save_screenshot(f"screen-{str(randint(1, 9999999))}.png")
    driver.close()


if __name__ == "__main__":
    main()
