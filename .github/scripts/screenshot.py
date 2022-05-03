"""Script for generating screenshots of the main page in ``.github/workflows/screenshot.yml``."""

from time import sleep
from urllib.parse import urlencode

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main() -> None:
    """Main function of the script."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    for url in ["/", "/#donate", "/#about", "/django-admin", "/admin"]:
        driver.get("http://localhost:8000" + url)
        driver.set_window_size(1920, 1080)
        sleep(5)
        driver.save_screenshot(f"Screenshot+{urlencode(url)}.png")
        driver.close()


if __name__ == "__main__":
    main()
