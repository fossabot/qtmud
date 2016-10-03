import qtmud

# pylint: disable=invalid-name

def commands(client, *, H=False, h=False):
    """ Sends a list of the client's commands to the client.

        :param client:      The client issuing the command command. (That'd be
                            you.) This isn't part of the command you enter.
        :param H:           Shows the client this docstring.
        :param h:           Shows the client a brief help.

        Creates a ``send`` event to tell the client a list of their commands.
    """
    output = ''
    brief = ('commands [-Hh]\n\n'
             'If entered without argument, lists all your valid commands.')
    if H:
        output += commands.__doc__
    elif h:
        output += brief
    else:
        output += ('Your commands are: {}'
                   ''.format(', '.join([c for c in client.commands.keys()])))
    if output:
        qtmud.schedule('send', recipient=client, text=output)
        return True


# pylint: disable=blacklisted-name
def foo(client, *, H=False, h=False, p=False):
    """ The dedicated test command

        :param client:      The client issuing the foo command. (That'd be
                            you.) **This isn't part of the command you enter.**
        :param H:           Shows the client this docstring.
        :param h:           Shows the client a brief help.

        This is a testing command, so you should check the source itself for
        information on what it actually does.
    """
    output = ''
    brief = ('syntax: foo [-Hh]\n\n'
             'Check source for real information, this is a testing command.')
    if H:
        output += foo.__doc__
    elif h:
        output = brief
    elif p:
        line = ('You can also use %^RED%^nesting %^GREEN%^Pinkfish-style '
                '%^B_YELLOW%^markup tags%^, though they%^ become less%^ '
                'readable.')
        output += ('You test the pinkfish_parser with the following line:\n\n'
                   '{}\n\nIt returns: {}'.format(line,
                                                 qtmud.pinkfish_parse(
            line)))
    else:
        output = 'You foo, to no effect.'
    if output:
        qtmud.schedule('send', recipient=client, text=output)
    return True
# pylint: enable=blacklisted-name


def help(client, topic='', *, H=False, h=False, domain=''):
    """ The command for receiving in-game help. Searches through commands,
    subscribers, and active_services and returns either a list of available
    matching helpfiles, or the docstring of the single match.

        :param client:      The client issuing the help command. (That'd be
                            you.) **This isn't part of the command you enter.**
        :param H:           Shows the client this docstring.
        :param h:           Shows the client a brief help.
        :param topic:       None by default, otherwise the name of the
                            command/service/subscriber you're looking to get
                            help with.
        :param domain:      Optionally limit where you're looking for help to
                            either cmds, subscribers, or services.

        For example, you might enter ``help talker`` to learn more about qtMUD's
        talker system. You would be prompted to enter either
        ``help --domain=cmds talker`` to learn about the in-game talker
        command or ``help --domain=services talker`` to learn about the
        Talker service`.
    """
    output = ''
    brief = ('help [-Hh] [--domain=$domain] [topic]\n\n'
             'Search for help for *topic*. Use *--domain=* to limit where you '
             'search to cmds, subscribers, or services.')
    matches = []
    help_locations = {'cmds': [client.commands],
                      'subscribers': [qtmud.subscribers],
                      'services': [qtmud.active_services]}
    if H:
        output += help.__doc__
    elif h:
        output += brief
    elif topic:
        topic = topic.lower()
        for _domain, locations in help_locations.items():
            print(domain)
            print(_domain)
            if domain == _domain or not domain:
                for location in locations:
                    if topic in location:
                        matches.append(location[topic])
        if matches:
            if len(matches) == 1:
                output += matches[0].__doc__
            else:
                output += ('Multiple matches found, try "help '
                           '--domain=*domain* {}" where *domain* is one of : {}'
                           ''.format(topic,
                                     ', '.join(m.__module__.split('.')[-1]
                                               for m in matches)))
    else:
        output += help.__doc__
    if output:
        qtmud.schedule('send', recipient=client, text=output)
        return True
    else:
        output = 'No help found. Try looking at https://qtmud.rtfd.io'
        qtmud.schedule('send', recipient=client, text=output)
        return False


def talker(client, channel=None, *, H=False, h=False, l=False):
    """ Command for interacting with the Talker service.

        :param client:      The client issuing the talker command. (That'd be
                            you.) **This isn't part of the command you enter.**
        :param H:           Shows the client this docstring.
        :param h:           Shows the client a brief help.
        :param channel:     The channel you're getting information on.
        :param l:           Show the channel's history.

        .. todo:: --depth argument to specify how much history to show
    """
    output = ''
    brief = ('syntax: talker [-Hhl] [channel]\n\n'
             'If entered without argument, lists the channels you\'re tuned '
             'into. If a channel is given, shows information about that '
             'channel. If the -l flag is given, shows that channel\'s logs.')
    if H:
        output += talker.__doc__
    elif h:
        output = brief
    else:
        if not channel:
            output += ('you\'re listening to {}'
                      ''.format([c for c in client.channels]))
        else:
            if channel in client.channels:
                if l:
                    output += ('({}) channel log:\n{}'
                               ''.format(channel,
                                         '\n'.join(m for m in
                                                   qtmud.active_services[
                                                       'talker'].history[
                                                           channel])))
                else:
                    output += 'Info about the channel goes here.'
    if output:
        qtmud.schedule('send', recipient=client, text=output)
        return True


def quit(client, *, H=False, h=False):
    """ Command to quit qtMUD

        :param client:      The client issuing the quit command. (That'd be
                            you.) **This isn't part of the command you enter.**
        :param H:           Shows the client this docstring.
        :param h:           Shows the client a brief help.
    """
    output = ''
    brief = ('syntax: help [-Hh]\n\n'
             'Causes the client to leave the game.')
    if H:
        output += quit.__doc__
    elif h:
        output = brief
    else:
        qtmud.schedule('send', recipient=client, text='you quit goodbye')
        qtmud.schedule('client_disconnect', client=client)
    if output:
        qtmud.schedule('send', recipient=client, text=output)
    return True


def who(client, *, H=False, h=False):
    """ Command to check your name

        :param client:      The client issuing the who command. (That'd be
                            you.) **This isn't part of the command you enter.**
        :param H:           Shows the client this docstring.
        :param h:           Shows the client a brief help.
    """
    output = ''
    brief = ('syntax: who [-Hh]\n\n'
             'Shows a list of the currently connected clients.')
    if H:
        output += who.__doc__
    elif h:
        output = brief
    else:
        output = ('The following clients are currently connected:\n'
                  '{}'.format('\n'.join([c.name for c in
                                         qtmud.connected_clients])))
    qtmud.schedule('send', recipient=client, text=output)
    return True


def whoami(client, *, H=False, h=False):
    """ Command to quit qtMUD

        :param client:      The client issuing the whoami command. (That'd be
                            you.) **This isn't part of the command you enter.**
        :param H:           Shows the client this docstring.
        :param h:           Shows the client a brief help.
    """
    output = ''
    brief = ('syntax: whoami [-Hh]\n\n'
             'Shows your own name.')
    if H:
        output += whoami.__doc__
    elif h:
        output = brief
    else:
        output = ('You are {}'.format(client.name))
    qtmud.schedule('send', recipient=client, text=output)
    return True
