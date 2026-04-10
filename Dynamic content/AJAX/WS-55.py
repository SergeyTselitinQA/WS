from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver, 5)

driver.get("https://aqa-proka4.org/sandbox/web")
driver.find_element("xpath", "//*[@id='loadAjaxBtn']").click()

# Ожидание появления loader:
wait.until(EC.visibility_of_element_located((By.ID, "ajaxLoader")))

# Ожидание исчезновения loader и появления контента:
wait.until(EC.invisibility_of_element_located((By.ID, "ajaxLoader")))
wait.until(EC.visibility_of_element_located((By.ID, "ajaxContent")))

rows = driver.find_elements("xpath", "//*[@id='ajaxTableBody']/tr")

assert len(rows) > 0
