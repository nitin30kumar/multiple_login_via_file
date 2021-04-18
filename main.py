import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://onlinenotessharing.epizy.com")

#open file and read lines
file_to_login = open('login.txt', 'r')
Lines = file_to_login.readlines()

#read string before and after : symbol
count=0
for line in Lines:
    count+=1

    #string before and after : symbol
    usrnm = line.partition(':')

    # click on button to login
    driver.find_element_by_link_text('Login').click()

    # put username
    time.sleep(1)
    driver.find_element_by_name('user').clear()
    driver.find_element_by_name('user').send_keys(usrnm[0])

    # put password
    time.sleep(1)
    driver.find_element_by_name('pass').clear()
    driver.find_element_by_name('pass').send_keys(usrnm[2])

    try:
        # login credentials wrong then alert box is encountered
        alert = driver.switch_to.alert
        alert.accept()
        print("Attempt",count,":Invalid login credentials:", usrnm[0], "and", usrnm[2])

    except:
        # login credentials correct, no alert box, just naviagted to dashboard
        print("Attempt",count,":Logged in successful with following credentials:", usrnm[0], "and", usrnm[2])
        driver.back()

time.sleep(5)
driver.quit()