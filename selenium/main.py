from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# driver config
webdriver_path = "/media/rabid/Development/PYTHON/python-playground/selenium/chromedriver/chromedriver"
service = Service(webdriver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

# site url
driver.get('https://www.techwithtim.net/')

search = driver.find_element(By.NAME, "s")
search.send_keys('test')
search.send_keys(Keys.RETURN)

# GET CONTENTS
posts = []
try:
    body = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "page"))
    )
    articles = body.find_elements(By.TAG_NAME, "article")
    for article in articles:
        post_time = article.find_element(By.CLASS_NAME, 'entry-meta').text
        post_content = article.find_element(By.CLASS_NAME, 'entry-summary').text
        posts.append({'time' : post_time, 'content' : post_content})  
except:
    driver.quit()

result = {'count' : len(posts), 'posts' : posts}    
print(json.dumps(result, indent=4))

time.sleep(7)
driver.close()
