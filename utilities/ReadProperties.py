#this is used to read config.ini and create objects for other modules
#Every update to config.ini requires a method to read it in ReadProperties.py

import configparser

config = configparser.RawConfigParser()
config.read('./Configurations/config.ini')

class readConfig:
    @staticmethod
    def URLHome():
        url = config.get('common info', 'URLHome')
        return url

    @staticmethod
    def URLAccounts():
        url = config.get('common info', 'URLAccounts')
        return url

    @staticmethod
    def URLSolutions():
        url = config.get('common info', 'URLSolutions')
        return url

    @staticmethod
    def URLArticles():
        url = config.get('common info', 'URLArticles')
        return url
