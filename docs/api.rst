#########
qtMUD API
#########

This is the complete API for qtMUD

qtmud module
############

.. automodule:: qtmud
    :members:
    :undoc-members:
    :show-inheritance:

qtmud.cmds module
=================

.. automodule:: qtmud.cmds
    :members:
    :undoc-members:
    :show-inheritance:

qtmud.services module
=====================

.. automodule:: qtmud.services
    :members:
    :undoc-members:
    :show-inheritance:

qtmud.subscriptions module
==========================

.. automodule:: qtmud.subscriptions
    :members:
    :undoc-members:
    :show-inheritance:

qtmud.txt module
================

.. automodule:: qtmud.txt
    :members:
    :undoc-members:
    :show-inheritance:

Glossary
########
.. glossary::
    MUD
        Multi-User Dimension. A more historic term for MMORPG, MUDs were some
        of the earliest multiplayer games. `Wikipedia
        <https://www.wikiwand.com/en/MUD>`_ has a pretty comprehensive
        article on them.

    MUD client
        A specialized client for playing MUDs. (duh)

    MUD engine
        Also known as drivers, MUD engines are game engines meant for
        presenting :term:`MUDs <MUD>`. There have traditionally been two main
        classes of MUD engine: DIKU and LPC. DIKU MUDs came first, and used
        database-driven logic to present a simplistic hack-and-slash
        environment to the player. LPC MUDs used object-oriented programming
        techniques to render more detailed game worlds to the player. qtmud
        follows in the tradition of the latter.

    mudlib
        short for Multi-User Dimension Library, a mudlib is a game written
        for a :term:`MUD engine` to run. From qtmud's perspective, a mudlib
        is a Python package which is heavily reliant on the :mod:`qtmud` module.