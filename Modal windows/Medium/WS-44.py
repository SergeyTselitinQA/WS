from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

driver.find_element("xpath", "//*[@id='openNestedModalBtn']").click()
modal_one = driver.find_element("xpath", "//*[@id='nestedModal1']")
assert "flex" in modal_one.get_attribute("class")

driver.find_element("xpath", "//*[@id='openNestedModal2Btn']").click()
modal_two = driver.find_element("xpath", "//*[@id='nestedModal2']")
assert  "flex" in modal_two.get_attribute("class")

driver.find_element("xpath", "//*[@id='openNestedModal3Btn']").click()
modal_three = driver.find_element("xpath", "//*[@id='nestedModal3']")
assert "flex" in modal_three.get_attribute("class")

driver.find_element("xpath", "//*[@id='closeNestedModal3Btn']").click()
driver.find_element("xpath", "//*[@id='closeNestedModal2Btn']").click()
driver.find_element("xpath", "//*[@id='closeNestedModal1Btn']").click()

modal_window = driver.find_elements("xpath", "//*[@id='nestedModal1' and contains(@class,'hidden')]")
assert len(modal_window) == 1