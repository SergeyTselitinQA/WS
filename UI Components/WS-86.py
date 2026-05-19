from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

shadow_host = driver.find_element(By.ID, "shadowHost")
shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)
button = shadow_root.find_element(By.CSS_SELECTOR, "button")
button.click()


count = driver.execute_script("return arguments[0].shadowRoot.querySelector('.click-count')", shadow_host)
num_count = driver.execute_script("return arguments[0].textContent", count)
assert "1" in num_count
