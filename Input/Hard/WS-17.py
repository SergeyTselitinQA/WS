from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")
driver.find_element("xpath", "//*[contains(@class,'email-field-group')]/button").click()

alert = driver.switch_to.alert
alert.accept()

try:
    WebDriverWait(driver, 3).until(EC.alert_is_present())
    raise AssertionError("Alert всё ещё присутствует после accept()")
except TimeoutException:
    pass  # ожидаемо — алерт закрыт
