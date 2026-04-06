from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

NAME = "Anastasiya"
TEXT = "Привет, Anastasiya!"

driver.get("https://aqa-proka4.org/sandbox/web")
driver.find_element("xpath", "//*[@id='promptBtn']").click()
alert = driver.switch_to.alert
alert.send_keys(NAME)
alert.accept()
text = alert.text
assert text == TEXT
alert.accept()

wait.until_not(EC.alert_is_present(), message="Alert не исчез за отведённое время")
assert True  # если wait не выбросил — ок