from  selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

driver.find_element("xpath", "//*[@id='successModalBtn']").click()
modal_total = driver.find_element("xpath", "//*[@id='dynamicModal']")
assert "Операция выполнена" in modal_total.text

modal = driver.find_element("xpath", "(//*[@id='dynamicModalContainer']//div[contains(@class,'border-green-500')])[1]")
assert "border-green-500" in modal.get_attribute("class")
