from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--incognito")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")
price = driver.find_element("xpath", "//*[@id='priceSlider']")

min_p = int(price.get_attribute("min") or 0)
max_p = int(price.get_attribute("max") or 100)
target = 850
width = price.size["width"]
pos_px = width * (target - min_p) / (max_p - min_p)
center = width / 2
offset = int(pos_px- center)
ActionChains(driver).click_and_hold(price).move_by_offset(offset, 0).release().perform()
assert price.get_attribute("value") == str(target)
