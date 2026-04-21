import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

email_toggle = driver.find_element("xpath", "(//*[contains(@class,'relative ')])[1]")
id_email = driver.find_element("xpath", "//*[@id='emailToggle']")
if not id_email.is_selected():
    email_toggle.click()

push_toggle = driver.find_element("xpath", "(//*[contains(@class,'relative ')])[2]")
id_push = driver.find_element("xpath", "//*[@id='pushToggle']")
if not id_push.is_selected():
    push_toggle.click()

dark_toggle = driver.find_element("xpath", "(//*[contains(@class,'relative ')])[3]")
id_dark = driver.find_element("xpath", "//*[@id='darkModeToggle']")
if not id_dark.is_selected():
    dark_toggle.click()



assert id_email.is_selected() == True
assert id_push.is_selected() == True
assert id_dark.is_selected() == True

# color_picker = driver.find_element("xpath", "colorPicker")
# driver.execute_script("arguments[0].value = '#FF0000'", color_picker)

time.sleep(5)