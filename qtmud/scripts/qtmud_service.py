"""This module contains the qtmud command.

    .. versionadded:: 0.1.0

"""
import click
import importlib
import sys

log = None

@click.group()
@click.option('--verbose', is_flag=True, help='Show debug, info, warning, error, and critical log messages.')
@click.option('--quiet', is_flag=True, help='Show only error, and critical log messages.')
@click.pass_context
def qtmud(ctx, verbose, quiet):
    """Interact with the qtMUD engine.

        .. versionadded:: 0.1.0

    This function (or command, if you're reading this in the command
    line) provides the means for interacting with the qtMUD engine.
    """
    try:
        ctx.ensure_object(dict)
    except Exception as err:
        print('Click, the command parser qtMUD uses, failed to work: {}'.format(err))
    ctx.obj['VERBOSE'] = verbose
    ctx.obj['QUIET'] = quiet

@qtmud.command()
@click.pass_context
@click.option('--verbose', is_flag=True, help='Show debug, info, warning, error, and critical log messages.')
@click.option('--quiet', is_flag=True, help='Show only error, and critical log messages.')
@click.option('--mudlib', envvar='QTMUD_MUDLIB', default=None, help='The MUD library\'s main Python module.')
@click.option('--services', envvar='QTMUD_SERVICES', default='ClientUtilities,MUDSocket', help='Which services to load, start, and run.', show_default=True)
@click.option('--subscriptions', envvar='QTMUD_SUBSCRIPTIONS', default='send,shutdown', help='Which subscriptions to enable.', show_default=True)
@click.option('--colored_output/--no_colored_output', envvar='QTMUD_COLORED_OUTPUT', default=True, help='Whether to enable the colored output optional feature.', show_default=True)
def serve(ctx, verbose, quiet, mudlib, services, subscriptions, colored_output):
    """Load, start, and run the qtMUD engine.

        .. versionadded:: 0.1.0

    This function (or command, if you're reading this with your
    command line) loads, starts,  and runs a qtMUD server.  It does
    things like set up the MUD library, optional features, server
    ports, and so on.

    NOTE: These options may be set as environmental variables, please
    see README.org, under the "Configuration" heading.  In addition to
    these defaults, the mudlib you load may specify its own default
    subscriptions: please familiarize yourself with its configuration.

    """
    global log
    try:
        qtmud = importlib.import_module('qtmud').qtmudEngine()
        log = qtmud.log.getChild('qtmud_service')
        log.info('Imported %s version %s', qtmud.__name__, qtmud.__version__)
    except Exception as err:
        click.echo('Couldn\'t import the qtmud module: {}\n{}'.format(err, sys.exc_info()))
        exit()
    if ctx.obj['QUIET'] or quiet:
        log.info(('Making the log stream quiet: only error and critical output will be shown.'))
        qtmud.log.setLevel('ERROR')
    elif ctx.obj['VERBOSE'] or verbose:
        log.info('Making the log stream verbose: debug, info, warning, error, and critical output will be shown.')
        qtmud.log.setLevel('DEBUG')
    optional_features = list()
    if colored_output is True:
        optional_features.append('colored_output')
    try:
        qtmud.load(mudlib=mudlib, services=services, subscriptions=subscriptions, optional_features=optional_features)
        try:
            qtmud.start()
            try:
                qtmud.run()
            except Exception as err:
                log.critical('Failed to run qtMUD: %s', err, exc_info=True)
        except Exception as err:
            log.critical('Failed to start qtMUD: {}'.format(err))
    except Exception as err:
        log.critical('Failed to load qtMUD: {}'.format(err))

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
    

