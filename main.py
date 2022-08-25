# This is a sample Python script.
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# option = Options()
# option.add_argument("--disable-infobars")
# option.add_argument("start-maximized")
# option.add_argument("--disable-extensions")
# option.add_argument("--disable-notifications")
# option.add_argument("--disable-save-password");
# option.add_argument("--window-size=1920,1080");
# option.add_argument("--disable-popup-blocking")
# option.add_argument("--allow-running-insecure-content")
# option.add_argument("download.default_directory=C:/Downloads")

# https://peter.sh/experiments/chromium-command-line-switches/ list of options


service = Service("./chromedriver")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/hovers")
# driver.get("https://www.ucuzabilet.com/")
# driver.find_element(By.ID, "from_text").click()
# time.sleep(1)
# WebDriverWait(driver, 5).until(expected_conditions.alert_is_present())
# alert = Alert(driver)
# alert.dismiss()


user = driver.find_element(By.CSS_SELECTOR, "div.figure")
username = driver.find_element(By.CSS_SELECTOR, "div.figure h5")
link = driver.find_element(By.XPATH, "//a[text()='View profile']")

print(username.is_displayed())

print("username: "+username.text)

time.sleep(2)
action = ActionChains(driver)
action.move_to_element(user)
action.click(link)
action.drag_and_drop_by_offset()
action.drag_and_drop()
action.perform()

time.sleep(2)
print("---------")
# print(username.is_displayed())
#
# print("username: "+username.text)
# link.click()

time.sleep(2)
print(driver.current_url)
assert "users/1" in driver.current_url

driver.quit()












