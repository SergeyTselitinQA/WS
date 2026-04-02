from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

table_head = ["ID", "Name", "Email", "Status"]

driver.get("https://aqa-proka4.org/sandbox/web")
th_elements = driver.find_elements("xpath", "//*[@id='filterableTable']//thead//th")
result_head = [th.text.strip() for th in th_elements]
assert table_head == result_head, "Заголовок таблицы не соответствует ожидаемому результау"
