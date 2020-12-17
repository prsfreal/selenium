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

    @staticmethod
    def firstname():
        value = config.get('user1', 'firstname')
        return value

    @staticmethod
    def lastname():
        value = config.get('user1', 'lastname')
        return value

    @staticmethod
    def address():
        value = config.get('user1', 'address')
        return value

    @staticmethod
    def city():
        value = config.get('user1', 'city')
        return value

    @staticmethod
    def state():
        value = config.get('user1', 'state')
        return value

    @staticmethod
    def zip():
        value = config.get('user1', 'zip')
        return value

    @staticmethod
    def phone():
        value = config.get('user1', 'phone')
        return value

    @staticmethod
    def email():
        value = config.get('user1', 'email')
        return value

    @staticmethod
    def contractorname():
        value = config.get('user1', 'contractorname')
        return value

    @staticmethod
    def contractoremail():
        value = config.get('user1', 'contractoremail')
        return value
