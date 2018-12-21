"""This module contains the ``qtmud`` shell script.

    .. versionadded:: 0.1.0

The qtMUD driver is most commonly accessed through a shell command: ``qtmud``.

This module is the implementation of that command.  It's
implemented using the :mod:`click` module.  The rest of this
module's documentation is written for the perspective of a
command-line user: someone accessing these functions through
their shell or a shell script.

"""
import click
import functools
import importlib
import sys

log = None

def shared_params(func):
    @click.option('--verbose', is_flag=True,
                  help='When passed, the standard output will every log message it receives.')
    @click.option('--quiet', is_flag=True,
                  help='When passed, the standard output will only show the important log messages it receives.')
    @click.option('--mudlibs',
                  envvar='QTMUD_MUDLIBS', default=None,
                  help='A comma-separated list of MUD libraries.', show_default=True)
    @click.option('--services',
                  envvar='QTMUD_SERVICES', default='ClientUtilities,MUDSocket',
                  help='A comma-separated list of driver services.', show_default=True)
    @click.option('--optional_features',
                  envvar='QTMUD_OPTIONAL_FEATURES', default='colored_output',
                  help='A comma-separated list of optional features.', show_default=True)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@click.group()
@shared_params
@click.pass_context
def qtmud(ctx, verbose, quiet, mudlibs, services, optional_features):
    """Interact with the qtMUD engine.

        .. versionadded:: 0.1.0

    This command group provides access to the qtMUD driver,
    letting you configure some of the most core settings.

    \b
    Options can also be set through *environment values*,
    like::
        export QTMUD_MUDLIBS=fyreside
        export QTMUD_SERVICES=ClientUtilities,MUDSocket
        export QTMUD_OPTIONAL_FEATURES=colored_output
    
    """
    try:
        ctx.ensure_object(dict)
    except Exception as err:
        print('Click, the command parser qtMUD uses, failed to work: {}'.format(err))
    ctx.obj['VERBOSE'] = verbose
    ctx.obj['QUIET'] = quiet
    ctx.obj['QTMUD_MUDLIBS'] = mudlibs
    ctx.obj['QTMUD_SERVICES'] = services
    ctx.obj['QTMUD_OPTIONAL_FEATURES'] = optional_features

@qtmud.command()
@shared_params
@click.pass_context
def serve(ctx, verbose, quiet, mudlibs, services, optional_features):
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
        log = driver.log.getChild('scripts.qtmud.qtmud.serve')
        log.info('Imported %s version %s', driver.__name__, driver.__version__)
    except Exception as err:
        click.echo('Couldn\'t import the qtmud module: {}\n{}'.format(err, sys.exc_info()))
        exit()
    try:
        driver.log.setLevel('ERROR') if (ctx.obj['QUIET'] or quiet) else (driver.log.setLevel('DEBUG') if (ctx.obj['VERBOSE'] or verbose) else None)
        log.info('Log level is: %s', driver.log.getEffectiveLevel())
    except Exception as err:
        driver.log('Failed to set driver log level: %s', err, exc_info=True)
    try:
        driver.load()
    except Exception as err:
        log.critical('Failed to load qtMUD: %s', err)

@qtmud.command()
@click.pass_context
@click.option('--username', envvar='QTMUD_TEST_USERNAME')
def test(ctx, username):
    """ Test the qtMUD engine against expectations.

        .. versionadded:: 0.1.0

    This function (or command, if you're reading this in the command line).
    """
    click.echo('Test functions have not yet been written (or tied into this command.)')
    click.echo('Hello %s!' % username)
    

