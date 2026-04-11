from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)



driver.get("https://aqa-proka4.org/sandbox/web")
volume_slider = driver.find_element("xpath", "//*[@id='volumeSlider']")
ActionChains(driver).click_and_hold(volume_slider).move_by_offset(510, 0).release().perform()

result_volume = volume_slider.get_attribute("value")
assert result_volume == "100", f"Получили {result_volume}"