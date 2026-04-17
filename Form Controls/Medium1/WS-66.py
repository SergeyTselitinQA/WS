from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

RESULT = "Страна: Великобритания\nИнструмент: Postman\nЯзыки: C#, Ruby\nОпыт: Lead (7+ лет)"

driver.get("https://aqa-proka4.org/sandbox/web")

country = Select(driver.find_element("xpath", "//*[@id='countrySelect']"))
country.select_by_value("uk")

automation = Select(driver.find_element("xpath", "//*[@id='automationTool']"))
automation.select_by_value("postman")

languages = Select(driver.find_element("xpath", "//*[@id='languagesSelect']"))
languages.select_by_value("csharp")
languages.select_by_value("ruby")

experience = Select(driver.find_element("xpath", "//*[@id='experienceSelect']"))
experience.select_by_value("lead")

driver.find_element("xpath", "//*[@id='showSelectBtn']").click()
result  = driver.find_element("xpath", "//*[@id='selectResult']").text
assert RESULT == result