###########################
Manual of qtMUD Development
###########################

This manual is intended as a comprehensive reference for the
maintainance and development of qtMUD, as a codebase and as a project.

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

Since this part of the manual is ultimately about learning to work
with the codebase, I'll let the documentation of those functions -
hopefully - speak for itself.  You should get used to reading this
type of documentation: you'll be encouraged to write it for any code
you write.

.. autofunction:: qtmud.Driver.load

The MUD Library
---------------

The MUD library is a bundle of services added to the driver, usually to add game features.


The `qtmud` Command
-------------------

The MUD driver - and its library - are most often accessed through the `qtmud` command.



********************
Source Documentation
********************

This section contains the documentation written into the qtMUD source code.

.. _qtmud-command:

``qtmud`` Command
=================

.. click:: qtmud.scripts.qtmud_service:qtmud
   :prog: qtmud
   :show-nested:


``qtmud`` module
================

.. automodule:: qtmud
    :members:
    :undoc-members:
    :show-inheritance:

``qtmud.thing`` module
======================
       
.. automodule:: qtmud.thing
    :members:
    :undoc-members:
    :show-inheritance:
