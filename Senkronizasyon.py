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
# driver.implicitly_wait(30)
# driver nesnesi ile calisiyor
driver.get("https://pynishant.github.io/Selenium-python-waits.html")

tryit = driver.find_element(By.XPATH, "//button[contains(text(), 'Try it')]").click()

WebDriverWait(driver, 45).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'CLICK ME')]")))
clickme = driver.find_element(By.XPATH, "//button[contains(text(), 'CLICK ME')]").click()
WebDriverWait(driver, 3).until(expected_conditions.alert_is_present())
uyari = Alert(driver)
time.sleep(1)
uyari.accept()

# presence vs visibility
# implicit wait - gizli bekleme
# explicit wait - aciktan bekleme
# fluent wait
driver.quit()