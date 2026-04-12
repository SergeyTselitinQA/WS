from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

volume_slider = driver.find_element("xpath", "//*[@id='tempSlider']")
min_v = int(volume_slider.get_attribute("min") or 0)
max_v = int(volume_slider.get_attribute("max") or 100)
target = 30
width = volume_slider.size['width']
pos_px = width * (target - min_v) / (max_v - min_v)
center = width / 2.0
offset = int(pos_px - center)
ActionChains(driver).click_and_hold(volume_slider).move_by_offset(offset, 0).release().perform()
assert volume_slider.get_attribute("value") == str(target)
