import time

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
prefs = {'download.default_directory': f"{os.getcwd()}\\download",}

chrome_options.add_experimental_option("prefs", prefs)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

xpath = "//button[contains(normalize-space(.),'sample.txt')]"
el = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
WebDriverWait(driver, 10).until(EC.visibility_of(el))
el.click()

dl = os.path.join(os.getcwd(), "download")
end = time.time() + 30  # таймаут 30 с
while time.time() < end:
    names = os.listdir(dl) if os.path.isdir(dl) else []
    # если есть .crdownload — ждём
    if any(n.endswith(".crdownload") and "sample" in n for n in names):
        time.sleep(0.5)
        continue
    # если появился готовый .txt — успех
    if any(n.endswith(".txt") and "sample" in n for n in names):
        break
    time.sleep(0.5)

assert any(n.endswith(".txt") and "sample" in n for n in os.listdir(dl)), \
    f"Файлы sample*.txt не найдены в {dl}"

time.sleep(3)