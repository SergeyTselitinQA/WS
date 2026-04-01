from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

status = "Active"

driver.get("https://aqa-proka4.org/sandbox/web")
user_status = driver.find_element("xpath", "(//*[@id='filterableTableBody']/tr/td/span)[1]").text

assert status == user_status, "Не верный статус"
