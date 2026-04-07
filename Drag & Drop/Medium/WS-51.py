from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

source = driver.find_element("xpath", "//*[contains(@data-item, 'item3')]")
target = driver.find_element("xpath", "//*[@id='selectedItems']")
area_input = driver.find_element("xpath", "//*[@id='availableItems']")

ActionChains(driver).drag_and_drop(source, target).perform()
items = driver.find_elements("xpath", "//*[@id='selectedItems']//*[contains(@class,'draggable')]")
assert len(items)  > 0

ActionChains(driver).drag_and_drop(source, area_input).perform()
items = driver.find_elements("xpath", "//*[@id='selectedItems']//*[contains(@class,'draggable')]")
assert len(items)  == 0
