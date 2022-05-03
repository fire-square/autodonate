"""Script for generating screenshots of the main page in ``.github/workflows/screenshot.yml``."""

from base64 import b64encode
from json import loads
from subprocess import check_output
from time import sleep
from typing import Dict, List

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main() -> None:
    """Main function of the script."""
    # Load all urls
    urls: List[Dict[str, str]] = loads(check_output("poetry run python manage.py show_urls -uf json".split()).decode())

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    for url in urls:
        # Check if url contains url arguments
        if url["url"].find("<") != -1:
            # Drop
            continue
        driver.get("http://localhost:8000" + url["url"])
        driver.set_window_size(1920, 1080)
        sleep(3)
        driver.save_screenshot(f"screenshot-{b64encode(url['url'].encode()).decode()}.png")
    driver.close()


if __name__ == "__main__":
    main()
