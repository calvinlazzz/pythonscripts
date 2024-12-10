# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service = Service('/Users/calvin.la/Downloads/chromedriver-mac-arm64')
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt
def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome( options=options)
  driver.get("http://automated.pythonanywhere.com/login")
  return driver

def clean_text(text):
    
    output = float(text.split(": ")[1])
    return output

def write_file(text):
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open("output.txt", "w") as file:
        file.write(text)
def main():
  driver = get_driver()
  driver.find_element(by='id', value='id_username').send_keys('automated')
  time.sleep(1)
  driver.find_element(by= 'id', value='id_password').send_keys('automatedautomated'+ Keys.RETURN)
  time.sleep(1)
  driver.find_element(by='xpath', value = '/html/body/nav/div/a').click()
  time.sleep(2)
  while True:
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    text = str(clean_text(element.text))
    write_file(text)

print(main())