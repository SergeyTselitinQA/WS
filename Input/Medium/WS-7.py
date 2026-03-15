from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

driver.find_element("xpath", "//*[@id='val-username']").send_keys("Username")
driver.find_element("xpath", "//*[@id='val-email']").send_keys("test@gmail.com")
driver.find_element("xpath", "//*[@id='val-password']").send_keys("123456Q1")
driver.find_element("xpath", "//input[@id='val-confirm-password']").send_keys("123456Q1")
driver.find_element("xpath", "//*[@id='valSubmitBtn']").click()

success = driver.find_element("xpath", "//*[text()='Все проверки пройдены! Форма валидна.']").text
mistake_user = driver.find_element("xpath", "//*[@id='username-error']")
mistake_email = driver.find_element("xpath", "//*[@id='email-error']")
mistake_password = driver.find_element("xpath", "//*[@id='password-error']")

assert success == 'Все проверки пройдены! Форма валидна.', 'Ошибка в валидации'
assert not mistake_user.is_displayed()
assert not mistake_email.is_displayed()
assert not mistake_password.is_displayed()
