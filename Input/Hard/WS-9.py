from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://aqa-proka4.org/sandbox/web")

driver.find_element("xpath", "//*[@id='dyn-name']").send_keys("Ivan")
driver.find_element("xpath", "//*[@name='email[]']").send_keys("test@gmail.com")
driver.find_element("xpath", "//*[@name='phone[]']").send_keys("+7999445566")
driver.find_element("xpath", "//*[@id='dynSubmitBtn']").click()

success = driver.find_element("xpath", "//*[@id='dynFormResult']").text
expected = "Форма успешно отправлена! Имя: Ivan Email (1): test@gmail.com Телефоны (1): +799944556"
assert expected in success.replace("\n", " ")
