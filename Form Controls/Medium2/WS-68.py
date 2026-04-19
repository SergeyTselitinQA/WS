import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver =webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver, 10)

FILE_ONE = "foto.jpeg"
FILE_TWO = "redis.jpg"

driver.get("https://aqa-proka4.org/sandbox/web")

driver.find_element("xpath", "//*[@id='singleFile']").send_keys(f'{os.getcwd()}\\download\\foto.jpeg')
file_name_one = driver.find_element("xpath", "//*[@id='singleFileName']").text
assert FILE_ONE in file_name_one

button_input = driver.find_element("xpath", "//*[@id='multipleFiles']")
button_input.send_keys(f'{os.getcwd()}\\download\\redis.jpg')
file_name_two = driver.find_element("xpath", "//*[@id='multipleFilesList']").text
assert FILE_TWO in file_name_two

driver.find_element("xpath", "//*[@id='startProgressBtn']").click()
wait.until(lambda d: "width: 100%" in d.find_element("xpath", "//*[@id='animatedProgress']").get_attribute("style"))
width = driver.find_element("xpath", "//*[@id='animatedProgress']").get_attribute("style")
assert "width: 100%" in width
