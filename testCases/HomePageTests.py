import inspect
import pytest
from datetime import datetime
from selenium import webdriver
from pageObjects.HomePage import homePage
from pageObjects.PrivacyPolicy import PrivacyPolicy
from utilities.ReadProperties import readConfig
from utilities.CustomLogger import LogGen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Test_HomePageSuite:
    URL = readConfig.URLHome()
    logger = LogGen.loggen()
    defName = (inspect.stack()[0][3])

    @pytest.fixture
    def additionalSetup(self, setupandteardown):
        self.driver = setupandteardown
        self.driver.get(self.URL)
        self.hp = homePage(self.driver)
        self.action = ActionChains(self.driver)


    def test_0001(self, additionalSetup):
        self.counter = 0
        self.src = self.driver.page_source

        self.logger.info(f'***{self.defName}: test_0001: Verify Text of 3 Banners is Present***')

        if self.hp.slider1text in self.src:
            self.logger.info("Slider1 text present")

        else:
            self.logger.info("FAILED - Slider 1 Text did not match")
            self.counter +=1

        if self.hp.slider2text in self.src:
            self.logger.info("Slider2 text present")

        else:
            self.logger.info("FAILED - Slider 2 Text did not match")
            self.counter +=1

        if self.hp.slider3text in self.src:
            self.logger.info("Slider3 text present")

        else:
            self.logger.info("FAILED - Slider 3 Text did not match")
            self.counter +=1

        if self.counter == 0:
            self.logger.info("PASSED\n")

            assert True
        else:
            self.logger.info(f'FAILED - {self.counter} elements failed to verify.\n')
            assert False


    def test_0002(self, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0002: Open FAQ 1***')
        self.action.move_to_element(self.driver.find_element_by_xpath(self.hp.faq1list1)).click().perform()

        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.hp.faq1list1))
            )
            self.logger.info('Found the FAQ1 details')
            self.logger.info('PASSED\n')
            assert True


        except:
            self.logger.info(f'Could not locate ELEMENT by XPATH')
            self.logger.info(f'lp.FAQ1List XPATH = {self.hp.faq1list1}\n')
            assert False


    def test_0003(self, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0003: Footer Link***')
        self.action.move_to_element(self.driver.find_element_by_xpath(self.hp.privacypolicy)).click().perform()
        self.pp = PrivacyPolicy(self.driver)

        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.pp.paragraph))
            )

            self.logger.info('Found the Privacy Policy Page')
            self.logger.info('PASSED\n')
            assert True


        except:
            self.logger.info(f'Could not locate ELEMENT by XPATH')
            self.logger.info(f'pp.paragraph XPATH = {self.pp.paragraph}\n')
            assert False






