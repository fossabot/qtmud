"""This module contains the Client Utilities service class.

    .. versionadded:: 0.1.0


"""

__version__ = '0.1.0'
"""str: The service's version.

"""
class ClientUtilities():
    def __init__(self, driver):
        self.__name__ = 'ClientUtilities'
        self.__version__ = '0.1.0'
        self.driver = driver
        self.log = driver.log.getChild('service.%s' % self.__name__)
        self.subscriptions = {'finger' : 'rabble' }

    def finger(self):
        return

    def start(self):
        log = self.log.getChild('start()')
        log.debug('Starting.')
