from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

driver.find_element("xpath", "//*[@id='copyButton']").click()
button_text = driver.find_element("xpath", "//*[@id='copyText']").text
assert "Скопировать" in button_text

success = driver.find_element(By.ID, "copySuccess")
assert "hidden" not in success.get_attribute("class")
