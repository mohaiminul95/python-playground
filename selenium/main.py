from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# driver config
webdriver_path = "/media/rabid/Development/PYTHON/python-playground/selenium/chromedriver/chromedriver"
service = Service(webdriver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

# site url
driver.get('https://sims.technometrics.net')

# admin access
email = "admin@sims.net"
password = 12345678

app_email = driver.find_element_by_id('login-email')
app_password = driver.find_element_by_id('login-password')
app_email.send_keys(email)
app_password.send_keys(password)

loginBtn = driver.find_element_by_class_name('waves-light')
loginBtn.click()

time.sleep(15)
driver.close()
