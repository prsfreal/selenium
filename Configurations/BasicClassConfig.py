#Contains attributes of the TestSuiteClasses that get created for each new file in ./testCases
#These attibutes may or not be called for each test method.

import inspect
from utilities.CustomLogger import LogGen
from utilities.DataBaseConnection import MySQLConnection


class basic:
    logger = LogGen.loggen()
    defName = (inspect.stack()[0][3])
    MYSQL = MySQLConnection()