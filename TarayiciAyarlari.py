import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

service = Service("./chromedriver")
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-infobars")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--disable-notifications")
options.add_argument("--disable-save-password")
options.add_argument("--disable-extensions")
options.add_argument("download.default_directory=C:/kullanicilar/ali/test")
options.add_argument("--window-size=768,1024")
options.add_argument("--disable-popup-blocking")
driver = webdriver.Chrome(service=service, options=options)
# driver.maximize_window()
driver.implicitly_wait(10)
# driver.get("http://www.google.com")
driver.get("https://www.ucuzabilet.com")
time.sleep(2)
driver.quit()