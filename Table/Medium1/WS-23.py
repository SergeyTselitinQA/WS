from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

driver.find_element("xpath", "//*[@id='sortableTable']/thead/tr/th[4]").click()

rows = driver.find_elements("xpath", "//*[@id='sortableTableBody']/tr")

salary = [row.find_element("xpath", "./td[4]").text for row in rows]
salary_numeric = [int(s.replace('$', '').replace(',', '').strip()) for s in salary]
assert salary_numeric == sorted(salary_numeric), "Salary не отсортирована по возрастанию!"
