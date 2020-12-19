import time
from Configurations.Users import users
from Configurations.BasicClassConfig import basic

class ddFederalCheckoutPage(basic):

    orderfirstname = '//*[@id="billing_first_name"]'
    orderlastname = '//*[@id="billing_last_name"]'
    orderaddress = '//*[@id="billing_address_1"]'
    ordercity = '//*[@id="billing_city"]'
    orderstate = '//*[@id="billing_state"]'
    orderzip = '//*[@id="billing_postcode"]'
    orderphone = '//*[@id="billing_phone"]'
    orderemail = '//*[@id="billing_email"]'
    ordercontractorname = '//*[@id="billing_contractors_name"]'
    ordercontractoremail = '//*[@id="billing_contractors_email_address"]'
    ordercouponcode = '//*[@id="coupon_code"]'
    orderccinfo = '/html/body/div[1]/div/div/div/section[2]/div/div/div/div/div/div/div/div/div/div/form/div[2]/div/div[2]/ul/li/div/div/fieldset/div[1]/div/iframe'
    orderbutton = '//*[@id="place_order"]'
    ordertccheckbox = '//*[@id="terms"]'
    addonorderbutton = '//*[@id="wcf-upsell-offer"]/span/span'
    errorelement = '//*[@id="wcf-embed-checkout-form"]/div/form/div[1]'

    def __init__(self, driver):
        self.driver = driver

    def setfname(self, x):
        self.driver.find_element_by_xpath(self.orderfirstname).clear()
        if x == None:
            self.driver.find_element_by_xpath(self.orderfirstname).send_keys('')
        else:
            self.driver.find_element_by_xpath(self.orderfirstname).send_keys(x)

    def setlname(self, x):
        self.driver.find_element_by_xpath(self.orderlastname).clear()
        self.driver.find_element_by_xpath(self.orderlastname).send_keys(x)

    def setaddress(self, x):
        self.driver.find_element_by_xpath(self.orderaddress).clear()
        self.driver.find_element_by_xpath(self.orderaddress).send_keys(x)

    def setcity(self, x):
        self.driver.find_element_by_xpath(self.ordercity).clear()
        self.driver.find_element_by_xpath(self.ordercity).send_keys(x)

    def setstate(self, x):
        self.driver.find_element_by_xpath(self.orderstate).clear()
        self.driver.find_element_by_xpath(self.orderstate).send_keys(x)

    def setzip(self, x):
        self.driver.find_element_by_xpath(self.orderzip).clear()
        if x == None:
            self.driver.find_element_by_xpath(self.orderzip).send_keys('')
        else:
            self.driver.find_element_by_xpath(self.orderzip).send_keys(x)

    def setemail(self, x):
        self.driver.find_element_by_xpath(self.orderemail).clear()
        self.driver.find_element_by_xpath(self.orderemail).send_keys(x)

    def setphone(self, x):
        self.driver.find_element_by_xpath(self.orderphone).clear()
        self.driver.find_element_by_xpath(self.orderphone).send_keys(x)

    def setemail(self, x):
        self.driver.find_element_by_xpath(self.orderemail).clear()
        self.driver.find_element_by_xpath(self.orderemail).send_keys(x)

    def setcname(self, x):
        self.driver.find_element_by_xpath(self.ordercontractorname).clear()
        self.driver.find_element_by_xpath(self.ordercontractorname).send_keys(x)

    def setcemail(self, x):
        self.driver.find_element_by_xpath(self.ordercontractoremail).clear()
        self.driver.find_element_by_xpath(self.ordercontractoremail).send_keys(x)

    def setcoupon(self, x):
        self.driver.find_element_by_xpath(self.ordercouponcode).clear()
        self.driver.find_element_by_xpath(self.ordercouponcode).send_keys(x)

    def setcardnum(self, x):
        self.driver.find_element_by_name('cardnumber').clear()
        self.driver.find_element_by_name('cardnumber').send_keys(x)

    def setcarddate(self, x):
        self.driver.find_element_by_name('exp-date').clear()
        self.driver.find_element_by_name('exp-date').send_keys(x)

    def setcardcode(self, x):
        self.driver.find_element_by_name('cvc').clear()
        self.driver.find_element_by_name('cvc').send_keys(x)

    def settandcbox(self):
        self.driver.find_element_by_xpath(self.ordertccheckbox).click()

    def setiframe(self, x):
        self.driver.switch_to.frame(frame_reference=self.driver.find_element_by_xpath(x))

    def setwindow(self):
        self.driver.switch_to.default_content()

    def clickSubmit(self):
        self.driver.find_element_by_xpath(self.orderbutton).click()







