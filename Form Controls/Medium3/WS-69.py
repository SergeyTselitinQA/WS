import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

email_toggle = driver.find_element("xpath", "//*[@id='emailToggle']")
if not email_toggle.is_selected():
    email_toggle.click()

push_toggle = driver.find_element("xpath", "//*[@id='pushToggle']")
if not push_toggle.is_selected():
    push_toggle.click()

dark_toggle = driver.find_element("xpath", "//*[@id='darkModeToggle']")
if not dark_toggle.is_selected():
    dark_toggle.click()

time.sleep(5)