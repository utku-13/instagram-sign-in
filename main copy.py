from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USER_NAME = "mail"
PASSWORD = "password"



path = "/Users/utkuozer/chromedriver"

optns = webdriver.ChromeOptions()
optns.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=optns,service=Service(executable_path=path,log_path="NUL"))

driver.get("https://www.instagram.com/")

#lang_sel = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
#lang_sel.click()
#print(lang_sel.text)

#lang_sel = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
#lang_sel.click()
#print(lang_sel.text)

user_name_enter = driver.find_element(By. XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
user_name_enter.send_keys(USER_NAME)


password_enter = driver.find_element(By. XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
password_enter.send_keys(PASSWORD)

login_button = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
login_button.click()

#INSTAGRAM SIGN IN.


