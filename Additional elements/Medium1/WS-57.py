from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver, 5)

driver.get("https://aqa-proka4.org/sandbox/web")
driver.find_element("xpath", "//*[@id='addDisappearingBtn']").click()
element = wait.until(EC.presence_of_element_located(("xpath", "//*[@id='disappearing-1']")))
assert element.is_displayed()

wait_long = WebDriverWait(driver, 10)
wait_long.until(EC.invisibility_of_element(element))
