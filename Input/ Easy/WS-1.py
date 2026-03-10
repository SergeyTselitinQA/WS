from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

driver.get("https://aqa-proka4.org/sandbox/web")

a= ("xpath", "//*[@id='username']")
wait.until(EC.element_to_be_clickable(a))
driver.find_element(*a).send_keys("Ivan")

driver.find_element("xpath", "//*[@id='email']").send_keys("test@gmail.com")
driver.find_element("xpath", "//*[@id='password']").send_keys("Qwerty11!")
DROPDOWN_ELEMENT = ("xpath", "//*[@id='country']")
DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))
DROPDOWN.select_by_value("ru")
driver.find_element("xpath", "//*[@id='terms']").click()
driver.find_element("xpath", "//*[@id='submitBtn']").click()
element_success = driver.find_element("xpath", "//*[@id='formResult']").text
assert element_success == 'Форма успешно отправлена!', 'Ошибка в регистации пользователя'
