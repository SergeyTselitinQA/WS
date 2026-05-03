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

# ждём появления новой вкладки
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

all_windows = driver.window_handles

# переключаемся на первую вкладку, отличную от main
for window in all_windows:
    if window != main_window:
        driver.switch_to.window(window)
        break

# ждём, пока кнопка в новой вкладке станет кликабельной, затем кликаем
elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "tooltipBtn1")))
elem.click()

before = set(driver.window_handles)

# клик, открывающий новое окно
driver.find_element(By.XPATH, "//*[@id='openWindowBtn']").click()

# дождаться появления нового окна
WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > len(before))

# найти handle нового окна (разница множеств)
after = set(driver.window_handles)
new_handles = after - before
if not new_handles:
    raise RuntimeError("Не удалось найти новый window handle")
new_window = new_handles.pop()

# переключиться на новое окно и сфокусировать его
driver.switch_to.window(new_window)
driver.execute_script("window.focus();")

# проверка
print("switched to:", driver.current_window_handle, "title:", driver.title, "url:", driver.current_url)

# затем можно ждать и кликать в новом окне
elem = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "tooltipBtn1")))
elem.click()


print(all_windows)
time.sleep(3)