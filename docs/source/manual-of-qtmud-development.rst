.. _manual-of-qtmud-development:

###########################
Manual of qtMUD Development
###########################

This manual is intended as a comprehensive reference for the
maintainance and development of qtMUD, as a codebase and as a
project.  It does not assume familiarity with Python, but does
assume you're familiar with :ref:`project-information`.

***************************
Introduction to the Project
***************************

qtMUD is a hobby project created by - `emsenn <https://emsenn.net>`_.

Background
==========

qtMUD's first commit was on September 3rd, 2016, with rapid
development happening until October 8th, 2016.  A basic notion of how
to handle things was sketched out, but then real life happened and the
project stopped being updated.

On December 17th, 2018, I had the time and interest in working qtMUD
again, and so began to overhaul it.  While a lot of the idea of the
existing code seemes solid, I'm unhappy with the implementation.

****************************
Introduction to the Codebase
****************************

Concepts
========

The MUD Driver
--------------

The MUD driver is the "engine" that makes a MUD happen.  In qtMUD, the
driver's main responsibility is maintaining a list of
subscriptions and events.  Subscriptions are functions that will be
called when an event is scheduled.

qtMUD provides very few subscriptions itself.  Most are added through
services.  qtMUD comes with several services, but its expected that
more will be added by a MUD library.

The qtMUD driver is implemented in with the :class:`qtmud.Driver`
class - though it's important to note, expects to be controlled by the
:ref:`qtmud-command`.

The best way of I can think of to explain how qtMUD works is by
explaining how what happens when you run the command ``qtmud serve``,
which according to its help text "loads, starts, and runs the qtMUD
driver."

Which, after handling all the options and arguments, is exactly what
it does: it creates an instance of :class:`qtmud.Driver`, and calls
:func:`qtmud.Driver.load`, :func:`qtmud.Driver.start`, and
:func:`qtmud.Driver.run`.

The MUD Library
---------------

The MUD library is a bundle of services added to the driver, usually to add game features.


The `qtmud` Command
-------------------

The MUD driver - and its library - are most often accessed through the `qtmud` command.

********************************
Server Administration Operations
********************************

.. _manual-of-qtmud-development#install-the-codebase-locally:

Install the Codebase Locally
============================

To install the latest stable version::
  pip install qtmud

To install the current development version::
  pip install --user git+ssh://git@github.com/emsenn/qtmud.git@development

.. todo:: Write real instructions for installing qtMUD.  

**********************
Development Operations
**********************

Development Flow
================

Whitelabeling
=============

This section contains a step-by-step for changing qtMUD's name to
something else, across the codebase.

.. warning:: These instructions are incomplete and following them may
             leave you with a non-functioning codebase.

1) Change the name of the ``./qtmud`` folder.
2) Change the name of the modules imported near the top of ``./qtmud/__init__.py``
3) Change the name in setup.py
4) ``./docs/conf.py``
5) ``./qtmud/scripts/``

.. warning:: These instructions are incomplete.  Even if they were
             complete, they wouldn't capture the numerous instances
             where qtMUD is mentioned by-name in the documentation:
             replacing that text is left as an exercise between you
             and your text editor.
