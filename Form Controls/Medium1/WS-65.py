from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

RESULT = "Страна: Россия\nИнструмент: Playwright\nЯзыки: Python, JavaScript\nОпыт: Junior (0-2 года)"

driver.get("https://aqa-proka4.org/sandbox/web")
country = Select(driver.find_element("xpath", "//*[@id='countrySelect']"))
country.select_by_value("ru")

automation = Select(driver.find_element("xpath", "//*[@id='automationTool']"))
automation.select_by_value("playwright")

languages = Select(driver.find_element("xpath", "//*[@id='languagesSelect']"))
languages.select_by_value("python")
languages.select_by_value("javascript")

experience = Select(driver.find_element("xpath", "//*[@id='experienceSelect']"))
experience.select_by_value("junior")

driver.find_element("xpath", "//*[@id='showSelectBtn']").click()
result = driver.find_element("xpath", "//*[@id='selectResult']").text
assert RESULT == result
