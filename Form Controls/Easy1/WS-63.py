from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

result_one = "Условия приняты. Выбрано навыков: 0 (нет)"

driver.get("https://aqa-proka4.org/sandbox/web")
driver.find_element("xpath", "//*[@id='termsCheckbox']").click()
driver.find_element("xpath", "//*[@id='showCheckboxBtn']").click()
result_text = driver.find_element("xpath", "//*[@id='selectedSkills']").text
assert result_one == result_text

driver.find_element("xpath", "//*[@id='selectAllSkills']").click()
driver.find_element("xpath", "//*[@id='showCheckboxBtn']").click()
checked = driver.find_elements(By.CSS_SELECTOR, ".skill-checkbox:checked")
int_checked = [hui.get_attribute("value") for hui in checked]
assert len(int_checked) == 5

driver.find_element("xpath", "(//*[contains(@class,'skill-checkbox')])[3]").click()
driver.find_element("xpath", "//*[@id='showCheckboxBtn']").click()
checked1 = driver.find_elements(By.CSS_SELECTOR, ".skill-checkbox:checked")
value = [q.get_attribute("value") for q in checked1]
assert len(value) == 4
