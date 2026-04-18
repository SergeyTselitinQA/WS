from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

RESULT = "Страна: Германия\nИнструмент: Appium\nЯзыки: Python, Ruby\nОпыт: Senior (5+ лет)"
SELECTED = ['python', 'ruby']

driver.get("https://aqa-proka4.org/sandbox/web")

country = Select(driver.find_element("xpath", "//*[@id='countrySelect']"))
country.select_by_value("de")

automation = Select(driver.find_element("xpath", "//*[@id='automationTool']"))
automation.select_by_value("appium")

languages = Select(driver.find_element("xpath", "//*[@id='languagesSelect']"))
languages.select_by_value("python")
languages.select_by_value("ruby")
selected = [opt.get_attribute("value") for opt in languages.all_selected_options]

experience = Select(driver.find_element("xpath", "//*[@id='experienceSelect']"))
experience.select_by_value("senior")

driver.find_element("xpath", "//*[@id='showSelectBtn']").click()

result = driver.find_element("xpath", "//*[@id='selectResult']").text
assert RESULT == result
assert SELECTED == selected
