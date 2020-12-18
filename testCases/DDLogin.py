import pytest
from pageObjects.HomePage import homePage
from pageObjects.LoginPage import loginPage
from utilities.ReadProperties import readConfig
from utilities import ExcelUtilities
from selenium.webdriver.common.action_chains import ActionChains
from Configurations.BasicClassConfig import basic


class Test_002_DDT_Login(basic):
    URL = readConfig.URLHome()
    dataPath = './TestData/data.xlsx'

    # This fixture sets up and driver, goes to initial URL of test, initiates ActionChains,
    # and initializes the POM class(es) for the tests
    @pytest.fixture
    def additionalSetup(self, setupandteardown):
        self.driver = setupandteardown
        self.driver.get(self.URL)
        self.action = ActionChains(self.driver)
        self.lp = loginPage(self.driver)
        self.hp = homePage(self.driver)

    def test_valid_logins(self, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0001: Purchase BackgroundCheck***')
        self.hp.navigateToAccountPage()


        try:
            self.rows = ExcelUtilities.getRowCount(self.dataPath, 'Sheet1')
            self.columns = ExcelUtilities.getColumnCount(self.dataPath, 'Sheet1')
            status = []
            self.counter = 1
            self.waitAndsee(self.lp.userNameField)

            for i in range(2, self.rows+1):
                self.user = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 1)
                self.password = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 2)
                self.expected = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 3)
                self.lp.setUserName(self.user)
                self.lp.setPassword(self.password)
                self.lp.clickLogin()

                try:
                    self.waitAndsee(self.lp.displayName)
                    self.logger.info(f'Test {self.counter} = PASS')
                    self.lp.clickLogout()
                    self.waitAndsee(self.lp.confirmLogout)
                    self.lp.clickConfirm()
                    status.append('Pass')

                except:
                    self.logger.info(f'Test {self.counter} = FAIL')
                    self.logger.info(f'ID:{self.user}   PASS:{self.password}')
                    status.append('Fail')

                self.logger.info(f'{status}')
                self.counter += 1


        except:
            self.logger.exception(f'--Could not locate ELEMENT by XPATH or Excel parameters are wrong.')
            assert False

        if 'Fail' not in status:
            self.logger.info(f'\n')
            assert True

        else:
            self.logger.info(f'\n')
            assert False

