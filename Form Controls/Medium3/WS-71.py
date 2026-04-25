from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

email_toggle = driver.find_element("xpath", "//*[@id='emailToggle']")
element_email = driver.find_element("xpath", "(//*[contains(@class,'relative')])[1]")
if not email_toggle.is_selected():
    element_email.click()

push_toggle = driver.find_element("xpath", "//*[@id='pushToggle']")
element_push = driver.find_element("xpath", "(//*[contains(@class,'relative')])[2]")
if not push_toggle.is_selected():
    element_push.click()

dark_toggle = driver.find_element("xpath", "//*[@id='darkModeToggle']")
element_dark = driver.find_element("xpath", "(//*[contains(@class,'relative')])[3]")
if not dark_toggle.is_selected():
    element_dark.click()

color_picker = driver.find_element("xpath", "//*[@id='colorPicker']")
driver.execute_script("arguments[0].value = '#789e5b'", color_picker)
driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", color_picker)

assert email_toggle.is_selected() == True
assert push_toggle.is_selected() == True
assert dark_toggle.is_selected() == True

assert color_picker.get_attribute("value") == '#789e5b'
