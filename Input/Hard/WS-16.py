from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

driver.find_element("xpath", "//*[@name='phone[]']").send_keys("+7999")
driver.find_element("xpath", "//*[@id='addPhoneBtn']").click()
driver.find_element("xpath", "(//*[@name='phone[]'])[2]").send_keys("+37525")
driver.find_element("xpath", "//*[@id='addPhoneBtn']").click()
driver.find_element("xpath", "(//*[@name='phone[]'])[3]").send_keys("+1103")

phone_list = driver.find_elements("xpath", "(//*[contains(@class,'phone-field-group')]/button)")
phone_list[-1].click()
phone_counter = driver.find_elements("xpath", "//*[contains(@class,'phone-field-group')]")

assert len(phone_counter) == 2
