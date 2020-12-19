import pytest
from POM.ArticlesArchivePage import articleArchivePage
from POM.ArticlePage import articlePage
from POM.CriminalBackgroundCheck import criminalBackgroundCheckPage
from POM.FederalLanding import federalLandingPage
from DDPOM.DDFederalCheckout import ddFederalCheckoutPage
from utilities.ReadProperties import readConfig
from Configurations.BasicClassConfig import basic
from selenium.webdriver.common.action_chains import ActionChains
from utilities import ExcelUtilities
import time


class Test_HomePageSuite(basic):
    URL = readConfig.URLArticles()
    dataPath = './DDTESTDATA/data2.xlsx'

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
        self.ddfc = ddFederalCheckoutPage(self.driver)


    def test_0001(self, additionalSetup):
        self.logger.info(f'***{self.defName}: test_0001: Bad Purchase Info***')
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
            self.waitAndsee(self.ddfc.orderfirstname)
            self.rows = ExcelUtilities.getRowCount(self.dataPath, 'Sheet1')
            self.columns = ExcelUtilities.getColumnCount(self.dataPath, 'Sheet1')
            status = []
            self.counter = 1

            for i in range(2, self.rows+1):
                self.fname = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 1)
                self.lname = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 2)
                self.address = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 3)
                self.city = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 4)
                self.state = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 5)
                self.zip = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 6)
                self.phone = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 7)
                self.email = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 8)
                self.cname = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 9)
                self.cemail = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 10)
                self.coupon = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 11)
                self.ccnum = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 12)
                self.ccdate = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 13)
                self.cccode = ExcelUtilities.readData(self.dataPath, 'Sheet1', i, 14)

                self.ddfc.setfname(self.fname)
                self.ddfc.setlname(self.lname)
                self.ddfc.setaddress(self.address)
                self.ddfc.setcity(self.city)
                self.ddfc.setstate(self.state)
                self.ddfc.setzip(self.zip)
                self.ddfc.setphone(self.phone)
                self.ddfc.setemail(self.email)
                self.ddfc.setcname(self.cname)
                self.ddfc.setcemail(self.cemail)
                self.ddfc.setcoupon(self.coupon)
                time.sleep(2)
                self.ddfc.setiframe(self.ddfc.orderccinfo)
                self.ddfc.setcardnum(self.ccnum)
                self.ddfc.setcarddate(self.ccdate)
                self.ddfc.setcardcode(self.cccode)
                self.ddfc.setwindow()
                time.sleep(2)
                self.ddfc.settandcbox()
                self.ddfc.clickSubmit()


                try:
                    self.waitAndsee(self.ddfc.errorelement, time=60)
                    self.logger.info(f'Test {self.counter} = PASS')
                    status.append('Pass')
                    self.driver.refresh()

                except:
                    self.logger.info(f'Test {self.counter} = FAIL')
                    status.append('Fail')

                self.counter += 1

        except:
            self.logger.exception(f'--Could not locate ELEMENT by XPATH')
            self.logger.info(f'fc.orderfirstname XPATH = {self.ddfc.orderfirstname}\n')
            assert False

        if 'Fail' not in status:
            self.logger.info(f'PASSED\n')
            assert True

        else:
            self.logger.info(f'FAILED\n')
            assert False