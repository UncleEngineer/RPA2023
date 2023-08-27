from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

path = r'C:\Users\Uncle Engineer\Desktop\RPA 2023\chromedriver.exe'
service = Service(path)

driver = webdriver.Chrome(service=service)
driver.get("https://uncle-tools.com/admin")

username = driver.find_element(By.NAME, 'username')
username.send_keys('uncle')
time.sleep(5)
password = driver.find_element(By.NAME, 'password')
password.send_keys('Admin12345')
password.send_keys(Keys.RETURN)
time.sleep(2)

url = 'https://uncle-tools.com/admin/myapp/product/add/'
driver.get(url)

fruit = [['มะม่วง', 30],['ทุเรียน', 40], ['องุ่น', 50]]

for i,j in fruit:
    name = driver.find_element(By.NAME, 'name')
    name.send_keys(i)
    time.sleep(5)
    price = driver.find_element(By.NAME, 'price')
    price.clear()
    price.send_keys(j)
    time.sleep(5)
    # save = driver.find_element(By.NAME, '_save')
    # save.click()

    saveadd = driver.find_element(By.NAME, '_addanother')
    saveadd.click()
    time.sleep(5)

time.sleep(60)
driver.quit()