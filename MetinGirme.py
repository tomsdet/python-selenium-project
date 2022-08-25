import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("http://tr.wikipedia.org")
# aramakutusu = driver.find_element(By.NAME, "search")
# aramakutusu.send_keys("Ay")
# print("bekleme basladi")
# time.sleep(1.0)
# print("bekleme bitti")
# # aramakutusu.send_keys(Keys.ENTER)
# # driver.find_element(By.XPATH, "//form[@id='searchform']//*[contains(text(), 'Ara')]").click()
# driver.find_element(By.CSS_SELECTOR, "form#searchform button").click()
# birinci_baslik = driver.find_element(By.ID, "firstHeading").text
# print("Ilk Baslik: " + birinci_baslik)
# driver.find_element(By.XPATH, "//a[text()='Dünya']").click()
# ikinci_baslik = driver.find_element(By.ID, "firstHeading").text
# print("Ikinci baslik: "+ikinci_baslik)
driver.quit()



