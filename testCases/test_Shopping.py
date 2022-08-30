import time

import pytest
import selenium.webdriver.firefox.firefox_binary
from selenium import webdriver
from pageObjects.loginPage import Login
import os
import string
import random
from Utilities.readProperties import ReadConfig
from pageObjects.shoppingPage import Shopping
from selenium.webdriver.common.by import By


class Test_002_Shopping():

    baseURL = ReadConfig.getURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    def test_shopping(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.loginBTNclick()

        self.shopping = Shopping(self.driver)
        self.shopping.addBackpack()
        self.shopping.addBikeLight()
        self.shopping.addTshirt()
        self.shopping.addJacket()
        self.shopping.addOnesie()
        self.shopping.addRedTshirt()

        time.sleep(1.2)
        self.shopping.removeJacket()
        self.shopping.removeBikeLight()

        self.shopping.cartClick()
        self.shopping.checkout()
        self.shopping.firstName_checkOut('Davud')
        self.shopping.lastName_checkOut('Gobeljic')
        self.shopping.postalCode_checkout('71000')

        self.shopping.continue_checkout()
        self.shopping.finish()

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if 'THANK YOU FOR YOUR ORDER' in self.msg:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False
