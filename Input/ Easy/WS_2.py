from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://aqa-proka4.org/sandbox/web")

# ждём появление поля пароля
pwd = WebDriverWait(driver, 10).until(EC.presence_of_element_located(("xpath", "//*[@id='username']")))

# убедимся, что поле required (если нет — validationMessage будет пуст)
# вызвать валидацию: клик на сабмит или reportValidity
submit = driver.find_element("xpath", "//*[@id='submitBtn']")
submit.click()

# безопасно получить validationMessage у найденного элемента
val_msg = driver.execute_script("return arguments[0] ? arguments[0].validationMessage : null;", pwd)
assert val_msg == 'Заполните это поле.', 'Ошибка в регистации пользователя'
