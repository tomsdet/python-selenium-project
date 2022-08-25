from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
# seckin_madde_alani = driver.find_element(By.ID, "mp-tfa")
# seckin_madde_yazisi = seckin_madde_alani.text
# seckin_madde_yazisi = seckin_madde_yazisi.split(",")[0]
# print("seckin madde: "+ seckin_madde_yazisi)
# kaliteli_madde = driver.find_element(By.ID, "mf-tfp").text
# kaliteli_madde = kaliteli_madde.split(",")[0]
# print("kaliteli madde: "+kaliteli_madde)
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("test")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
mesaj = driver.find_element(By.ID, "flash").text
print("Mesaj: "+mesaj)
if "username is invalid" in mesaj:
    print("OK")
else:
    print("Hata")
driver.quit()
