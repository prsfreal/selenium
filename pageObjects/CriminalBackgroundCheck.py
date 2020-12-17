from selenium.webdriver.common.action_chains import ActionChains
import time

class criminalBackgroundCheckPage():

    federalCourtButton = '//*[@id="post-2219"]/div/div/div/div/section[4]/div[2]/div/div/div/div/section/div/div/div[1]/div/div/div/div/div/div[3]/a'




    def __init__(self, driver):
        self.driver = driver


    def navigateToFederalCourt(self):
        self.action = ActionChains(self.driver)
        self.action.move_to_element(self.driver.find_element_by_xpath(self.federalCourtButton))
        self.action.click(self.driver.find_element_by_xpath(self.federalCourtButton))
        self.action.perform()
        time.sleep(1)