from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from os import listdir, mkdir, chdir, remove
from os.path import isdir, isfile
from shutil import rmtree
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("http://localhost:8000/")
driver.set_window_size(1920, 1080)
sleep(5)
driver.save_screenshot(f'screen.png')
driver.close()
