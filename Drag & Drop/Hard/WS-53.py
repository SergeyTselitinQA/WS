from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://aqa-proka4.org/sandbox/web")

task1 = driver.find_element("xpath", "//*[contains(@data-task,'task1')]")
task2 = driver.find_element("xpath", "//*[contains(@data-task,'task2')]")
task3 = driver.find_element("xpath", "//*[contains(@data-task,'task3')]")
task4 = driver.find_element("xpath", "//*[contains(@data-task,'task4')]")

to_do = driver.find_element("xpath", "//*[@id='todoContainer']")
in_progress = driver.find_element("xpath", "//*[@id='progressContainer']")
done = driver.find_element("xpath", "//*[@id='doneContainer']")


ActionChains(driver).drag_and_drop(task1, in_progress).perform()
ActionChains(driver).drag_and_drop(task1, done).perform()
ActionChains(driver).drag_and_drop(task4, to_do).perform()
ActionChains(driver).drag_and_drop(task4, done).perform()
ActionChains(driver).drag_and_drop(task2, done).perform()
ActionChains(driver).drag_and_drop(task3, done).perform()

tasks_in_done = driver.find_elements("xpath", "//*[@id='doneContainer']//*[contains(@class,'task-card')]")
task_ids = [t.get_attribute("data-task") for t in tasks_in_done]
assert len(task_ids) == 5
