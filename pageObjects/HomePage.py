from selenium.webdriver.common.action_chains import ActionChains
import time

class homePage():

    account = '//*[@id="menu-item-3492"]/a'

    def __init__(self, driver):
        self.driver = driver

    def navigateToAccountPage(self):
        self.action = ActionChains(self.driver)
        self.action.move_to_element(self.driver.find_element_by_xpath(self.account))
        self.action.click(self.driver.find_element_by_xpath(self.account))
        self.action.perform()
        time.sleep(1)
        print('done')



