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
page_size.select_by_value("20")

select_options  = page_size.first_selected_option
selected_text = select_options.text.strip()
selected_value = select_options.get_attribute("value")

visible = selected_text
visible_value = selected_value

assert "20" == visible_value, f"Ожидалось чтобы в селекте отображалось '20', но увидели: {visible_value}"
assert "20" in visible, f"Ожидалось чтобы в селекте отображалось '20', но увидели: {visible}"