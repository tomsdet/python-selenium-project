import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demoqa.com/droppable/")

kaynak = driver.find_element(By.CSS_SELECTOR, "div#simpleDropContainer div")
hedef = driver.find_element(By.CSS_SELECTOR, "div#simpleDropContainer div.drop-box")

print("Once: "+hedef.text)
action = ActionChains(driver)
action.drag_and_drop(kaynak, hedef).perform()
time.sleep(2)
print("Sonra: "+hedef.text)
time.sleep(2)
driver.quit()
