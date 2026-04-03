from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")
driver.find_element("xpath", "//*[@id='nextPageBtn']").click()
driver.find_element("xpath", "//*[@id='nextPageBtn']").click()
driver.find_element("xpath", "//*[@id='nextPageBtn']").click()
action_btn = driver.find_element("xpath", "//*[contains(@class,'page-btn') and contains(@class,'bg-blue-600')]").text

assert action_btn == "4"