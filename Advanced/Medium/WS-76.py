from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver, 10)

COPY = "Копировать"
PASTE = "Вставить"
EDIT = "Редактировать"
DELETE = "Удалить"

driver.get("https://aqa-proka4.org/sandbox/web")

element_area = driver.find_element("xpath", "//*[@id='contextArea']")

ActionChains(driver).context_click(element_area).perform()
driver.find_element("xpath", "(//*[contains(text(), 'Копировать')])[1]").click()
copy = driver.find_element("xpath", "//*[@id='selectedAction']").text
assert COPY == copy

ActionChains(driver).context_click(element_area).perform()
driver.find_element("xpath", "(//*[contains(text(), 'Вставить')])[1]").click()
paste = driver.find_element("xpath", "//*[@id='selectedAction']").text
assert PASTE == paste

ActionChains(driver).context_click(element_area).perform()
driver.find_element("xpath", "(//*[contains(text(), 'Редактировать')])[1]").click()
edit = driver.find_element("xpath", "//*[@id='selectedAction']").text
assert EDIT == edit

driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element_area)
ActionChains(driver).context_click(element_area).perform()
driver.find_element("xpath", "(//*[contains(text(), 'Удалить')])[1]").click()
delete = driver.find_element("xpath", "//*[@id='selectedAction']").text
assert DELETE == delete
