import pytest
import time
import inspect
from decouple import config
from selenium import webdriver
from pageObjects.HomePage import homePage
from pageObjects.LoginPage import loginPage
from utilities.ReadProperties import readConfig
from utilities.CustomLogger import LogGen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime



class Test_001_Login:
    URL = readConfig.BaseURL1()
    userName = config('TESTID')
    password = config('PASSKEY')
    logger = LogGen.loggen()
    defName = (inspect.stack()[0][3])
    testStartTime = datetime.now().strftime('%m_%d_%Y_%I%M% %p')

    def test_0001(self, setupandteardown):
        self.logger.info(f'***{self.defName}: Navigate from Homepage to Account Page***')
        self.driver = setupandteardown
        self.driver.get(self.URL)
        self.hp = homePage(self.driver)
        self.hp.navigateToAccountPage()

        title = self.driver.title
        if title == 'My Account | Validate Services':
            self.logger.info("PASSED")
            assert True

        else:
            self.logger.error('FAILED')
            self.logger.error(f'Title = {title} NOT My Account | Validate Services')
            self.driver.save_screenshot(f'./Screenshots/{self.defName}_{self.testStartTime}.png')
            assert False




    def test_0002(self, setupandteardown):
        self.logger.info(f'***{self.defName}: Login to Account and Logout***')
        self.driver = setupandteardown
        self.driver.get(self.URL)

        self.hp = homePage(self.driver)
        self.hp.navigateToAccountPage()

        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, loginPage.userNameField))
            )
            title = self.driver.title
            self.lp = loginPage(self.driver)
            self.lp.setUserName(self.userName)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

        except:
            self.logger.info(f'Could not locate ELEMENT by XPATH')
            self.logger.info(f'lp.userNameField XPATH = {loginPage.userNameField}')
            assert False

        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, loginPage.logoutButton))
            )
            self.lp.clickLogout()

        except:
            self.logger.info(f'Could not locate ELEMENT by XPATH')
            self.logger.info(f'lp.logoutButton XPATH = {loginPage.logoutButton}')
            assert False


        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, loginPage.confirmLogout))
            )
            self.lp.clickConfirm()


        except:
            self.logger.info(f'Could not locate ELEMENT by XPATH')
            self.logger.info(f'lp.confirmLogout XPATH ={loginPage.confirmLogout}')
            assert False


        if title == 'My Account | Validate Services':
            self.logger.info('PASSED')
            assert True

        else:
            self.logger.error('FAILED')
            self.logger.error(f'Title = {title} NOT My Account | Validate Services')
            self.driver.save_screenshot(f'./Screenshots/{self.defName}.png')
            assert False


