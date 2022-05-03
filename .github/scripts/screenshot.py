"""Script for generating screenshots of the main page in ``.github/workflows/screenshot.yml``."""

import re
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
    # Blacklist url regex expression
    expr = re.compile(r".*(auth|login|__|<|>|api).*")

    # Load all urlpatterns
    urls: List[Dict[str, str]] = loads(check_output("poetry run python manage.py show_urls -uf json".split()).decode())

    # Initialize Chrome (pre-installed on GitHub Actions machine)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # Download appropriate driver version for Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Iterarate over all urls in urlpatterns
    for url in urls:
        driver.get("http://localhost:8000" + url["url"])

        # Sleep 1 second, wait for redirects
        sleep(1)

        # Check if url contains url arguments. Drop if hit.
        if expr.findall(driver.current_url, flags=re.I):
            continue

        # Set window size to page size (fullpage screenshot)
        required_width = driver.execute_script("return document.body.parentNode.scrollWidth")
        required_height = driver.execute_script("return document.body.parentNode.scrollHeight")
        driver.set_window_size(required_width, required_height)

        # Sleep more to ensure full page load
        sleep(2)

        # Save screenshot of body element, avoid scrollbar
        driver.find_element_by_tag_name("body").screenshot(f"screenshot-{b64encode(url['url'].encode()).decode()}.png")

    # Properly close Chrome
    driver.close()


if __name__ == "__main__":
    main()
