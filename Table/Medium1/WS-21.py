from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")
driver.find_element("xpath", "//*[@id='sortableTable']/thead/tr/th[2]").click()
driver.find_element("xpath", "//*[@id='sortableTable']/thead/tr/th[2]").click()

rows = driver.find_elements("xpath", "//*[@id='sortableTableBody']/tr")
names = [row.find_element("xpath", "./td[2]").text for row in rows]

assert names == sorted(names, reverse=True), "Имена не отсортированы в обратном порядке по алфавиту!"
