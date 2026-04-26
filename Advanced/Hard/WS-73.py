from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

SIMPLE_FRAME = "✓ Кнопка нажата!"
LEVEL_TWO = "✓ Вложенная кнопка нажата!"
ALERT = "Кнопка в родительском frame нажата!"
CHILD_FRAME = "✓ Вложенная кнопка нажата!"

wait = WebDriverWait(driver, 10)

driver.get("https://aqa-proka4.org/sandbox/web")

driver.switch_to.frame("simpleFrame")
driver.find_element("xpath", "//*[@id='iframeButton']").click()
simple_frame = driver.find_element("xpath", "//*[@id='iframeResult']").text
assert SIMPLE_FRAME == simple_frame
driver.switch_to.default_content()

driver.switch_to.frame("parentFrame")
driver.find_element("xpath", "//*[@id='parentButton']").click()
alert = wait.until(EC.alert_is_present())
text = alert.text
assert  ALERT == text
alert.accept()

driver.switch_to.frame("childFrame")
driver.find_element("xpath", "//*[@id='childButton']").click()
child_frame = driver.find_element("xpath", "//*[@id='childResult']").text
assert CHILD_FRAME == child_frame
