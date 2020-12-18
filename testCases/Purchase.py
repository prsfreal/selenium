import pytest
from pageObjects.ArticlesArchivePage import articleArchivePage
from pageObjects.ArticlePage import articlePage
from pageObjects.CriminalBackgroundCheck import criminalBackgroundCheckPage
from pageObjects.FederalLanding import federalLandingPage
from pageObjects.FederalCheckout import federalCheckoutPage
from utilities.ReadProperties import readConfig
from Configurations.BasicClassConfig import basic
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
        self.cbc = criminalBackgroundCheckPage(self.driver)
        self.fl = federalLandingPage(self.driver)
        self.fc = federalCheckoutPage(self.driver)


    def test_0001(self, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0003: Purchase BackgroundCheck***')
        self.aap.navigateToArticle1()

        try:
            self.waitAndsee(self.ap.backgroundcheckbutton)
            self.ap.navigateToBackgroundCheck()

        except:
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'cbc.federalCourtButton XPATH = {self.ap.backgroundcheckbutton}\n')
            assert False

        try:
            self.waitAndsee(self.cbc.federalCourtButton)
            self.cbc.navigateToFederalCourt()

        except:
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'cbc.federalCourtButton XPATH = {self.cbc.federalCourtButton}\n')
            assert False

        try:
            self.waitAndsee(self.fl.startreportbutton)
            self.fl.navigateToPurchase()

        except:
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'fl.startreportbutton XPATH = {self.fl.startreportbutton}\n')
            assert False

        try:
            self.waitAndsee(self.fc.orderfirstname)
            #TODO enter in the user number from Configuration.Users.user
            self.fc.makePurchase(1)

        except:
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'fc.orderfirstname XPATH = {self.fc.orderfirstname}\n')
            assert False

        try:
            self.waitAndsee(self.fc.addonorderbutton, 'XPATH', 60)
            self.logger.info(f'PASSED')
            assert True

        except:
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'self.fc.addonorderbutton XPATH = {self.fc.addonorderbutton}\n')
            assert False