from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://aqa-proka4.org/sandbox/web"

EXPECTED_HEADERS = ["ID", "Name", "Email", "Status", "Actions"]
EXPECTED_ROWS = [
    {"id": "1", "name": "John Doe", "email": "john@example.com", "status": "Active"},
    {"id": "2", "name": "Jane Smith", "email": "jane@example.com", "status": "Pending"},
    {"id": "3", "name": "Bob Johnson", "email": "bob@example.com", "status": "Inactive"}
]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver, 10)

driver.get(URL)
table = wait.until(EC.visibility_of_element_located(("xpath", "//*[@id='usersTable']")))
header_elements = table.find_elements("xpath", "//*[@id='usersTable']/thead/tr/th")

# Проверка заголовков
headers = [h.text.strip() for h in header_elements]
assert headers == EXPECTED_HEADERS

# Получение строк тела таблицы
rows = table.find_elements("xpath", "//*[@id='usersTable']/tbody/tr")
assert len(rows) == len(EXPECTED_ROWS), f"Получили количество  строк {len(rows)}, ожидали {len(EXPECTED_ROWS)}"
