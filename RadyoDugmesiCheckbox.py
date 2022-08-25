from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://tomspizzeria.herokuapp.com/")
orta_boy = driver.find_element(By.CSS_SELECTOR, "input[value='Orta']")
zeytin = driver.find_element(By.CSS_SELECTOR, "input[value='zeytin']")
mantar = driver.find_element(By.CSS_SELECTOR, "input[value='mantar']")
print(orta_boy.is_selected())
print(zeytin.is_selected())
print(mantar.is_selected())
orta_boy.click()
zeytin.click()
mantar.click()
print(orta_boy.is_selected())
print(zeytin.is_selected())
print(mantar.is_selected())
# driver.quit()
