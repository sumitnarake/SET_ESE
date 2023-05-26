# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test1(self):

    self.driver.get("https://github.com/")
   
    self.driver.set_window_size(945, 742)
     
    self.driver.find_element(By.CSS_SELECTOR, ".dropdown-caret:nth-child(3)").click()
    
    self.driver.find_element(By.LINK_TEXT, "Your repositories").click()
   
    self.driver.find_element(By.LINK_TEXT, "SET_ESE").click()
   
    self.driver.find_element(By.CSS_SELECTOR, ".Button--primary .Button-label").click()
    
    self.driver.find_element(By.LINK_TEXT, "Download ZIP").click()


test = TestTest1()
test.setup_method(None)
test.test_test1()
test.teardown_method(None)
