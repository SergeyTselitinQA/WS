from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

TEXT = "Способ оплаты: Криптовалюта\nПлан подписки: Pro ($29)"

driver.get("https://aqa-proka4.org/sandbox/web")

card_radio = driver.find_element("xpath", "//*[@id='paymentCard']")
card_radio.click()
assert card_radio.is_selected()

pay = driver.find_element("xpath", "//*[@id='paymentPaypal']")
pay.click()
assert pay.is_selected()

bitcoin = driver.find_element("xpath", "//*[@id='paymentCrypto']")
bitcoin.click()
assert bitcoin.is_selected()

pro = driver.find_element("xpath", "//*[@id='planPro']")
pro.click()
assert pro.is_selected()

driver.find_element("xpath", "//*[@id='showRadioBtn']").click()
text = driver.find_element("xpath", "//*[@id='radioResult']").text
assert text == TEXT
