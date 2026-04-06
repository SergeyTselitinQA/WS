from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://aqa-proka4.org/sandbox/web")
driver.find_element("xpath", "//*[@id='alertBtn']").click()
alert = driver.switch_to.alert
alert.accept()

# ожидаем и утверждаем, что alert отсутствует
wait.until_not(EC.alert_is_present(), message="Alert не исчез за отведённое время")
assert True  # если wait не выбросил — ок
