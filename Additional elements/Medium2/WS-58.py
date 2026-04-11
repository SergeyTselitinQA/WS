from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

RESULT = "Дата: 2026-12-31 | Дата и время: 2026-12-31T23:56 | Время: 03:20 | Неделя: 2026-W19"

driver.get("https://aqa-proka4.org/sandbox/web")
driver.find_element("xpath", "//*[@id='datePicker']").send_keys("31.12.2026")
el = driver.find_element("xpath", "//*[@id='dateTimePicker']")
el.send_keys("31.12.2026")
el.send_keys(Keys.TAB)
el.send_keys("23:56")
driver.find_element("xpath", "//*[@id='timePicker']").send_keys("03:20")
driver.find_element("xpath", "//*[@id='weekPicker']").send_keys("19.2026")
driver.find_element("xpath", "//*[@id='showDateBtn']").click()

result = driver.find_element("xpath", "//*[@id='selectedDate']").text
assert result == RESULT

