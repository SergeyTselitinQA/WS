from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service =Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")
DROPDOWN_ELEMENT = ("xpath", "//*[@id='statusFilter']")
DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))
DROPDOWN.select_by_visible_text("Active")

row1 = driver.find_elements("xpath", "//*[contains(@class,'table-row') and not(contains(@class,'hidden'))]")
assert len(row1) == 3

DROPDOWN.select_by_visible_text("Inactive")
row2 = driver.find_elements("xpath", "//*[contains(@class,'table-row') and not(contains(@class,'hidden'))]")
assert len(row2) == 2

DROPDOWN.select_by_visible_text("Pending")
row2 = driver.find_elements("xpath", "//*[contains(@class,'table-row') and not(contains(@class,'hidden'))]")
assert len(row2) == 1
