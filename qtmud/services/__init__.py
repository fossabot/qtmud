class ClientUtilities():
    def __init__(self, driver):
        self.__name__ = 'Client Utilities'
        self.__version__ = '0.1.0'
        self.driver = driver
        self.subscriptions = {'finger' }
