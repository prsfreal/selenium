import pytest
from pageObjects.HomePage import homePage
from pageObjects.PrivacyPolicy import PrivacyPolicy
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
        self.hp = homePage(self.driver)


    def test_0001(self, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0001: Verify Text of 3 Banners is Present***')
        self.counter = 0
        self.src = self.driver.page_source

        if self.hp.slider1text in self.src:
            self.logger.info("--Slider1 text present")

        else:
            self.logger.exception("--FAILED - Slider 1 Text did not match")
            self.counter +=1

        if self.hp.slider2text in self.src:
            self.logger.info("--Slider2 text present")

        else:
            self.logger.exception("--FAILED - Slider 2 Text did not match")
            self.counter +=1

        if self.hp.slider3text in self.src:
            self.logger.info("--Slider3 text present")

        else:
            self.logger.exception("--FAILED - Slider 3 Text did not match")
            self.counter +=1


        if self.counter == 0:

            self.MYSQL.cursor.execute("select * from customers where id = 15")
            record = self.MYSQL.cursor.fetchall()
            for i in record:
                self.logger.info(i[0])


            self.logger.info("PASSED\n")
            assert True

        else:
            self.logger.info(f'FAILED - {self.counter} element(s) failed to verify.\n')
            assert False


    def test_0002(self, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0002: Open FAQ 1***')
        self.action.move_to_element(self.driver.find_element_by_xpath(self.hp.faq1list1)).click().perform()

        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.hp.faq1list1))
            )
            self.logger.info('--Found the FAQ1 details')
            self.logger.info('PASSED\n')
            assert True


        except:
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'lp.FAQ1List XPATH = {self.hp.faq1list1}\n')
            assert False


    def test_0003(self, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0003: Footer Link***')
        self.action.move_to_element(self.driver.find_element_by_xpath(self.hp.privacypolicy)).click().perform()
        self.pp = PrivacyPolicy(self.driver)

        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, self.pp.paragraph))
            )

            self.logger.info('--Found the Privacy Policy Page')
            self.logger.info('PASSED\n')
            assert True


        except:
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'pp.paragraph XPATH = {self.pp.paragraph}\n')
            assert False






