#Contains attributes of the TestSuiteClasses that get created for each new file in ./testCases
#These attributes may or not be called for each test method.

import inspect
from utilities.CustomLogger import LogGen
from utilities.DataBaseConnection import MySQLConnection
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class basic():
    logger = LogGen.loggen()
    defName = (inspect.stack()[0][3])
    MYSQL = MySQLConnection()

    def waitAndsee(self, elem, find='XPATH', time=5):
        if find == 'XPATH':
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.XPATH, elem))
            )

        elif find == 'ID':
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.ID, elem))
            )

        else:
            WebDriverWait(self.driver, time).until(
                EC.presence_of_element_located((By.XPATH, elem))
            )
