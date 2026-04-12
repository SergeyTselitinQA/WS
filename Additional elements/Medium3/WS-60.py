from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")
volume_slider = driver.find_element("xpath", "//*[@id='volumeSlider']")
driver.execute_script("arguments[0].value = 100", volume_slider)
driver.execute_script("arguments[0].dispatchEvent(new Event('input'))", volume_slider)
assert volume_slider.get_attribute("value") == "100"
