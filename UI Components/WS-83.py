from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

star_one = driver.find_elements("xpath", "//*[@id='starRating1']//*[contains(@class,'star')]")
star_one[3].click()
start_one_result = driver.find_element("xpath", "//*[@id='ratingText1']").text
assert start_one_result == "4/5"

star_two = driver.find_elements("xpath", "//*[@id='starRating2']//*[contains(@class,'star2')]")
star_two[0].click()
start_two_result = driver.find_element("xpath", "//*[@id='ratingText2']").text
assert start_two_result == "1/5"
