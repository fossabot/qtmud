.. _manual-of-qtmud-development:

###########################
Manual of qtMUD Development
###########################

This manual is intended as a comprehensive reference for the
maintainance and development of qtMUD, as a codebase and as a
project.  It assumes you're familiar with
:ref:`project-information`.

It does *not* assume that you're familiar with Python, the
programming language the codebase is written in.

************
Introduction
************

This section hopes to explain some of the concepts that are
important to understanding the qtMUD driver - such as what a
"driver" is:

The qtMUD **driver** is the "engine" that lets a MUD happen.
In qtMUD, the driver's main responsibility is maintaining
four records:

- A record of **loaded services**, which can control on-going
  driver operations.  Services are loaded when the driver is
  :meth:`loaded <qtmud.Driver.load>`.
- A record of **loaded subscriptions**, which do things when
  called by a relevant *event*.  Services list their
  subscriptions, and they're loaded when the service is.
- A record of **events**, which are subscriptions to be called
  each time the driver *ticks*.  Events are added by service
  ticks or subscriptions.
- A records of **instanced things**, which are in-game
  objects: everything from player avatars to rooms to spells.
  Things are instanced by service ticks or subscriptions.



********************************
Server Administration Operations
********************************

.. _manual-of-qtmud-development#install-the-codebase-locally:

Install the Codebase Locally
============================

To install the latest stable version::
  pip install qtmud

To install the current development version::
  pip install --user \
  git+ssh://git@github.com/emsenn/qtmud.git@development

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
