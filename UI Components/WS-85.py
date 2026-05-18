from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

FORM_TEXT = "Форма успешно отправлена!"

driver.get("https://aqa-proka4.org/sandbox/web")

driver.find_element("xpath", "//*[@id='wizardFirstName']").send_keys("Ivan")
driver.find_element("xpath", "//*[@id='wizardLastName']").send_keys("Ivanov")
driver.find_element("xpath", "(//button[contains(text(), 'Далее')])[1]").click()

number_one = driver.find_element("xpath", "//*[@id='step1Indicator']")
class_one = number_one.get_attribute("class")
assert "bg-green-600" in class_one

driver.find_element("xpath", "//*[@id='wizardEmail']").send_keys("test@gmail.com")
driver.find_element("xpath", "//*[@id='wizardPhone']").send_keys("+7111223")
driver.find_element("xpath", "(//button[contains(text(), 'Далее')])[2]").click()

number_two = driver.find_element("xpath", "//*[@id='step2Indicator']")
class_two = number_two.get_attribute("class")
assert "bg-green-600" in class_two

driver.find_element("xpath", "//*[@onclick='submitWizard()']").click()
form_text = driver.find_element("xpath", "//*[@id='wizardSuccess']").text
assert form_text == FORM_TEXT
