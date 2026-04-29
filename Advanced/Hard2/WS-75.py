import time

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
TOOLTIP_TWO = "Я снизу! 👇"
MENU = "Главная\nПрофиль\nНастройки\nВыход"

driver.get("https://aqa-proka4.org/sandbox/web")

button_one = driver.find_element("xpath", "//*[@id='tooltipBtn1']")
ActionChains(driver).move_to_element(button_one).perform()

tooltip = driver.find_element("xpath", "//*[contains(@class,'opacity-100')]").text
assert tooltip == TOOLTIP

button_two = driver.find_element("xpath", "//*[@id='tooltipBtn2']")
ActionChains(driver).move_to_element(button_two).perform()

tooltip_btn = driver.find_element("xpath", "//*[@id='tooltip2' and contains(@class, 'opacity-100')]").text
assert TOOLTIP_TWO == tooltip_btn

menu = driver.find_element("xpath", "//*[@id='hoverMenu']")
ActionChains(driver).move_to_element(menu).perform()

el = wait.until(EC.visibility_of_element_located(("xpath", "//*[@id='hoverDropdown' and contains(@class,'opacity-100')]")))
tooltip_menu = el.text
assert MENU == tooltip_menu

time.sleep(3)