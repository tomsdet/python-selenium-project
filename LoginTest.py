from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# test otomasyon
# test: beklentileri karsiliyormu
# 1. istenileni yapiyormu? pozitf test 2. istenmiyeni yapiyormu negatif

# internett login sayfasina git https://the-internet.herokuapp.com/login
# driver.get("https://the-internet.herokuapp.com/login")
# # kullanici adi gir
# driver.find_element(By.ID, "username").send_keys("test")
# #sifre gir
# driver.find_element(By.ID, "password").send_keys("asdf")
# # log in dugmesine tikla
# driver.find_element(By.CSS_SELECTOR, "button.radius").click()
# # yanlis kullanici adi Your username is invalid!
# mesaj = driver.find_element(By.ID, "flash").text
#
# if "Your username is invalid!" in mesaj:
#     print("OK, yanlis kullanici adi dogru calisiyor")
# else:
#     print("HATA: yanlis kullanici adi calismiyor")
#
# # yanlis sifre girince: Your password is invalid!
# driver.get("https://the-internet.herokuapp.com/login")
# driver.find_element(By.ID, "username").send_keys("tomsmith")
# driver.find_element(By.ID, "password").send_keys("asdf")
# driver.find_element(By.CSS_SELECTOR, "button.radius").click()
# mesaj2 = driver.find_element(By.ID, "flash").text
# print("Yanlis sifre mesaji: " + mesaj2)
# if "Your password is invalid!" in mesaj2:
#     print("OK, yanlis sifre adi dogru calisiyor")
# else:
#     print("HATA: yanlis sifre  calismiyor")
#
# # ikisi de dogru ise: mesaj: You logged into a secure area! link secure icerecek   sayfa da secure area
#
# driver.get("https://the-internet.herokuapp.com/login")
# driver.find_element(By.ID, "username").send_keys("tomsmith")
# driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
# driver.find_element(By.CSS_SELECTOR, "button.radius").click()
# mesaj3 = driver.find_element(By.ID, "flash").text
# print("Mesaj 3: "+mesaj3)
# if "You logged into a secure area!" in mesaj3:
#     print("OK, dogru bilgiler kullanici adi dogru calisiyor")
# else:
#     print("HATA: dogru bilgiler calismiyor")
#
# link = driver.current_url
# if "secure" in link:
#     print("OK link secure iceriyor")
# else:
#     print("HATA: link secure icermiyor")
#
# dogru_mesaj = driver.find_element(By.CSS_SELECTOR, "h2").text
# print("dogru mesaj: "+dogru_mesaj)
# if "Secure Area" in dogru_mesaj:
#     print("OK, Sayfa basligi dogru")
# else:
#     print("HATA: sayfa basligi yanlis")
#
# #logout dugmesine tikla
# driver.find_element(By.XPATH, "//i[contains(text(),'Logout')]").click()
#
# # sayfa linkini dogrula
# if "login" in driver.current_url:
#     print("OK. login sayfasina donduk")
# else:
#     print("HATA: login sayfasina donmedi")






def login(username, password):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()
    mesaj = driver.find_element(By.ID, "flash").text
    return mesaj

mesaj = login("asdf", "xyz")
assert  "Your username invalid!" in mesaj
mesaj = login("tomsmith", "asdf")
assert "Your password is invalid!"  in mesaj
mesaj = login("tomsmith", "SuperSecretPassword!")
assert "You logged into a secure area!" in mesaj
link = driver.current_url
assert "secure" in link
driver.quit()