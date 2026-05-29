from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

canvas = driver.find_element(By.ID, "drawingCanvas")

# Рисование линии:
actions = ActionChains(driver)
actions.move_to_element_with_offset(canvas, 50, 50)
actions.click_and_hold()
actions.move_by_offset(100, 100)
actions.release()
actions.perform()

# Проверка что canvas изменился:
canvas_data = driver.execute_script("return arguments[0].toDataURL()", canvas)
