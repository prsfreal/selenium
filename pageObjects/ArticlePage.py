from selenium.webdriver.common.action_chains import ActionChains
import time
from decouple import config

class articlePage():

    twitterwidget = '//*[@id="main"]/div/div/section[2]/div/div/div/div/div/div[2]/div/div/div[2]'
    emailfield = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div/div[1]/label/div/div[2]/div/input'
    passwordfield = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/form/div/div[2]/label/div/div[2]/div/input'
    loginbutton = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]/div/span/span/span'
    email = config('twitteremail')
    password = config('twitterpassword')

    def __init__(self, driver):
        self.driver = driver

    def navigateToTwitter(self):
        self.action = ActionChains(self.driver)
        self.action.move_to_element(self.driver.find_element_by_xpath(self.twitterwidget))
        self.action.click(self.driver.find_element_by_xpath(self.twitterwidget))
        self.action.perform()
        time.sleep(1)

    def signIntoTwitter(self):
        self.driver.find_element_by_xpath(self.emailfield).clear()
        self.driver.find_element_by_xpath(self.emailfield).send_keys(self.email)

        self.driver.find_element_by_xpath(self.passwordfield).clear()
        self.driver.find_element_by_xpath(self.passwordfield).send_keys(self.password)

        self.driver.find_element_by_xpath(self.loginbutton).click()










