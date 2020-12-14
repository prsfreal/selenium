#this is used to read config.ini and create objects for other modules
#Every update to config.ini requires a method to read it in ReadProperties.py

import configparser

config = configparser.RawConfigParser()
config.read('./Configurations/config.ini')

class readConfig:
    @staticmethod
    def BaseURL1():
        url = config.get('common info', 'baseURL1')
        return url

    @staticmethod
    def BaseURL2():
        url = config.get('common info', 'baseURL2')
        return url
