from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

driver.find_element("xpath", "//*[@id='dyn-name']").send_keys("Ivan")
driver.find_element("xpath", "//*[@name='email[]']").send_keys("test@gmail.com")
driver.find_element("xpath", "//*[@id='dynSubmitBtn']").click()

pwd = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", "//*[@name='phone[]']")))
val_msg = driver.execute_script("return arguments[0] ? arguments[0].validationMessage : null;", pwd)
assert val_msg == 'Заполните это поле.', 'Ошибка в регистации пользователя'
