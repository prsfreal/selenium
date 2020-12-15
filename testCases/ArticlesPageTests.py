import inspect
import pytest
from selenium import webdriver
from pageObjects.ArticlesPage import articlePage
from utilities.ReadProperties import readConfig
from utilities.CustomLogger import LogGen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Test_ArticlePageSuite:
    URL = readConfig.URLArticles()
    logger = LogGen.loggen()
    defName = (inspect.stack()[0][3])

    @pytest.fixture
    def additionalSetup(self, setupandteardown):
        self.driver = setupandteardown
        self.driver.get(self.URL)
        self.ap = articlePage(self.driver)
        self.action = ActionChains(self.driver)


    def test_0001(self, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0001: Verify Text of 3 Banners is Present***')
