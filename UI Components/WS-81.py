import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

TEXT = "Слайд 2"

driver.get("https://aqa-proka4.org/sandbox/web")

driver.find_element("xpath", "//*[@id='carouselNextBtn']").click()
time.sleep(1)
carousel_track = driver.find_element("xpath", "(//*[@id='carouselTrack']//h3)[2]").text
assert carousel_track == TEXT

dot = driver.find_element("xpath", "(//*[contains(@class, 'carousel-dot')])[3]")
dot.click()
cls = dot.get_attribute("class")
assert "bg-blue-600" in cls
