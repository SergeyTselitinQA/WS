from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")
driver.find_element("xpath", "//*[@title='Очистить']").click()
editor = driver.find_element("xpath", "//*[@id='wysiwygEditor']")
editor.send_keys("Тестовый текст")

driver.find_element("xpath", "//button[@title='Жирный']").click()
editor.send_keys("жирный текст")

html_content = driver.execute_script("return arguments[0].innerHTML", editor)
assert "<strong>" in html_content or "<b>" in html_content
