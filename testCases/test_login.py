import pytest
import time
from selenium import webdriver
from pageObjects.HomePage import homePage
from pageObjects.LoginPage import loginPage
from utilities.ReadProperties import readConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Test_001_Login:
    baseURL = readConfig.BaseURL()
    userName = readConfig.username()
    password = readConfig.password()
    logger = LogGen.loggen()

    def test_homepage_nav_to_account_page(self, setup):
        self.driver = setup
        self.logger.info('**********Test_001_Login**********')
        self.logger.info("**********Navigate from homepage to Account**********")
        self.driver.get(self.baseURL)
        title = self.driver.title
        self.hp = homePage(self.driver)
        self.hp.navigateToAccountPage()

        if title == 'Home | Validate Services':
            self.logger.info("**********PASSED**********")
            self.driver.close()
            assert True
        else:
            self.logger.error('**********FAILED**********')
            self.driver.save_screenshot('./Screenshots/adsfg.png')
            self.driver.close()
            assert False




    '''def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.hp = homePage(self.driver)
        self.hp.navigateToAccountPage()


        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, loginPage.userNameField))
            )
            title = self.driver.title
            self.lp = loginPage(self.driver)
            self.lp.setUserName(self.userName)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

        except:
            self.logger.info(f'Could not locate userNameField ={loginPage.userNameField}')
            self.driver.close()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, loginPage.logoutButton))
            )
            self.lp.clickLogout()

        except:
            self.logger.info(f'Could not locate logoutButton ={loginPage.logoutButton}')
            self.driver.close()


        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, loginPage.confirmLogout))
            )
            self.lp.clickConfirm()
            self.driver.close()

        except:
            self.logger.info(f'Could not locate confirmLogout ={loginPage.confirmLogout}')
            print('what am i doing here')
            self.driver.close()


        if title == 'My Account | Validate Services':
            self.logger.info("**********PASSED**********")
            assert True
        else:
            self.logger.info("**********FAILED**********")
            assert False'''


