import pytest
from pageObjects.ArticlesArchivePage import articleArchivePage
from pageObjects.ArticlePage import articlePage
from pageObjects.CriminalBackgroundCheck import criminalBackgroundCheckPage
from pageObjects.FederalLanding import federalLandingPage
from utilities.ReadProperties import readConfig
from Configurations.BasicClassConfig import basic
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



class Test_HomePageSuite(basic):
    URL = readConfig.URLArticles()

    #This fixture sets up and driver, goes to initial URL of test, initiates ActionChains,
    # and initializes the POM class(es) for the tests
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
        self.logger.info('Now in second window')

        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.ap.emailfield))
            )
            self.ap.signIntoTwitter()
            self.logger.info('Signed into twitter but did not send the tweet. Just requires one more command.')
            assert True


        except:
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'ap.tweetfield XPATH = {self.ap.tweetfield}\n')
            assert False





    def test_0002(self, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0002: Sign up for discount***')
        self.aap.navigateToArticle1()


        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.ap.discountname))
            )

            self.ap.discountsubmit()

        except:
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'ap.discountname XPATH = {self.ap.discountname}\n')
            assert False

        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.ap.discountverifypath))
            )
            self.src = self.driver.page_source
            if self.ap.discountverifytext in self.src:
                self.logger.info('PASSED')
                assert True
            else:
                self.logger.info('Could not find verify text.')
                assert False

        except:
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'ap.discountverifypath XPATH = {self.ap.discountverifypath}\n')
            assert False



