import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

code = "123456"
for i, digit in enumerate(code, 1):
  driver.find_element(By.ID, f"otp{i}").send_keys(digit)

for i in range(1, 7):
  value = driver.find_element(By.ID, f"otp{i}").get_attribute("value")
  assert len(value) == 1

full_code = "".join([driver.find_element(By.ID, f"otp{i}").get_attribute("value") for i in range(1, 7)])
assert code == full_code