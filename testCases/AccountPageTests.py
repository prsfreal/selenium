import pytest
from decouple import config
from pageObjects.HomePage import homePage
from pageObjects.LoginPage import loginPage
from utilities.ReadProperties import readConfig
from Configurations.BasicClassConfig import basic
from selenium.webdriver.common.action_chains import ActionChains


class Test_001_Login(basic):
    URL = readConfig.URLHome()
    userName = config('TESTID')
    password = config('PASSKEY')

    #This fixture sets up and driver, goes to initial URL of test, initiates ActionChains,
    # and initializes the POM class(es) for the tests
    @pytest.fixture
    def additionalSetup(self, setupandteardown):
        self.driver = setupandteardown
        self.driver.get(self.URL)
        self.action = ActionChains(self.driver)
        self.hp = homePage(self.driver)


    def test_0001(self, setupandteardown):
        self.logger.info(f'***{self.defName}: Login to Account and Logout***')
        self.driver = setupandteardown
        self.driver.get(self.URL)
        self.hp = homePage(self.driver)

        self.hp.navigateToAccountPage()

        try:
            self.waitAndsee(loginPage.userNameField)
            title = self.driver.title
            self.lp = loginPage(self.driver)
            self.lp.setUserName(self.userName)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()

        except:
            self.logger.info(f'Could not locate ELEMENT by XPATH')
            self.logger.info(f'lp.userNameField XPATH = {self.lp.userNameField}')
            assert False

        try:
            self.waitAndsee(self.lp.logoutButton)
            self.lp.clickLogout()

        except:
            self.logger.info(f'Could not locate ELEMENT by XPATH')
            self.logger.info(f'lp.logoutButton XPATH = {self.lp.logoutButton}')
            assert False

        try:
            self.waitAndsee(self.lp.confirmLogout)
            self.lp.clickConfirm()

        except:
            self.logger.info(f'Could not locate ELEMENT by XPATH')
            self.logger.info(f'lp.confirmLogout XPATH ={self.lp.confirmLogout}')
            assert False


        if title == 'My Account | Validate Services':
            self.logger.info('PASSED')
            assert True

        else:
            self.logger.error('FAILED')
            self.logger.error(f'Title = {title} NOT My Account | Validate Services')
            self.driver.save_screenshot(f'./Screenshots/{self.defName}.png')
            assert False


