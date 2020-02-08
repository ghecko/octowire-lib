#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__authors__ = "Jordan Ovrè, Paul Duncan"
__copyright__ = "Copyright (c) Jordan Ovrè / Paul Duncan"
__license__ = "GPLv3"
__version__ = "0.0.1"
__contact__ = "Jordan Ovrè / Ghecko <ghecko78@gmail.com>, Paul Duncan / Eresse <eresse@dooba.io>"

description = 'Octowire library'
name = 'octowire'


setup(
    name=name,
    version=__version__,
    packages=find_packages(),
    license=__license__,
    description=description,
    author=__authors__,
    url='https://bitbucket.org/dooba_core/octowire-lib/',
    install_requires=[
        'pyserial>=3.4,<4',
        'tabulate>=0.8.6,<1'
    ],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha'
    ],
    keywords=['octowire', 'library', 'hardware', 'security', 'pentest'],
)
