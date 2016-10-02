#####################
Developing with qtMUD
#####################

qtMUD is meant to be used as a framework for developing your own MUD. This
document contains an explanation of how qtMUD works, and some tutorials for
using it to create your own MUD.



Getting Started
###############

Download Source
===============

The easiest way to get the source code for qtMUD is by cloning the
`GitHub repository <https://github.com/emsenn/qtmud>`_::

    $ git clone https://github.com/emsenn/qtmud.git

This will create a new folder with

How it Works
============

The best way to explain how qtMUD functions is probably by looking, in
detail, at what happens when you execute ``./bin/qtmud_run``::

    qtmud_run preparing to start qtmud 0.0.6
    qtmud        WARNING  No valid config found, using default values

If ``qtmud_run`` isn't passed the ``--conf`` argument
(``qtmud_run --conf ./fireside.conf``), it will look in *./qtmud.conf*,
*./.qtmud.conf*, *~/qtmud.conf*, and *~/.qtmud.conf*, in that order. If it
can\'t find one there, it will rely on defaults set in the
:mod:`qtmud` module.::

    qtmud        INFO     qtmud.load() called
    qtmud        INFO     adding qtmud.subscriptions to qtmud.subscribers
    qtmud        INFO     adding qtmud.services to qtmud.active_services
    qtmud        INFO     qtmud.load()ed

:func:`qtmud.load` ::

    qtmud        INFO     filling qtmud.client_accounts from ./qtmud_client_accounts.p
    qtmud        INFO     start()ing active_services
    qtmud        INFO     talker start()ed
    qtmud        INFO     start()ing MUDSocket
    qtmud        INFO     MUDSocket successfully bound to ('localhost', 5787)
    qtmud        INFO     MUDSocket successfully bound to ('localhost', 5788, 0, 0)
    qtmud        INFO     mudsocket start()ed
    qtmud        INFO     qtmud.run()ning



Tutorials
#########

Making & Using Things
=====================

.. todo:: Coming by version 0.1.0!

Making & Using Subscriptions
============================

.. todo:: Coming by version 0.1.0!

Making & Using Services
=======================

.. todo:: Coming by version 0.1.0!

Local Customs
#############

These are all the rules that I try and follow. If you plan on
`submitting a pull request <https://github.com/emsenn/qtmud/pulls>`_ you should
try to follow these rules, where applicable. (A few sections are relevant
only to me, and are there so I don't forget how to do things..)

Flow
====

.. todo:: Coming by version 0.1.0!

Commit Messages
---------------

.. versionadded:: 0.0.8

Our commit messages follow the format used by
`gitchangelog <https://github.com/vaab/gitchangelog>`_, since that's what is
used to create the changelog.

That format is::

    action: [audience:] Summary of Commit [!tag]




Release
-------

bump version in:

* docs/conf.py
* qtmud/__init__.py
* setup.py

Versioning
==========

.. todo:: Coming by version 0.1.0!