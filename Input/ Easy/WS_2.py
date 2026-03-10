import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")
driver.find_element("xpath", "//*[@id='submitBtn']").click()
time.sleep(3)
try:
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    print("Текст уведомления:", alert_text)  # Вывод текста уведомления
    alert.accept()  # Закрыть уведомление
except Exception as e:
    print("Уведомление не отображается:", e)