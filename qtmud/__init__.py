"""This module is the core of the qtMUD game engine.

    .. versionadded:: 0.0.1

This module contains the qtmudEngine class and establishes some core
configuration.
"""

import click
import importlib
import logging
import pickle
import os
import sys
import types
import uuid
from inspect import getmembers, isfunction, isclass
from logging.config import dictConfig

import qtmud.subscriptions
import qtmud.services
import qtmud.thing
from qtmud import cmds, txt

__version__ = '0.1.0'
"""int: the engine's version.

    .. versionadded:: 0.0.1
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
format, see :func:`python:logging.config.DictConfig` for more
information.

"""

class Driver():
    """The main MUD driver.

        .. versionadded:: 0.1.0

    This class is the main MUD driver. 

    Attributes
    ----------
    __name__ : str
        The engine's name.  This should be set to whatever this class is called, which should be named after the game engine.
    __version__: str
        The engine's version.  Set from the `qtmud` module's variable of the same name.
    logging : :mod:`logging`
        An import of the `logging` module. 
        .. todo:: This might not be used by anything, and if that's the case should be removed.
    log : :class:`logging.Logger`
        The engine's logger object.
    thing_template : :class:`qtmud.thing.Thing`
        The template Thing that'll be instanced and returned by :func:`new_thing`
    """
    def __init__(self):
        self.__name__ = 'qtmudEngine'
        self.__version__ = __version__
        self.logging_config = logging_config
        self.logging.config.dictConfig(self.logging_config)
        self.log = logging.getLogger(__name__)
        self.thing_template = qtmud.thing.Thing
        self.configuration = dict()
        self.enabled_features = list()
        self.loaded_subscriptions = dict()
        self.enabled_subscribers = dict()
        self.loaded_services = dict()
        self.started_services = dict()
        self.running_services = dict()
        self.mudlib = dict()
        self.mudlib_subscriptions = list()
        self.mudlib_services = list()
        self.events = dict()
        return
    
    def load(self, mudlib=None, services=None, subscriptions=None, optional_features=None):
        """Load optional features, mud libraries, services, and subscriptions.

            .. versionadded:: 0.1.0

        Parameters
        ----------
        mudlib : list
            The names (as strings) of the modules to be imported as MUD libraries.
        """
        log = self.log.getChild('load()')
        log.debug('Loading qtMUD.')
        log.debug('Enabling optional features.')
        for feature in optional_features:
            self.load_feature(feature)
        if subscriptions:
            log.debug('Loading qtMUD subscriptions.')
            for subscription in subscriptions.split(','):
                try:
                    self.load_subscription(getattr(qtmud.subscriptions,subscription))
                except AttributeError as err:
                    log.error('There is no "%s" subscription.', subscription)
                except Exception as err:
                    log.error('Failed to load "%s" subscription: %s', subscription, err, exc_info=True)
        else:
            log.warning('No subscriptions were enabled.')
        if services:
            log.debug('Loading qtMUD services.')
            for service in services.split(','):
                try:
                    self.load_service(getattr(qtmud.services,service))
                except AttributeError as err:
                    log.warning('There is no "%s" service.', service)
                except Exception as err:
                    log.warning('Failed to load "%s" service: %s', service, err, exc_info=True)
        if mudlib:
            self.load_mudlib(mudlib)
        log.info('qtMUD Engine has loaded. {} optional features enabled.  {} subscribers and {} services loaded.'.format(len(self.enabled_features), len(self.enabled_subscribers), len(self.loaded_services)))
        log.debug('The following optional features were loaded: {}'.format(', '.join(self.enabled_features)))
        log.debug('The following subscribers were loaded: {}'.format(', '.join(self.loaded_subscriptions)))
        log.debug('The following services were loaded: {}'.format(', '.join(self.loaded_services)))
        return

    def load_feature(self, feature):
        log = self.logging.getLogger(__name__+'.load_feature()')
        for requirement in feature_data[feature]['requirements']:
            try:
                importlib.import_module(requirement)
                self.enabled_features.append(feature)
                log.debug('"{}" feature was enabled.'.format(feature))
            except ImportError as err:
                log.debug('"{}" feature failed to load: {}'.format(err))
        return

    def load_mudlib(self, mudlib):
        """ This method loads a mudlib.

            .. versionadded:: 0.1.0
        """
        log = self.logging.getLogger(__name__+'.load()')
        log.debug('Loading mudlib: %s', mudlib)
        log.debug('Importing mudlib modules')
        try:
            self.mudlib = importlib.import_module(mudlib)
            log.debug('Imported core mudlib module')
            try:
                self.mudlib_subscriptions = importlib.import_module(mudlib+'.subscriptions')
                log.debug('Imported mudlib subscriptions module.')
                self.mudlib_services = importlib.import_module(mudlib+'.services')
                log.debug('Imported mudlib services module.')
            except ImportError as err:
                log.warning('Failed to import a part of the MUD library: {}'.format(err))
            log.info('Imported {} version {}'.format(self.mudlib.__name__, self.mudlib.__version__))
        except ImportError as err:
            log.error('Failed to import the MUD library: {}'.format(err))
        log.debug('Enabling default mudlib subscriptions.')
        for sub in [s[1] for s in getmembers(self.mudlib_subscriptions) if isfunction(s[1])]:
            if sub.__name__ in self.mudlib_subscriptions.exclusive_subscriptions:
                self.enabled_subscribers.pop(sub.__name__)
            if sub.__name__ not in self.enabled_subscribers:
                self.enabled_subscribers[sub.__name__] = list()
            self.enabled_subscribers[sub.__name__].append(sub)

    def load_subscription(self, subscription):
        log = self.logging.getLogger(__name__+'.load_subscription()')
        sub = subscription
        sub_name = subscription.__name__
        log.debug('Loading "%s" subscription', sub_name)
        if sub_name not in self.loaded_subscriptions:
            self.loaded_subscriptions[sub_name] = list()
        self.loaded_subscriptions[sub_name].append(sub)

    def load_service(self, service):
        log = self.logging.getLogger(__name__+'.load_service()')
        serv = service
        serv_name = service.__name__
        if serv_name in self.loaded_services:
            log.warning('Failed to load the "%s" service, %s, because there is already a service by that name, %s', serv_name, serv, self.loaded_services[serv_name])
        else:
            try:
                self.loaded_services[serv_name] = serv(self)
                try:
                    self.loaded_services[serv_name].load()
                except AttributeError as err:
                    log.debug('The %s service has no load method, so it\'ll be considered loaded.', serv_name)
            except Exception as err:
                log.warning('Failed to load %s:%s', serv_name, err, exc_info=True)

    def start(self):
        log = self.logging.getLogger(__name__+'.start()')
        log.debug('Starting qtMUD.')
        for service in self.loaded_services:
            try:
                self.loaded_services[service].start()
                self.started_services[service] = self.loaded_services[service]
            except AttributeError:
                pass
            except RuntimeWarning as err:
                log.warning('Failed to start %s: %s', service, err, exc_info=True)
        log.info('qtMUD has started.  The following services were started: {}'.format(', '.join(self.started_services)))
        return

    def run(self):
        log = self.logging.getLogger(__name__+'.run()')
        log.debug('Running the qtMUD engine.')
        try:
            while True:
                self.tick()
        except KeyboardInterrupt:
            log.info('KeyboardInterrupt detected, shutdown scheduled.')
            self.shutdown()
        return

    def shutdown(self):
        log = self.log.getChild('shutdown()')
        log.debug('Shutting down.')
        while True:
            if self.events:
                log.debug('Processing final events: {}'.format(qtmud.events))
                self.tick()
            else:
                break
        for service in self.loaded_services:
            service = self.loaded_services[service]
            log.debug('Shutting down {}.'.format(service.__class__.__name__))
            try:
                service.shutdown()
                log.debug('shutdown() %s successfully',
                          service.__class__.__name__)
            except Exception as err:
                log.warning('%s failed to shutdown: %s',
                            service.__class__.__name__, err)
        log.info('shutdown() finished, raising SystemExit')
        raise SystemExit

    def new_thing(self, **kwargs):
        return self.thing(**kwargs)
        
    def schedule(self, sub, **payload):
        log = self.logging.getLogger(__name__+'.schedule()')
        if not self.loaded_subscriptions.get(sub, []):
            log.warning('Failed to schedule "%s" event, but there is no loaded subscription.', sub)
            return False
        for method in self.loaded_subscriptions.get(sub, []):
            if method not in self.events:
                self.events[method] = []
            log.debug('Scheduled "%s" event.', method.__name__)
            self.events[method].append(payload)
        return

    def tick(self):
        log = self.logging.getLogger(__name__+'.tick()')
        if self.events:
            current_events = self.events
            self.events = dict()
            for event in current_events:
                for call in current_events[event]:
                    try:
                        event(self, **call)
                    except Exception as err:
                        log.warning('An event failed: {}'.format(err), exc_info=True)
        for service in self.started_services:
            try:
                self.started_services[service].tick()
            except AttributeError:
                pass
        return
    
class TalkerHandler(logging.Handler):
    def __init__(self):
        super(TalkerHandler, self).__init__()
        self.talker = active_services['talker']

    def emit(self, record):
        self.talker.broadcast(channel=record.levelname, speaker=record.name,
                              message=record.msg)


def load(optional_features=None,mudlib_name=None):
    """This function loads the qtMUD engine, and optionally a library.

        .. versionadded:: 0.0.3

    This function begins by enabling whatever features are specified.
    Most importantly, puts every function from
    :mod:`qtmud.subscriptions` and every class from
    :mod:`qtmud.services` into :attr:`subscribers` and
    :attr:`active_services`, respectively.

    After populating `subscribers` and `active_services`, calls the start()
    method for each class in `active_services`, then attempts to load
    :attr:`MUDLIB`, if one is specified, and finally calls
    :func:`load_client_accounts`.

    """
    global active_services
    global enabled_subscribers
    global mudlib
    load_features(features=features)
    self.log.debug('Adding qtmud.subscriptions to qtmud.subscribers.')
    subscribers = {s[1].__name__: [s[1]] for
                   s in getmembers(subscriptions) if isfunction(s[1])}
    self.log.debug('Adding qtmud.services to qtmud.active_services.')
    active_services = {t[1].__name__.lower(): t[1]() for
                       t in getmembers(services) if isclass(t[1])}
    if 'talker' in active_services:
        self.log.addHandler(TalkerHandler())
        for level in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
            active_services['talker'].new_channel(level)
    if mudlib_name:
        self.log.debug('Loading the {} library.'.format(mudlib_name))
        try:
            mudlib = importlib.import_module(mudlib_name)
            self.log.info('Imported {} version {}.'.format(mudlib_name, mudlib.__version__))
            try:
                mudlib.load()
            except Exception as err:
                self.log.error('{}'.format(err))
        except Exception as err:
            self.log.error('Failed to import {}: {}.'.format(mudlib_name, err))
    if load_client_accounts():
        pass
    log.info('{} has loaded {} subscribers {} and active_services.'.format(engine_name, len(subscribers), len(active_services)))
    return True

def load_features(features):
    log.debug('Enabling optional features.')
    for feature in features:
        if features[feature] is True:
            for requirement in feature_data[feature]['requirements']:
                try:
                    importlib.import_module(requirement)
                    features[feature] = True
                    log.debug('"{}" was turned on.'.format(feature))
                except ImportError as err:
                    log.debug('"{}" was left off.'.format(feature))
    log.info('The following optional features were enabled: {}'.format(', '.join([f for f in features if features[f] is True])))

    return True

def load_client_accounts(file=(os.environ.get('QTMUD_CLIENT_PICKLE', None))):
    """ Populates :attr:`qtmud.client_accounts` with the pickle file
    specified. """
    if not file:
        return False
    global client_accounts
    try:
        client_accounts = pickle.load(open(file, 'rb'))
        log.debug('qtmud.client_accounts filled from %s', file)
        return True
    except FileNotFoundError:
        log.warning('No save file found, attempting to make one at %s', file)
        try:
            save_client_accounts()
        except Exception as err:
            log.error('Failed to create a save file.  All changes will be lost.')
        return False


def new_client_account(name, password, birthtime=None):
    """ Create a new client account in :attr:`client_accounts`"""
    client_accounts[name.lower()] = {'name': name,
                                     'password': password}
    if birthtime:
        client_accounts[name]['birthtime'] = birthtime
    log.debug('made the new client %s', name)
    save_client_accounts()
    return client_accounts[name]

def embolden(text):
    for marker in ['**', '*', '``', '`']:
        text = text.split(marker)
        for word in text[1::2]:
            if word:
                text[text.index(word)] = '%^B_WHITE%^' + word + '%^'
        text = ''.join(text)
    return text


def pinkfish_parse(text, requester=None):
    if 'colored_output' not in enabled_features:
        return
    colors = {'BLACK': colored.black,
              'RED': colored.red,
              'GREEN': colored.green,
              'YELLOW': colored.yellow,
              'BLUE': colored.blue,
              'MAGENTA': colored.magenta,
              'CYAN': colored.cyan,
              'WHITE': colored.white}
    debug = ''
    working_text = ''
    layers = []
    bold = False
    delimiter = '%^'
    split_text = [c for c in embolden(text).split(delimiter)]
    if len(split_text) <= 1:
        return text
    position = 0
    while position < len(split_text):
        chunk = split_text[position]
        if chunk in ['B_'+c for c in colors]:
            bold=True
            chunk = ''.join(chunk.split('_')[1:])
        if chunk in colors:
            layers.append((chunk, bold))
            position += 1
        elif layers:
            layer = layers[-1]
            working_text += colors[layer[0]](chunk, bold=layer[1])+'\033[0;0m'
            position += 1
            if position < len(split_text):
                if split_text[position] not in colors and \
                                split_text[position] not in ['B_' + c for c in
                                                             colors]:
                    layers.pop(-1)
        else:
            working_text += chunk
            position += 1
    return working_text+'\033[0;0m'


def run():
    """ main loop """
    log.info('qtmud.run()ning')
    try:
        while True:
            tick()
    except KeyboardInterrupt:
        log.info('shutdown started')
        schedule('shutdown')
        tick()


def save_client_accounts(file=(os.environ.get('QTMUD_CLIENT_PICKLE', None))):
    """ Saves a pickle of the current :attr:`client_accounts`."""
    log.debug('saving client_accounts to %s', file)
    try:
        pickle.dump(client_accounts, open(file, 'wb'))
        return True
    except FileNotFoundError as err:
        log.warning('failed to save client_accounts: %s', err)


def schedule(sub, **payload):
    """ Schedules a call to sub with payload passed as parameters.
    """
    if not subscribers.get(sub, []):
        log.warning('Tried to schedule a %s event, no subscribers '
                    'listen to it though.', sub)
        return False
    for method in subscribers.get(sub, []):
        if method not in events:
            events[method] = []
        events[method].append(payload)
    return True


def search_connected_clients_by_name(name):
    """ Searches through :attr:`connected_clients` for one with a matching
    name. *(Ignores case)*

        :param name:        The name of the client you're looking for.
        :return list:       A list of connected clients with that name.
                            (Should probably just have one element.)
    """
    return [connected_clients[connected_clients.index(c)] for c in
            connected_clients
            if hasattr(c, 'name') and c.name.lower() == name.lower()]


def search_client_accounts_by_name(name):
    """ Searches through the :attr:`client_accounts` for a client with a
    matching name. *(For convenience, ignores case)*

        :param name:        The name of the client you're looking for
        :return list:       A list of the clients with that name. (Should
                            probably just have one element.)
    """
    return [c for c in client_accounts.keys() if c.lower() == name.lower()]


def start():
    """ Calls the start() function in every service in
    :attr:`active_services`.
    """
    log.debug('Starting the each service in qtmud.active_services.')
    for service in active_services:
        try:
            active_services[service].start()
        except AttributeError:
            log.debug('%s has no start method', service)
        except RuntimeWarning as warning:
            log.warning('%s failed to start: %s', service, warning)
    return True


def tick():
    """ Processes the events in :attr:`current_events`, sending them out to
    the :attr:`subscribers` who are listening for them.

        Also calls tick() in every service in :attr:`active_services`
    """
    global events
    if events:
        current_events = events
        events = dict()
        for event in current_events:
            for call in current_events[event]:
                try:
                    event(**call)
                except Exception as err:
                    log.warning(err, exc_info=True)
    for service in active_services:
        try:
            active_services[service].tick()
        except AttributeError:
            pass
    return True

