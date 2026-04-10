from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://aqa-proka4.org/sandbox/web")

container = driver.find_element("xpath", "//*[@id='infiniteScrollContainer']")
counter = len(driver.find_elements("xpath", "//*[contains(@class,'scroll-item')]"))
driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", container)

# Ожидание загрузки новых элементов:
new_count = len(driver.find_elements(By.CLASS_NAME, "scroll-item"))
assert new_count > counter
