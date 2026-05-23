from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

element = driver.find_element("xpath", "//*[@id='doubleClickBox']")
ActionChains(driver).double_click(element).perform()
count = driver.find_element("xpath", "//*[@id='doubleClickCount']").text
assert int(count) > 0
