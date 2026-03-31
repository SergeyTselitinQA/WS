from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

string_value = "Показано: 6 из 6 записей"

driver.get("https://aqa-proka4.org/sandbox/web")
input_name = driver.find_element("xpath", "//*[@id='filterInput']")
input_name.send_keys("Eve Martinez")

input_name.send_keys(Keys.CONTROL, "a")
input_name.send_keys(Keys.DELETE)
string_int = driver.find_element("xpath", "//*[@id='filterCount']").text

assert string_value == string_int
