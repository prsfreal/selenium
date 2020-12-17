import pytest
from pageObjects.ArticlesArchivePage import articleArchivePage
from pageObjects.ArticlePage import articlePage
from pageObjects.CriminalBackgroundCheck import criminalBackgroundCheckPage
from pageObjects.FederalLanding import federalLandingPage
from pageObjects.FederalCheckout import federalCheckoutPage
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
        self.cbc = criminalBackgroundCheckPage(self.driver)
        self.fl = federalLandingPage(self.driver)
        self.fc = federalCheckoutPage(self.driver)



    def test_0001(self, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0003: Purchase BackgroundCheck***')
        self.aap.navigateToArticle1()

        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.ap.backgroundcheckbutton))
            )

            self.ap.navigateToBackgroundCheck()

        except:
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'cbc.federalCourtButton XPATH = {self.ap.backgroundcheckbutton}\n')
            assert False



        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.cbc.federalCourtButton))
            )

            self.cbc.navigateToFederalCourt()

        except:
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'cbc.federalCourtButton XPATH = {self.cbc.federalCourtButton}\n')
            assert False

        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.fl.startreportbutton))
            )

            self.fl.navigateToPurchase()

        except:
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'fl.startreportbutton XPATH = {self.fl.startreportbutton}\n')
            assert False

        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.fc.orderfirstname))
            )

            self.fc.makePurchase()

        except:
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'fc.orderfirstname XPATH = {self.fc.orderfirstname}\n')
            assert False