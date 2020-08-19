# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 23:51:04 2020

@author: Tejas
"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logindata

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('F:\Channel\webdriver\chromedriver.exe', chrome_options=options)
action = ActionChains(driver)
time.sleep(1)


driver.get('http://www.amazon.in')
time.sleep(3)
 
firstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span/span')
action.move_to_element(firstLevelMenu).perform()
time.sleep(3)
 
secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')
secondLevelMenu.click()
time.sleep(3)

signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')
signinelement.send_keys(logindata.USERNAME)
time.sleep(3)

cont = driver.find_element_by_xpath('//*[@id="continue"]')
cont.click()
time.sleep(3)

passwordelement = driver.find_element_by_xpath('//*[@id="ap_password"]')
passwordelement.send_keys(logindata.PASSWORD)
time.sleep(3)

login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
login.click()
time.sleep(3)

'----------------------------X-------------------------X------------------------------------------------'

searchbar = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
searchbar.send_keys('3s 20a battery charging board')
searchbar.send_keys(Keys.ENTER)
time.sleep(3)

mainpage = driver.find_element_by_css_selector('div.sg-col-20-of-24')
listofproducts = mainpage.find_elements_by_css_selector('div.s-include-content-margin')
for item in listofproducts:
    try:
        item.find_element_by_css_selector('div.a-row')
        ans = True
    except:
        ans = False

    if(ans):
        item.find_element_by_css_selector('span.a-size-medium').click()
        break

driver.switch_to_window(driver.window_handles[1]) ##used to switche between tabs

addtocart = driver.find_element_by_xpath('//*[@id="add-to-cart-button"]')
addtocart.click()
time.sleep(3)

proceed = driver.find_element_by_xpath('//*[@id="hlb-ptc-btn-native"]')
proceed.click()
time.sleep(3)

