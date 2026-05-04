import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

main_window = driver.current_window_handle

# клик, открывающий новую вкладку
driver.find_element(By.XPATH, "//*[@id='openTabBtn']").click()
WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
time.sleep(1)

window_two = driver.window_handles
driver.switch_to.window(window_two[1])
driver.find_element("xpath", "//*[@id='paymentCard']").click()
time.sleep(1)

driver.switch_to.window(main_window)
elem = driver.find_element(By.ID, "paymentCard")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", elem)
elem.click()
time.sleep(1)

driver.find_element("xpath", "//*[@id='openWindowBtn']").click()
time.sleep(1)
three = driver.window_handles
driver.switch_to.window(three[2])
elem = driver.find_element(By.ID, "paymentCard")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", elem)
elem.click()
time.sleep(1)

driver.switch_to.window(main_window)
time.sleep(1)
driver.find_element("xpath", "//*[@id='openMultipleBtn']").click()
time.sleep(1)
all_window = driver.window_handles
assert len(all_window) == 6
time.sleep(1)
driver.close()
finish = driver.window_handles
assert len(finish)  == 5
