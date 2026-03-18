from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

driver.find_element("xpath", "//*[@id='dyn-name']").send_keys("ivan")

driver.find_element("xpath", "//*[@name='email[]']").send_keys("test1@gmail.com")
driver.find_element("xpath", "//*[@id='addEmailBtn']").click()
driver.find_element("xpath", "(//*[@name='email[]'])[2]").send_keys("test2@gmail.com")
driver.find_element("xpath", "//*[@id='addEmailBtn']").click()
driver.find_element("xpath", "(//*[@name='email[]'])[3]").send_keys("test3@gmail.com")

email_counter = driver.find_elements("xpath", "//*[contains(@class, 'email-field-group')]")
assert len(email_counter) == 3
