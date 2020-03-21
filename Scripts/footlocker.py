# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from django.test import LiveServerTestCase
from nose_parameterized import parameterized
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class Footlocker2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://footlocker.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_footlocker2(self):
        driver = self.driver
        driver.get("https://www.footlocker.com/")
        driver.find_element_by_xpath("//div[@id='app']/div/header/nav[2]/div[3]/button[3]/span").click()
        driver.find_element_by_css_selector("div.c-header-navigation-drawer__user > button.Link.Link-underline").click()
        driver.find_element_by_id("input_email_uid").clear()
        driver.find_element_by_id("input_email_uid").send_keys("marylewellyn@msn.com")
        driver.find_element_by_id("input_password_password").clear()
        driver.find_element_by_id("input_password_password").send_keys("homerMaple11**")
        driver.find_element_by_xpath("//form[@id='SignIn']/ul/li[3]/button").click()
        #driver.find_element_by_xpath("//div[@id='app']/div/header/nav[2]/div[3]/a[2]/span").click()
        driver.find_element_by_link_text("Checkout").click()
        driver.find_element_by_id("input_tel_cardNumber").click()
        driver.find_element_by_id("input_tel_cardNumber").clear()
        driver.find_element_by_id("input_tel_cardNumber").send_keys("44565556666")
        Select(driver.find_element_by_id("select_expiryMonth")).select_by_visible_text("01")
        Select(driver.find_element_by_id("select_expiryMonth")).select_by_visible_text("02")
        Select(driver.find_element_by_id("select_expiryYear")).select_by_visible_text("20")
        Select(driver.find_element_by_id("select_expiryYear")).select_by_visible_text("21")
        driver.find_element_by_id("input_tel_CSC").clear()
        driver.find_element_by_id("input_tel_CSC").send_keys("554")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_xpath("//form[@id='Payment']/div[4]/label/span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_local | ]]
    
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
