import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://tomspizzeria.herokuapp.com/iframe-demo.html")
# 1. iframe id
# 2. iframe name
# 3 index (0'dan basliyor')
driver.switch_to.frame(0)
driver.find_element(By.ID, "email").send_keys("brad.pitt@fil.com")
time.sleep(2)
# default_content => en ana sayfaya don,, sayfanin aslina don
# parent_frame => bir ustteki frame gecis icin
# 1. ana sayfa
#   2. frame 1
#      3 frame 2
driver.switch_to.default_content()
driver.find_element(By.ID, "isim").send_keys("angelina.jolie@film.com")
time.sleep(2)

driver.quit()