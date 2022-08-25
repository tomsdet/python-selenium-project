import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

buton2 = driver.find_element(By.XPATH, "(//button)[3]")
buton2.click()
WebDriverWait(driver, 3).until(expected_conditions.alert_is_present())
alert = Alert(driver)
time.sleep(1)
mesaj = alert.text
alert.send_keys("selenium alert test")
time.sleep(2)
alert.accept()

result = driver.find_element(By.ID, "result").text
print("mesaj: "+mesaj)
print("sonuc: "+result)
driver.switch_to.default_content()
driver.quit()