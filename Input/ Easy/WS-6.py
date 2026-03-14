import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

driver.find_element("xpath", "//*[@id='username']").send_keys("Ivan")
driver.find_element("xpath", "//*[@id='email']").send_keys("test@gmail.com")
driver.find_element("xpath", "//*[@id='password']").send_keys("Qwerty11!")
DROPDOWN_ELEMENT = ("xpath", "//*[@id='country']")
DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))
DROPDOWN.select_by_value("ru")
driver.find_element("xpath", "//*[@id='submitBtn']").click()

pwd = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", "//*[@id='terms']")))
val_msg = driver.execute_script("return arguments[0] ? arguments[0].validationMessage : null;", pwd)
assert val_msg == 'Чтобы продолжить, установите этот флажок.', 'Ошибка в регистации пользователя'
print("validationMessage:", val_msg)
time.sleep(3)