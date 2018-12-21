"""This module is the core of the qtMUD game engine.

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

This dictionary contains information about qtMUD's various
optional features, following the schema::

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

    This class is the main MUD **driver**: the engine that is
    qtMUD.

    Attributes
    ----------
    __name__ : str
        The engine's name.  Set to :attr:`qtmud.__name__`. 
    __version__: str
        The engine's version.  Set to :attr:`qtmud.__version__`.
    log : :class:`logging.Logger`
        The engine's logger object.
    thing_template : :class:`qtmud.thing.Thing`
        The template Thing that'll be instanced and returned by
        :func:`new_thing`
    loaded_services : dict
        Services that have had their subscriptions loaded.
    loaded_subscriptions : dict
        Subscriptions that will be passed events when the driver
        :func:`ticks <tick>`.

    """
    def __init__(self):
        self.__name__ = __name__
        self.__version__ = __version__
        self.logging_config = logging_config
        logging.config.dictConfig(self.logging_config)
        self.log = logging.getLogger(__name__)
        self.loaded_services = list()
        self.loaded_subscriptions = dict()
        self.started_services = list()
        self.events = dict()
        return
    
    def load(self, services=[]):
        """Load the driver.

            .. versionadded:: 0.1.0        

        This function ultimately has the goal of populating
        :attr:`loaded_services` and attr:`loaded_functions`.
        It does that by, for each ``service`` in ``services``,
        :meth:`creating a new instance
        <qtmud.Driver.create_class_instance_by_name>` and
        :meth:`loading it <qtmud.Driver.load_service>`.

        Parameters
        ----------
        services : list
            The names (as strings) of the classes to instanced as
            driver services.

        Returns
        -------
        None

        """
        log = self.log.getChild('load()')
        log.debug('Loading.')
        self.load_subscription(service=self, subscription=('shutdown', {}))
        for service in services:
            self.load_service(service)
        log.info('Loaded %s services and %s subscriptions.',
                 (', '.join([s.__name__ for s in self.loaded_services]) if self.loaded_services else 'no'),
                 (', '.join([s for s in self.loaded_subscriptions]) if self.loaded_subscriptions else 'no'))

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
        object
            Returns an instance of the found class, or None.

        """
        log = self.log.getChild('create_class_instance_by_name()')
        log.debug('Instancing %s.', class_name)
        m_name = '.'.join(class_name.split('.')[0:-1])
        c_name = class_name.split('.')[-1]
        try:
            return getattr(importlib.import_module(m_name), c_name)(self)
        except (ImportError, AttributeError):
            log.error('%s does not exist.', class_name)
        except Exception as err:
            log.error('Failed: %s', err, exc_info=True)

    def load_service(self, service):
        """Loads a service into the driver.

            .. versionadded:: 0.1.0

        This function loads a service into the qtMUD driver,
        which means adding its specified subscriptions to the
        driver's record of loaded subscriptions.

        Parameters
        ----------
        service : string
            The class to be loaded into the driver, such as 
            ``qtmud.services.ClientUtilities``

        """
        log = self.log.getChild('load_service()')
        log.debug('Loading service from %s', service)
        service = self.create_class_instance_by_name(service)
        log.debug('Loading %s version %s', service.__name__, service.__version__)
        try:
            for sub in service.subscriptions:
                self.load_subscription(service, (sub, service.subscriptions[sub]))
            self.loaded_services.append(service)
        except Exception as err:
            log.warning('Failed: %s', err, exc_info=True)

    def load_subscription(self, service, subscription):
        """Loads a subscription into the driver.

            .. versionadded:: 0.1.0
        
        """
        log = self.log.getChild('load_subscription()')
        log.debug('Loading %s subscription from %s', subscription[0], service.__name__)
        try:
            self.loaded_subscriptions[subscription[0]] = getattr(service, subscription[0])
        except Exception as err:
            log.warning('Failed: %s', err, exc_info=True)
        
    def start(self):
        """Starts the driver and its loaded services.

            .. versionadded:: 0.1.0

        """
        log = self.log.getChild('start()')
        log.debug('Starting.')
        for service in self.loaded_services:
            service.start()
        log.info('Started %s services.',
                 (', '.join([s.__name__ for s in self.started_services]) if self.started_services else 'no'))
        return

    def run(self):
        """Runs the driver: ticks it until told otherwise.

            .. versionadded:: 0.1.0

        """
        log = self.log.getChild('run()')
        log.debug('Running.')
        try:
            while True:
                self.tick()
        except KeyboardInterrupt:
            log.info('KeyboardInterrupt detected: scheduling shutdown event.')
            self.schedule('shutdown')
            self.tick()
        return

    def tick(self):
        """Ticks every started service and passes events to subscriptions.

        .. versionadded:: 0.1.0
        
        """
        log = self.log.getChild('tick()')
        if self.events:
            current_events = self.events
            log.debug('Events this tick: %s', current_events)
            self.events = dict()
            for event in current_events:
                for call in current_events[event]:
                    try:
                        self.loaded_subscriptions[event](**call)
                    except Exception as err:
                        log.warning('Event %s failed: %s', event, err, exc_info=True)

    def schedule(self, sub, **payload):
        log = self.log.getChild('schedule()')
        log.debug('Scheduling %s event.', sub)
        if not self.loaded_subscriptions.get(sub):
            log.warning('No subscription loaded for %s events', sub)
        else:
            if sub not in self.events:
                self.events[sub] = []
            self.events[sub].append(payload)



    def shutdown(self):
        log = self.log.getChild('shutdown()')
        log.debug('Shutting down.')
        while True:
            if self.events:
                log.debug('Processing events: %s', self.events)
                tick()
            else:
                break
        log.info('Shut down.  Raising SystemExit.')
        raise SystemExit

