"""
----------------------------------------------------------------------------
    ##     ##        ###        ########
    ###   ###       ## ##       ##     ##
    #### ####      ##   ##      ##     ##
    ## ### ##     ##     ##     ##     ##
    ##     ##     #########     ##     ##
    ##     ## ### ##     ## ### ##     ## ###
    ##     ## ### ##     ## ### ########  ###

MAD - M1ch3al Autonomous Drone

Author: SIROLA RENATO
 Email: renato.sirola@gmail.com
----------------------------------------------------------------------------
"""

from setuptools import setup

setup(
    name='MAD',
    version='0.1',
    description='MAD - M1ch3al Autonomous Drone',
    author='Renato Sirola',
    author_email='renato.sirola@gmail.com',
    license='Internal',
    package_data={
        'mad.drone.application.configurations': ['*.yaml'],
        'mad.drone.application.configurations.sensors': ['*.yaml'],
    },
    zip_safe=False,
    package_dir={'': '.'},
    install_requires=[
        'PyYAML',
        'pypubsub',
        'pyserial',
      ],
    packages=['mad',
              'mad.gui',
              'mad.drone',
              'mad.drone.application',
              'mad.drone.application.configurations',
              'mad.drone.application.configurations.sensors',
              'mad.drone.core',
              'mad.drone.sensors',
              'mad.drone.utils',
              'mad.tests'
              ]
)






