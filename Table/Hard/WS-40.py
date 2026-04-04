from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

page_size = Select(driver.find_element("xpath", "//*[@id='pageSize']"))
page_size.select_by_value("5")

selected_option = page_size.first_selected_option
selected_text = selected_option.text.strip()
selected_value = selected_option.get_attribute("value")

# сохранить в переменную и проверить
visible = selected_text  # или selected_value, в зависимости что нужно
assert "5" in visible, f"Ожидалось чтобы в селекте отображалось '5', но увидели: {visible}"
