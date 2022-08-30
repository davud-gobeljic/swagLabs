import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class Shopping():

    backpack_id = 'add-to-cart-sauce-labs-backpack'
    bikeLight_id = 'add-to-cart-sauce-labs-bike-light'
    tShirt_id = "add-to-cart-sauce-labs-bolt-t-shirt"
    jacket_id="add-to-cart-sauce-labs-fleece-jacket"
    onesie_id = "add-to-cart-sauce-labs-onesie"
    tshirtRed_id = "add-to-cart-test.allthethings()-t-shirt-(red)"

    bikeLightRemove_id = 'remove-sauce-labs-bike-light'
    jacketRemove_id = 'remove-sauce-labs-fleece-jacket'

    cart_xpath = "//a[@class='shopping_cart_link']"
    checkout_id = 'checkout'

    firstName_checkout_id = 'first-name'
    lastName_checkout_id = 'last-name'
    postalCode_checkout_id = 'postal-code'
    continue_checkout_id = 'continue'
    finishBTN_id = 'finish'


    def __init__(self, driver):
        self.driver = driver

    def addBackpack(self):
        self.driver.find_element(By.ID, self.backpack_id).click()

    def addBikeLight(self):
        self.driver.find_element(By.ID, self.bikeLight_id).click()

    def addTshirt(self):
        self.driver.find_element(By.ID, self.tShirt_id).click()

    def addJacket(self):
        self.driver.find_element(By.ID, self.jacket_id).click()

    def addOnesie(self):
        self.driver.find_element(By.ID, self.onesie_id).click()

    def addRedTshirt(self):
        self.driver.find_element(By.ID, self.tshirtRed_id).click()

    def removeBikeLight(self):
        self.driver.find_element(By.ID, self.bikeLightRemove_id).click()

    def removeJacket(self):
        self.driver.find_element(By.ID, self.jacketRemove_id).click()

    def cartClick(self):
        self.driver.find_element(By.XPATH, self.cart_xpath).click()

    def checkout(self):
        self.driver.find_element(By.ID, self.checkout_id).click()

    def continue_checkout(self):
        self.driver.find_element(By.ID, self.continue_checkout_id).click()

    def firstName_checkOut(self, firstname):
        self.driver.find_element(By.ID, self.firstName_checkout_id).clear()
        self.driver.find_element(By.ID, self.firstName_checkout_id).send_keys(firstname)

    def lastName_checkOut(self, lastname):
        self.driver.find_element(By.ID, self.lastName_checkout_id).clear()
        self.driver.find_element(By.ID, self.lastName_checkout_id).send_keys(lastname)

    def postalCode_checkout(self, postalcode):
        self.driver.find_element(By.ID, self.postalCode_checkout_id).clear()
        self.driver.find_element(By.ID, self.postalCode_checkout_id).send_keys(postalcode)

    def continueBTN_checkout(self):
        self.driver.find_element(By.ID, self.continue_checkout_id).click()

    time.sleep(3)

    def finish(self):
        self.driver.find_element(By.ID, self.finishBTN_id).click()




