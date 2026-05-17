import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

driver.find_element("xpath", "//*[@id='wizardFirstName']").send_keys("Ivan")
driver.find_element("xpath", "//*[@id='wizardLastName']").send_keys("Ivanov")
driver.find_element("xpath", "(//button[contains(text(), 'Далее')])[1]").click()

time.sleep(3)