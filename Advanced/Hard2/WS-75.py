import time
from ctypes.macholib.framework import framework_info

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver, 10)

TOOLTIP = "Это всплывающая подсказка!"

driver.get("https://aqa-proka4.org/sandbox/web")

button_one = driver.find_element("xpath", "//*[@id='tooltipBtn1']")
ActionChains(driver).move_to_element(button_one).perform()

tooltip = driver.find_element("xpath", "//*[contains(@class,'opacity-100')]").text
assert tooltip == TOOLTIP


time.sleep(3)