import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

Ctrl_S = "Ctrl + S (Сохранить)"
Ctrl_Enter = "Ctrl + Enter (Отправить)"
Escape = "Escape (Закрыть)"
Alt_H = "Alt + H (Помощь)"

driver.get("https://aqa-proka4.org/sandbox/web")

body = driver.find_element("xpath", "//body")
body.send_keys(Keys.CONTROL + "s")

elem = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "keyPressed"))
)
text = elem.text
assert Ctrl_S == text

body.send_keys(Keys.CONTROL, Keys.ENTER)
text_enter = elem.text
assert Ctrl_Enter == text_enter

body.send_keys(Keys.ESCAPE)
text_escape = elem.text
assert Escape == text_escape

body.send_keys(Keys.ALT + "h")
text_alt = elem.text
assert Alt_H == text_alt

time.sleep(1)