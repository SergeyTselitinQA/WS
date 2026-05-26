from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

container = driver.find_element("xpath", "//*[@id='lazyLoadContainer']")
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", container)

# Ожидание загрузки изображений:
WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.CSS_SELECTOR, ".lazy-image-wrapper img"))
)

# Проверка что изображения загружены:
images = driver.find_elements(By.CSS_SELECTOR, ".lazy-image-wrapper img")
assert len(images) > 0
for img in images:
  assert img.get_attribute("src").startswith("https://")
