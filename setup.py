#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__authors__ = "Jordan Ovrè, Paul Duncan"
__copyright__ = "Copyright (c) ImmunIT - Jordan Ovrè / Paul Duncan"
__license__ = "Apache 2.0"
__version__ = "1.0.0"
__contact__ = "Jordan Ovrè / Ghecko <jovre@immunit.ch>, Paul Duncan / Eresse <pduncan@immunit.ch>"

description = 'Octowire library'
name = 'octowire'


setup(
    name=name,
    version=__version__,
    packages=find_packages(),
    license=__license__,
    description=description,
    author=__authors__,
    zip_safe=True,
    url='https://github.com/immunIT/octowire-lib/',
    download_url = 'https://github.com/immunIT/octowire-lib/archive/1.0.0.tar.gz',
    install_requires=[
        'pyserial>=3.4,<4',
        'beautifultable>=0.8.0'
        'colorama; platform_system == "Windows"'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable'
    ],
    keywords=['octowire', 'library', 'hardware', 'security', 'pentest'],
)
