# -*- coding: utf-8 -*-
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

class Nike(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.nike.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_nike(self):
        driver = self.driver
        driver.get("https://www.nike.com/")
        #self.driver.implicitly_wait(5)
        driver.find_element_by_xpath("//button[@id='MobileMenuToggle']/i").click()
        driver.find_element_by_xpath("//li[@id='MobileAccountMenuHeader']/button[2]/span").click()
        driver.find_element_by_name("emailAddress").clear()
        driver.find_element_by_name("emailAddress").send_keys("marylewellyn@msn.com")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("homerMaple11**")
        driver.find_element_by_xpath("//div[6]/input").click()
        driver.close()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
