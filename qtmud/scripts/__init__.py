"""This module contains scripts for interacting with the qtMUD Driver.

    .. versionadded:: 0.1.0

The qtMUD Driver is most commonly accessed through the shell
command ``qtmud``, which is implemented in this module, using
the :mod:`click` module.  The rest of this modules
documentation is written for the prespective of a command-line
user: someone accessing these functions through their shell or
a shell script.

"""
import click
import functools
import importlib
import sys

# This'll be assigned the return of
# logging.getLogger(__name__) by :func:`qtmud`, the base
# ``qtmud`` commmand.
log = None
"""obj: This module's logger object.

    .. versionadded:: 0.1.0

This starts as None, but is assigned the return of
:func:`logging.getLogger` by :func:`qtmud`, the base ``qtmud``
command.

"""

def standard_params(func):
    """Defines the "standard" qtmud command group paramters. 
    
        .. versionadded:: 0.1.0

    Within the :mod:`click` framework, the context of command
    options matters.  This usually makes sense, but for the
    purposes of the ``qtmud`` command group, it makes more
    sense to have them shared.  In practice, this means that
    the following commands are equivalent::
        qtmud --quiet serve
        qtmud serve --quiet

    This function creates the click options that'll be shared
    by the base ``qtmud`` command and all the subcommands.  If
    you're interested in making your own sub-command and want
    to make it accept these "standard" parameters, add this
    line before declaring the function::
        @standard_params

    """
    @click.option('--verbose', is_flag=True,
                  help='When passed, the standard output will every log message it receives.')
    @click.option('--quiet', is_flag=True,
                  help='When passed, the standard output will only show the important log messages it receives.')
    @click.option('--services',
                  envvar='QTMUD_SERVICES', default='qtmud.services.ClientUtilities',
                  help='A comma-separated list of driver services.', show_default=True)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@click.group()
@standard_params
@click.pass_context
def qtmud(ctx, verbose, quiet, services):
    """Interact with the qtMUD engine.

        .. versionadded:: 0.1.0

    This command provides access to qtMUD's driver
    configuration and subcommands for interacting with the
    driver.  Most importantly, this command lets you run a MUD
    with:: 
        qtmud serve
    
    This command lets you specify several driver options that
    are used before qtMUD loads itself: console log format and
    verbosity, and enabled driver services::
        qtmud --quiet serve --services=ClientUtilities,MUDSocket

    Services are classes which can specify new subscriptions
    for the driver to load, or be started and ticked when the
    driver does, and are responsible for all intradriver
    operations.  A default list of services is provided, which
    loads client utilities, an in-game chat service, and
    starts a socket server to allow client interfacing.

    Options can also be set through *environment values*,
    like::
        export QTMUD_SERVICES=ClientUtilities,MUDSocket

    """
    try:
        ctx.ensure_object(dict)
    except Exception as err:
        print('Click, the command parser qtMUD uses, '
              'failed to work: {}'.format(err))
    ctx.obj['verbose'] = verbose
    ctx.obj['quiet'] = quiet
    ctx.obj['QTMUD_SERVICES'] = services

@qtmud.command()
@standard_params
@click.pass_context
def serve(ctx, verbose, quiet, services):
    """Load, start, and run the qtMUD engine.

        .. versionadded:: 0.1.0

    This command loads, starts, and runs the MUD driver.

    Options may also be configured through *environment
    values*, please see use the command ``qtmud --help`` to
    see a list.

    """
    global log
    try:
        driver = importlib.import_module('qtmud').Driver()
        log = driver.log.getChild('scripts.qtmud.serve')
    except Exception as err:
        click.echo('Couldn\'t import the qtmud module: {}\n{}'.format(err, sys.exc_info()))
        exit()
    try:
        (driver.log.setLevel('ERROR')
         if (ctx.obj['quiet'] or quiet)
         else (driver.log.setLevel('DEBUG')
               if (ctx.obj['verbose'] or verbose)
               else None))
        driver.log.debug(('Driver logger level set to %s.  Only log '
                          'records at levels equal to or higher '
                          'than that will be shown.  10 is DEBUG, 40 '
                          'is ERROR'),
                         driver.log.getEffectiveLevel())
    except Exception as err:
        log.warning('Failed to set driver log level: %s',
                    err,
                    exc_info=True)
    log.info('Configured %s version %s', driver.__name__, driver.__version__)
    log.debug('Pre-load configuration applied.  Beginning to load.')
    try:
        driver.load(services=services.split(','))
    except Exception as err:
        log.critical('Failed to load qtMUD: %s', err, exc_info=True)

@qtmud.command()
@standard_params
@click.pass_context
def test(ctx, username):
    """ Test the qtMUD engine against expectations.

        .. versionadded:: 0.1.0

    This function (or command, if you're reading this in the command line).
    """
    click.echo('Test functions have not yet been written (or tied into this command.)')
    click.echo('Hello %s!' % username)
    

