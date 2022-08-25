import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.apple.com")
time.sleep(1)
print(driver.title)
apple = driver.current_window_handle
driver.switch_to.new_window("tab")
driver.get("https://www.tesla.com")
time.sleep(2)
print(driver.title)
tesla = driver.window_handles[1]
driver.switch_to.window(apple)
print(driver.title)
time.sleep(2)
driver.switch_to.window(tesla)
print(driver.title)
time.sleep(2)
driver.switch_to.window(apple)
time.sleep(1)
driver.quit()





