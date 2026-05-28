from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver, 10)

driver.get("https://aqa-proka4.org/sandbox/web")

btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Перейти к товарам')]")))
btn.click()
btn_two = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(),'Далее')])[3]")))
btn_two.click()
# Получение всех элементов breadcrumb:
breadcrumbs = driver.find_elements(By.CSS_SELECTOR, ".breadcrumb-item")
assert len(breadcrumbs) > 1

# Клик по определенному breadcrumb:
driver.find_element(By.XPATH, "//a[contains(text(), 'Товары')]").click()

# Проверка текущего breadcrumb пути:
breadcrumb_text = driver.find_element(By.ID, "breadcrumbNav").text
assert "Главная" in breadcrumb_text

