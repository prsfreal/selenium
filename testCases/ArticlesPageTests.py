import pytest
import time
from pageObjects.ArticlesArchivePage import articleArchivePage
from pageObjects.ArticlePage import articlePage
from utilities.ReadProperties import readConfig
from Configurations.BasicClassConfig import basic
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Test_HomePageSuite(basic):
    URL = readConfig.URLArticles()

    #This fixture sets up and driver, goes to inital URL of test, and initiates ActionChains,
    # and initiailizes the POM class(es) for the tests
    @pytest.fixture
    def additionalSetup(self, setupandteardown):
        self.driver = setupandteardown
        self.driver.get(self.URL)
        self.action = ActionChains(self.driver)
        self.aap = articleArchivePage(self.driver)
        self.ap = articlePage(self.driver)



    def test_0001(self, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0001: Send a tweet***')
        self.aap.navigateToArticle1()

        try:
            self.logger.info('i should wait for the page to reload')
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.ap.twitterwidget))
            )

            self.ap.navigateToTwitter()

        except:
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'ap.twitterwidget XPATH = {self.ap.twitterwidget}\n')
            assert False

        window1 = self.driver.window_handles[1]

        self.driver.switch_to_window(window1)

        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.ap.emailfield))
            )
            self.logger.info('did i send the keys')
            self.ap.signIntoTwitter()
            time.sleep(5)
            assert True


        except:
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'ap.twitterenterfield XPATH = {self.ap.emailfield}\n')
            assert False





    '''def test_0002(self, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0002: Sign up for discount***')


    def test_0003(self, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0003: Purchase BackgroundCheck***')'''
