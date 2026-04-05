from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

TEXT_MODAL = """Это простое модальное окно для практики автоматизации.
Попробуйте найти кнопку закрытия и взаимодействовать с окном!"""

driver.get("https://aqa-proka4.org/sandbox/web")
driver.find_element("xpath", "//*[@id='openModalBtn']").click()

text_modal = driver.find_element("xpath", "//*[@id='simpleModal']//*[@class='p-6']").text
assert TEXT_MODAL == text_modal

driver.find_element("xpath", "//*[@id='closeModalBtn']").click()
elems = driver.find_elements("xpath", "//*[@id='simpleModal']")
assert len(elems) == 0 or not elems[0].is_displayed(), "Модал всё ещё открыт"

driver.find_element("xpath", "//*[@id='openModalBtn']").click()
driver.find_element("xpath", "//*[@id='confirmModalBtn']").click()

elements = driver.find_elements("xpath", "//*[@id='simpleModal']")
assert len(elements) == 0 or not elems[0].is_displayed(), "Модал всё ещё открыт"
