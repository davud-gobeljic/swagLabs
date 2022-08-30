import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\davud\PycharmProjects\swagLabs\Configurations\config.ini")

class ReadConfig():
    @staticmethod
    def getURL():
        url = config.get('common', 'baseURL')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common', 'password')
        return password
