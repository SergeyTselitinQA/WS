from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

# найти все видимые строки в tbody
rows = driver.find_elements("xpath", "//*[@id='filterableTable']//tbody//tr[not(contains(@class,'hidden'))]")

# вариант A: проверка по ID в первой колонке
ids = [row.find_element("xpath", "./td[1]").text.strip() for row in rows]
assert len(ids) == len(set(ids)), f"Найдены дубликаты ID: {[x for x in ids if ids.count(x) > 1]}"
