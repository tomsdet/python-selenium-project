import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/upload")

file = "/Users/tom/PycharmProjects/SeleniumDemoProject/chromedriver"

upload_file = driver.find_element(By.ID, "file-upload")
time.sleep(2)
upload_file.send_keys(file)

driver.find_element(By.ID, "file-submit").click()

WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.TAG_NAME, "h3")))

baslik = driver.find_element(By.TAG_NAME, "h3").text

print(baslik)

dosya = driver.find_element(By.ID, "uploaded-files").text

print(dosya)
time.sleep(2)

driver.quit()
