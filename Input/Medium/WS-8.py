from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

driver.find_element("xpath", "//*[@id='valSubmitBtn']").click()
mistake_user = driver.find_element("xpath", "//*[@id='username-error']")
mistake_email = driver.find_element("xpath", "//*[@id='email-error']")
mistake_password = driver.find_element("xpath", "//*[@id='password-error']")

assert mistake_user.is_displayed()
assert mistake_email.is_displayed()
assert mistake_password.is_displayed()

assert "Username должен содержать минимум 5 символов" in mistake_user.text
assert "Email должен содержать символ @" in mistake_email.text
assert "Password должен содержать минимум 8 символов, включая буквы и цифры" in mistake_password.text
