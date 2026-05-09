from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

Selenium = "Selenium — это инструмент для автоматизации веб-браузеров. Он поддерживает множество языков программирования, включая Python, Java, C#, и JavaScript."
Playwright = "Playwright — современный фреймворк для автоматизации браузеров от Microsoft. Поддерживает Chromium, Firefox и WebKit с единым API."
Cypress = "Cypress — это fast, easy и reliable testing для всего, что запускается в браузере. Отличается от Selenium архитектурой выполнения тестов."
Appium = "Appium — это open-source инструмент для автоматизации нативных, гибридных и веб-приложений на iOS и Android платформах."

driver.get("https://aqa-proka4.org/sandbox/web")

driver.find_element("xpath", "//*[contains(text(), 'Что такое Selenium?')]").click()
content_selenium = driver.find_element("xpath", "//*[@id='accordion1']")
text_selenium = content_selenium.text
assert content_selenium.is_displayed()
assert text_selenium == Selenium

driver.find_element("xpath", "//*[contains(text(), 'Что такое Playwright?')]").click()
content_playwright = driver.find_element("xpath", "//*[@id='accordion2']")
text_playwright = content_playwright.text
assert content_playwright.is_displayed()
assert text_playwright == Playwright

driver.find_element("xpath", "//*[contains(text(), 'Что такое Cypress?')]").click()
content_cypress = driver.find_element("xpath", "//*[@id='accordion3']")
text_cypress = content_cypress.text
assert content_cypress.is_displayed()
assert text_cypress == Cypress

driver.find_element("xpath", "//*[contains(text(), 'Что такое Appium?')]").click()
content_appium = driver.find_element("xpath", "//*[@id='accordion4']")
text_appium = content_appium.text
assert content_appium.is_displayed()
assert text_appium == Appium
