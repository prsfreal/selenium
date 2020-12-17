from selenium.webdriver.common.action_chains import ActionChains
import time
from decouple import config
from utilities.ReadProperties import readConfig

class federalCheckoutPage():

    orderfirstname = '//*[@id="billing_first_name"]'
    orderlastname = '//*[@id="billing_last_name"]'
    orderaddress = '//*[@id="billing_address_1"]'
    ordercity = '//*[@id="billing_city"]'
    orderstate = '//*[@id="billing_state"]'
    orderzip = '//*[@id="billing_postcode"]'
    orderphone = '//*[@id="billing_phone"]'
    orderemail = '//*[@id="billing_email"]'
    ordercontractorname = '//*[@id="billing_contractors_name"]'
    ordercontractoremail = '//*[@id="billing_contractors_email_address"]'
    orderbutton = '//*[@id="post-3291"]/div/div/div/div/section[8]/div/div/div/div/div/div[3]/div/div/a/span/span'

    user1 = [readConfig.firstname(), readConfig.lastname(), readConfig.address(),readConfig.city(),
             readConfig.state(), readConfig.zip(), readConfig.phone(), readConfig.email(),
             readConfig.contractorname(), readConfig.contractoremail()]

    def __init__(self, driver):
        self.driver = driver

    def makePurchase(self):

        self.driver.find_element_by_xpath(self.orderfirstname).clear().send_keys(self.user1[0])
        self.driver.find_element_by_xpath(self.orderlastname).clear().send_keys(self.user1[1])
        self.driver.find_element_by_xpath(self.orderaddress).clear().send_keys(self.user1[2])
        self.driver.find_element_by_xpath(self.ordercity).clear().send_keys(self.user1[3])
        self.driver.find_element_by_xpath(self.orderstate).clear().send_keys(self.user1[4])
        self.driver.find_element_by_xpath(self.orderzip).clear().send_keys(self.user1[5])
        self.driver.find_element_by_xpath(self.orderphone).clear().send_keys(self.user1[6])
        self.driver.find_element_by_xpath(self.orderemail).clear().send_keys(self.user1[7])
        self.driver.find_element_by_xpath(self.ordercontractorname).clear().send_keys(self.user1[8])
        self.driver.find_element_by_xpath(self.ordercontractoremail).clear().send_keys(self.user1[9])
        self.driver.find_element_by_xpath(self.orderbutton).click()