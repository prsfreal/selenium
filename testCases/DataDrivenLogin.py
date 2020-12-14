import pytest
import time
import openpyxl
from selenium import webdriver
from pageObjects.HomePage import homePage
from pageObjects.LoginPage import loginPage
from utilities.ReadProperties import readConfig
from utilities.CustomLogger import LogGen
from utilities import ExcelUtilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Test_002_DDT_Login:
    baseURL = readConfig.BaseURL()
    logger = LogGen.loggen()
    dataPath = './TestData/data.xlsx'

    def test_login_DDT(self, setup):
        self.logger.info('test_login_DDT')
        self.driver = setup
        self.driver.get(self.baseURL)

        status = []
        self.rows = ExcelUtilities.getRowCount(self.dataPath, 'Sheet1')
        self.columns = ExcelUtilities.getColumnCount(self.dataPath, 'Sheet1')


        self.hp = homePage(self.driver)
        self.hp.navigateToAccountPage()



        self.counter = 1
        try:
            self.logger.info('Entered the top level TRY')
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, loginPage.userNameField))
            )
            self.lp = loginPage(self.driver)

            for i in range(2, self.rows+1):
                self.logger.info(f'Entered the FOR loop for the --{self.counter}-- time')
                self.counter += 1
                self.user = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 1)
                self.password = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 2)
                self.expected = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 3)
                self.lp.setUserName(self.user)
                self.lp.setPassword(self.password)
                self.lp.clickLogin()


                try:
                    self.logger.info(f'Entered the login attempt TRY for the --{self.counter}-- time')
                    WebDriverWait(self.driver, 3).until(
                        EC.presence_of_element_located((By.XPATH, loginPage.displayName))
                    )

                    if self.expected == 'pass':
                        self.logger.info('Passed a data driven test')
                        status.append('Pass')

                    elif self.expected == 'fail':
                        self.logger.info('Incorrect login = FAIL')
                        status.append('Fail')

                    self.lp.clickLogout()

                except:
                    self.logger.info(f'Invalid login could not find(Correct) ={loginPage.displayName}')


                try:

                    WebDriverWait(self.driver, 3).until(
                        EC.presence_of_element_located((By.XPATH, loginPage.confirmLogout))
                    )
                    self.logger.info('This TRY is only entered with correct login #1')
                    self.lp.clickConfirm()

                except:
                    self.logger.info(f'Invalid login could not find(Correct) ={loginPage.confirmLogout}')


                try:

                    WebDriverWait(self.driver, 3).until(
                        EC.presence_of_element_located((By.XPATH, loginPage.loginErrorMessage))
                    )
                    self.logger.info('This TRY is the bad login attempt --{self.counter}-- time')
                    if self.expected == 'fail':
                        self.logger.info('Failed to login = PASS')
                        status.append('Pass')

                    elif self.expected == 'pass':
                        self.logger.info('Incorrect login = FAIL')
                        status.append('Fail')


                except:
                    self.logger.info(f'Successful Login')

                self.logger.info(f'{status}')


        except:
            self.logger.info(f'Could not locate userNameField ={loginPage.userNameField} on the Account Page')
            self.driver.close()

        if 'Fail' not in status:
            self.logger.info(status)
            print(status)
            assert True
        else:
            self.logger.info(status)
            assert False

        self.driver.quit()
