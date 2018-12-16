###########
Using qtMUD
###########

On its own, qtMUD is a talker-style MUD. This means it provides
basic user accounts and the ability for them to communicate with
each other directly or through channels, along with some utility
functions.

qtMUD is 

While this is intended to be a framework for more complex MUDs,

Quickstart
##########

The easiest way to get started with qtMUD is by installing the
`PyPi package <https://pypi.python.org/pypi/qtMUD/>`_::

    $ pip install qtmud

If this fails for any reason, check the `Installation <#installation>`_
seciton for help. If it works::

    $ qtmud_run

should produce output like::

    qtmud_run preparing to start qtmud 0.0.6
    qtmud        WARNING  No valid config found, using default values
    qtmud        INFO     qtmud.load() called
    qtmud        INFO     adding qtmud.subscriptions to qtmud.subscribers
    qtmud        INFO     adding qtmud.services to qtmud.active_services
    qtmud        INFO     qtmud.load()ed
    qtmud        INFO     filling qtmud.client_accounts from ./qtmud_client_accounts.p
    qtmud        INFO     start()ing active_services
    qtmud        INFO     talker start()ed
    qtmud        INFO     start()ing MUDSocket
    qtmud        INFO     MUDSocket successfully bound to ('localhost', 5787)
    qtmud        INFO     MUDSocket successfully bound to ('localhost', 5788, 0, 0)
    qtmud        INFO     mudsocket start()ed
    qtmud        INFO     qtmud.run()ning

This means that qtMUD is up and running and you can connect to it as a
client. The easiest way to do this is with telnet::

    $ telnet localhost 5787

If everything is working, you should see output similar to this:::

    Trying ::1...
    Connection failed: Connection refused
    Trying 127.0.0.1...
    Connected to localhost.
    Escape character is '^]'.

    qtmud               0.0.6

    Successfully connected to qtmud, press enter to continue login...

From there, you can log in (qtMUD has *very* basic user accounts) and play
around with the default commands.

Installation
############

.. todo:: in-depth explanation of installation procedure for non-developers.


Configuration
#############

.. literalinclude:: .static/example.conf

.. todo:: verbose explanation of the qtmud.conf file

Client Features
###############

.. todo:: explanation of what clients can do, and how they're represented on
          the backend.

Pinkfish Parser
===============

    .. versionadded:: 0.0.10

Players (and developers) can use Pinkfish-style tags to make up their text.
Not too much to explain here. Enjoy abusing it on the talker.

    .. image:: .static/pinkfish_example.png
