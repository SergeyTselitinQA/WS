from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

INPUT = "Appium"

driver.get("https://aqa-proka4.org/sandbox/web")

input_btn = driver.find_element("xpath", "//*[@id='autocompleteInput']")
input_btn.send_keys("Appium")
options = driver.find_elements("xpath", "//*[@id='autocompleteDropdown']")
options[0].click()
auto_complete = driver.find_element("xpath", "//*[@id='autocompleteInput']")
selected = auto_complete.get_attribute("value")
assert INPUT == selected
