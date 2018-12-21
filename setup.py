from setuptools import setup

setup(name='qtMUD', version='0.1.0',
      description='A driver for running a MUD server.',
      long_description=('qtMUD is a driver for running a multi-user '
                        'dungeon, or MUD: a server for hosting a '
                        '(typically) text-driver multi-client '
                        'service, usually a game.'),
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: No Input/Output (Daemon)',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Education',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3.7',
                   'Topic :: Communications :: Chat',
                   'Topic :: Games/Entertainment :: Multi-User Dungeons (MUD)',
                   ],
      keywords='mud mmo mmorpg game',
      url='http://qtmud.readthedocs.io/en/latest/',
      author='emsenn',
      author_email='emsenn@emsenn.net',
      license='MIT',
      packages=setuptools.find_packages(),
      extras_require={
          'colored_output': ['termcolor'],
      },
      include_package_data=True,
      zip_safe=False,
      test_suite='tests',
      entry_points='''
        [console_scripts]
        qtmud=qtmud.scripts:qtmud
      ''')

