from selenium import webdriver
from selenium.webdriver.common.by import By

class Login:
    username_id = 'user-name'
    password_id = 'password'
    loginBTN = 'login-button'
    logout_id = 'logout_sidebar_link'

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.username_id).clear()
        self.driver.find_element(By.ID, self.username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.password_id).clear()
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def loginBTNclick(self):
        self.driver.find_element(By.ID, self.loginBTN).click()

    def logOutBTNclick(self):
        self.driver.find_element(By.ID, self.logout_id).click()


