import pytest
from selenium import webdriver
from pageObjects.loginPage import Login
import os
import string
import random
from Utilities.readProperties import ReadConfig
from selenium.webdriver.chrome.service import Service

class Test_001_login():
    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    def test_homePage(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == 'Swag Labs':
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False


    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.loginBTNclick()
        act_title = self.driver.title
        if act_title == 'Swag Labs':
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False



