from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

string_int = "Показано: 0 из 6 записей"
driver.get("https://aqa-proka4.org/sandbox/web")
driver.find_element("xpath", "//*[@id='filterInput']").send_keys("Ivan")
result_string = driver.find_element("xpath", "//*[@id='filterCount']").text

assert string_int == result_string
