from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

driver.find_element("xpath", "(//*[@id='sortableTable']/thead/tr/th)[1]").click()
rows = driver.find_elements("xpath", "//*[@id='sortableTableBody']/tr")
ids = [int(row.find_element("xpath", "./td[1]").text) for row in rows]

assert all(ids[i] <= ids[i + 1] for i in range(len(ids) - 1)), "IDs не отсортированы по возрастанию!"
