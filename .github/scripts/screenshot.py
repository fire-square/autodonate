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
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def main() -> None:
    """Main function of the script."""
    # Blacklist url regex expression
    expr = re.compile(r".*(auth|login|__|<|>|api).*")
    # Blacklist
    blacklist: List[str] = []

    # Load all urlpatterns
    urls: List[Dict[str, str]] = loads(check_output("poetry run python manage.py show_urls -uf json".split()).decode())

    # Initialize Chrome (pre-installed on GitHub Actions machine)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    # Download appropriate driver version for Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Iterate over screen widths
    for width in [1920, 720, 640, 480, 360]:
        # Iterate over all urls in urlpatterns
        for url in urls:
            # Check if url in blacklist
            if url["url"] in blacklist:
                continue

            # Check if url contains url arguments. Drop if hit.
            if expr.findall(url["url"].lower()):
                # Add to blacklist
                blacklist.append(url["url"])
                continue

            # Get page
            driver.get("http://localhost:8000" + url["url"])

            # Sleep 1 second, wait for redirects
            sleep(1)

            # Check if url contains url arguments. Drop if hit.
            if expr.findall(driver.current_url.lower()):
                # Add to blacklist
                blacklist.append(url["url"])
                continue

            # Set window size to page size (fullpage screenshot)
            driver.set_window_size(width, driver.execute_script("return document.body.parentNode.scrollHeight"))

            # Sleep more to ensure full page load
            sleep(2)

            # Save screenshot of body element, avoid scrollbar
            driver.find_element(by=By.TAG_NAME, value="body").screenshot(
                f"screenshot-{b64encode((url['url'] + ' (width: ' + str(width) + ')').encode()).decode()}.png"
            )

    # Properly close Chrome
    driver.close()


if __name__ == "__main__":
    main()
