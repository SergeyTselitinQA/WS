from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

INT_LIST = ['5', '1', '2', '3', '4']

driver.get("https://aqa-proka4.org/sandbox/web")
item1 = driver.find_element("xpath", "//*[contains(@data-position,'1')]")
item5 = driver.find_element("xpath", "//*[contains(@data-position,'5')]")

ActionChains(driver).click_and_hold(item5).move_to_element_with_offset(item1, 0, -10).release().perform()

items = driver.find_elements("xpath", "//*[contains(@class,'sortable-item')]")
positions = [item.get_attribute("data-position") for item in items]

assert INT_LIST == positions
