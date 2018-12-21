g"""This module is the core of the qtMUD game engine.

    .. versionadded:: 0.0.1

This module contains the qtmudEngine class and establishes some core
configuration.
"""

import importlib
import logging
import sys
from logging.config import dictConfig

__name__ = 'qtMUD'
"""str: The engine's name.

"""

__version__ = '0.1.0'
"""str: The engine's version.

    .. versionadded:: 0.0.1

This variable is usually used with the builtin ``__name__`` to provide
information about the codebase.  An instanced :class:`Driver` will
also set its own ``__name__`` and ``__verison__`` equal to the
``qtmud`` modules'.

"""
__url__ = 'https://qtmud.readthedocs.io/en/latest/'
""" The engine's main website.

    .. versionadded:: 0.0.2

"""
feature_data = {
    'colored_output' : { 'requirements' : ['termcolor'] },
}
"""dict: Information about optional features.

    .. versionadded:: 0.1.0

This dictionary contains information about qtMUD's various optional features, following the schema::
    feature_name : { 'requirements' : feature_requirements }

Where ``feature_name`` is a lowercase_underscore_spaced unique term
for the optional feature, and ``feature_requirements`` is a list of
strings, where each string is a module to import.

"""
logging_config = dict(version=1,
                      formatters={'f': {'format': ('\033[34m%(asctime)s\033[0m \033[34;1m%(name)s\033[0m \n\033[32m%(levelname)-8s\033[0m %(message)s'),
                                        'datefmt': ('%Y%m%d %I%M:%S')}},
                      handlers={'stream': {'class': 'logging.StreamHandler', 'formatter': 'f', 'level': logging.DEBUG}},
                      root={'handlers': ['stream'], 'level': logging.INFO})
"""dict: Defines preloaded logging format.

    .. versionadded:: 0.1.0

This dictionary is used to set :class:`qtmudEngine`'s logging
configuration when its initialized.  For more information on the
format, see :func:`logging.config.DictConfig` for more
information.

"""

class Driver():
    """The main MUD driver.

        .. versionadded:: 0.1.0

    This class is the main MUD driver. 

    Attributes
    ----------
    __name__ : str
        The engine's name.  Set to :attr:`qtmud.__name__`. 
    __version__: str
        The engine's version.  Set to :attr:`qtmud.__version__`.
    log : :class:`logging.Logger`
        The engine's logger object.
    thing_template : :class:`qtmud.thing.Thing`
        The template Thing that'll be instanced and returned by :func:`new_thing`
    loaded_subscriptions : dict
        subscriptions that will be passed events when the driver :func:`ticks <tick>`.
    """
    def __init__(self):
        self.__name__ = __name__
        self.__version__ = __version__
        self.logging_config = logging_config
        logging.config.dictConfig(self.logging_config)
        self.log = logging.getLogger(__name__)
        self.loaded_subscriptions = dict()
        self.loaded_services = list()
        return
    
    def load(self, services=[]):
        """Load the driver.

            .. versionadded:: 0.1.0        

        This function ultimately has the goal of populating
        :attr:`loaded_services` and attr:`loaded_functions`.
        It does that by, for each ``service`` in ``services``,
        calling :func:`create_service_instance_by_name` and :func:`load_service`.

        Parameters
        ----------
        services : list
            The names (as strings) of the classes to instanced as driver services.

        Returns
        -------
        bool
            True unless there is a critical exception.

        """
        log = self.log.getChild('load()')
        log.debug('Driver is loading.')
        for service in services:
            service = self.create_service_instance_by_name(service)
            self.load_service(service) if service else None

    def create_class_instance_by_name(self, class_name):
        """Returns an instance of a class, given a name.

            .. versionadded:: 0.1.0

        Parameters
        ----------
        class_name : str
            The class to be looked for.  Should be a module
            and class path, like qtmud.services.ClientUtilities

        Returns
        -------
        obj
            Returns an instance of the found class, or None.

        """
        log = self.log.getChild('create_class_instance_by_name()')
        log.debug('Instancing %s.', service_name)
        m_name = '.'.join(service_name.split('.')[0:-1])
        c_name = service_name.split('.')[-1]
        try:
            return getattr(importlib.import_module(m_name), c_name)(self)
        except (ImportError, AttributeError):
            log.error('%s does not exist', fail_msg, class_name)
        except Exception as err:
            log.error('%s', fail_msg, err, exc_info=True)

    def load_service(self, service):
        """Loads a service into the driver.

            .. versionadded:: 0.1.0

        This function loads a service into the qtMUD driver,
        which means adding its specified subscriptions to the
        driver's record of loaded subscriptions.

        Parameters
        ----------
        service : string
            The class to be loaded into the driver, such as ``qtmud.services.ClientUtilities``

        """
        log = self.log.getChild('load_service()')
        log.debug('Loading %s', service.__name__)
        fail_msg = 'Failed to load %s' % service.__name__
        try:
            for sub in service.subscriptions:
                self.load_subscription(service, (sub, service.subscriptions[sub]))
            self.loaded_services.append(service)
        except Exception as err:
            log.warning('%s: %s', fail_msg, err, exc_info=True)

    def load_subscription(self, service, subscription):
        """Loads a subscription into the driver.

            .. versionadded:: 0.1.0
        
        """
        log = self.log.getChild('load_subscription()')
        log.debug('Loading %s subscription from %s', subscription[0], service.__name__)
        fail_msg = 'Failed to load %s subscription from %s' % subscription[0], service.__name__
        try:
            pass
        except Exception as err:
            log.warning('%s: %s', fail_msg, err, exc_info=True)
        
