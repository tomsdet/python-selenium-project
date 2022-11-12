import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.ucuzabilet.com")

nereden = driver.find_element(By.ID, "from_text")
nereden.send_keys("avust")
time.sleep(2)
graz = driver.find_element(By.XPATH, "//li[contains(text(), 'GRZ')]")
graz.click()

time.sleep(2)
driver.quit()