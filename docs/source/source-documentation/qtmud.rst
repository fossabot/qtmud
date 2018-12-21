#############
qtMUD Package
#############

The qtMUD package - ``qtmud`` - is what qtMUD *is*: it's how
it's implemented.

.. note:: To learn how to install the qtMUD package on your
	  system, see the :ref:`"Install the Codebase Locally"
	  <manual-of-qtmud-development#install-the-codebase-locally>`
	  section of the
	  :ref:`manual-of-qtmud-development`.)

The qtMUD package contains the main qtMUD module, documented
below, and the following subpackages:

.. toctree::
   :maxdepth: 1
		
   qtmud.services
	       
qtMUD Module
============

.. automodule:: qtmud
   :members: __name__, __version__, feature_data, logging_config
   :undoc-members:
   :show-inheritance:

The Driver
----------

also known as...

.. autoclass:: qtmud.Driver
   :members: __name__, __version__, log, thing_template

``load``
^^^^^^^^

.. automethod:: qtmud.Driver.load

``start``
^^^^^^^^^

.. automethod:: qtmud.Driver.start

``run``
^^^^^^^

.. automethod:: qtmud.Driver.run

``tick``
^^^^^^^^

.. automethod:: qtmud.Driver.tick

``schedule``
^^^^^^^^^^^^

.. automethod:: qtmud.Driver.schedule
		
``load_service``
^^^^^^^^^^^^^^^^

.. automethod:: qtmud.Driver.load_service
   
``create_class_instance_by_name()``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automethod:: qtmud.Driver.create_class_instance_by_name

