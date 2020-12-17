import pytest
from pageObjects.ArticlesPage import articlePage
from utilities.ReadProperties import readConfig
from Configurations.BasicClassConfig import basic
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Test_HomePageSuite(basic):
    URL = readConfig.URLHome()

    #This fixture sets up and driver, goes to inital URL of test, and initiates ActionChains,
    # and initiailizes the POM class(es) for the tests
    @pytest.fixture
    def additionalSetup(self, setupandteardown):
        self.driver = setupandteardown
        self.driver.get(self.URL)
        self.action = ActionChains(self.driver)
        self.ap = articlePage(self.driver)


    def test_0001(self, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0001: Verify Text of 3 Banners is Present***')
