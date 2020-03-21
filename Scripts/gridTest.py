'''
Created on Mar 17, 2020

@author: Mary
'''
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from asyncio.tasks import wait_for
from json import load
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


desiredCapabilities={
"browserName":"chrome"
}

driver = webdriver.Remote(command_executor='http://192.168.126.1:4444/wd/hub',desired_capabilities = desiredCapabilities)
driver.get("https://www.nike.com")
driver.find_element_by_xpath("//button[@id='MobileMenuToggle']/i").click()
driver.find_element_by_xpath("//li[@id='MobileAccountMenuHeader']/button[2]/span").click()
driver.find_element_by_name("emailAddress").clear()
driver.find_element_by_name("emailAddress").send_keys("marylewellyn@msn.com")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("homerMaple11**")
driver.find_element_by_xpath("//div[6]/input").click()
driver.close()
print("you have connected to the grid")
driver.quit()