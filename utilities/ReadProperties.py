import configparser

config = configparser.RawConfigParser()
config.read('./Configurations/config.ini')

class readConfig:

    @staticmethod
    def username():
        id = config.get('common info', 'userName')
        return id

    @staticmethod
    def BaseURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def password():
        password = config.get('common info', 'password')
        return password