#####################
Developing with qtMUD
#####################

qtMUD is meant to be used as a framework for developing your own MUD. This
document contains an explanation of how qtMUD works, as well as detailed
explanations of our development process and some tutorials on how to expand
the library.


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

:func:`qtmud.load` populates::

    qtmud        INFO     filling qtmud.client_accounts from ./qtmud_client_accounts.p
    qtmud        INFO     start()ing active_services
    qtmud        INFO     talker start()ed
    qtmud        INFO     start()ing MUDSocket
    qtmud        INFO     MUDSocket successfully bound to ('localhost', 5787)
    qtmud        INFO     MUDSocket successfully bound to ('localhost', 5788, 0, 0)
    qtmud        INFO     mudsocket start()ed
    qtmud        INFO     qtmud.run()ning


Development Flow
################

This section is intended to be an outline of the steps that I take to bring a
part of qtMUD from idea to release. Each section is, roughly, broken up by
the console command used to handle the task.


GitHub Issues
=============

.. todo:: Coming by 0.1.0!


Flow Feature Start
==================
::

    $ git flow feature start womble

This creates a new git branch, ``feature/womble``, based on the ``develop``
branch. Once you're on the feature branch, you can make whatever changes to
the code you want. Let's pretend I added a womble method to
:mod:`qtmud.cmds`. Once I'm done writing it, I'll want to go ahead and run::

    $ python setup.py test

Even though I haven't written any test cases for my code (yet), it's still a
good idea to check and make sure your changes didn't inadvertently break
something existing. Once you're sure your code doesn't hurt existing
functionality, you can go ahead and commit the changes.


Git Commit
==========
::

    action: [audience:] Summary Of Commit [!tag]

In order to use `git-changelog <https://github.com/vaab/gitchangelog>`_ qtMUD
commit messages have a specific format:

* ``action`` represents what purpose the commit serves and is one of:
* * ``chg`` - You've refactored existing code, removed technical debt, or
    expanded test coverage
* * ``fix`` - You've fixed an issue. Ideally, prove the GitHub Issue # in the
    summary.
* * ``new`` - You've added new features, documentation, or test cases.

----

* ``audience`` represents who would care about the change
* * ``dev`` - API revisions/additions, refactors
* * ``usr`` - Client experience revisions/additions
* * ``pkg`` - Packaging/metadata revisions/additions
* * ``test`` - Test case revisions/additions
* * ``doc`` - documentation revisions/additions

----

* ``Summary Of Commit`` is a short (very short) summary of what the commit
  does. If you find yourself struggling to come up with this, you probably
  should be committing more frequently. Capitalize every word, unless it
  references a part of the code which is not capitalized.

----

* Each ``tag`` should be prefixed with an exclamation point, and should be
  one of:
* * ``!refactor`` marks that the commit deals with existing code.
* * ``!minor`` marks that the commit has a very minor change - adding a
    one-line comment or fixing a typo.
* * ``!cosmetic`` marks a commit as dealing with code practice adhesion -
    fixing pep8 violations or other small stuff
* * ``!wip`` marks a commit as being a work-in-progress - the committed code is
    functional, but doesn't contain all of the eventual changes the function
    will require.

If it wasn't clear from the tags, commits should have a single thing that
they deal with.  My commit for my new ``womble`` command might look something
like this::

    $ git commit -m "new: usr: Addition Of womble To qtmud.cmds !wip"

Once you've committed the functional code, it's time to test it.


Unittests
=========
::

    from unittest import TestCase
    import qtmud

    class TestWomble(TestCase):
    def test_Womble(self):
        cmd = cmds.womble
        client = qtmud.Client()
        self.assertTrue(cmd(client))

qtMUD uses `unittest <https://docs.python.org/3/library/unittest.html>`_ for
testing. For a more comprehensive guide on how to write qtMUD unittests,
check the respective tutorials for commands, subscriptions, and services.

I use `coverage <https://pypi.python.org/pypi/coverage>`_ to make sure my test
cases are comprehensive, and strongly suggest you do the same::

    $ coverage run setup.py test
    $ coverage report
    $ coverage annotate qtmud/cmds.py

I change and expand my test cases until the things I changed in this feature
are properly covered. Once my test cases are built, I'll want to go ahead and do
another commit::

    $ git commit -m "new: test: Test Cases For qtmud.cmds.womble !wip"


Pylint
======
::

    $ pylint -rn ./qtmud/cmds.py ./tests/test_cmds.py

Now that the ``womble`` command has been written, and we have tests to verify
it works, it's time to make sure the addition follows good Python practices.


Documentation
=============

D

::

    $ cd ./docs && make html

After you've linted your code, build the html documentation (goes into
./docs/build/html by default) and look for any errors caused by your docstrings.

Flow Feature Finish
===================
::

    $ git flow feature finish womble

Flow Release Start
==================
::

    $ git flow release start 0.0.4
    $ gitchangelog > ./docs/source/changelog.rst
    $ cd ./docs && make html && cd ..

Also, manually (for now) change the version in these three locations:
* ``docs/conf.py``
* ``qtmud/__init__.py``
* ``setup.py``


Flow Release Finish
===================
::

    $ git flow release finish 0.0.4
    $ python setup.py sdist bdist_wheel upload
    $ git push --all

The end!

Making & Using Things
#####################

.. todo:: Coming by version 0.1.0!

Making & Using Subscriptions
############################

.. todo:: Coming by version 0.1.0!

Making & Using Services
#######################

Changelog
#########

.. toctree::
    :maxdepth: 3

    changelog