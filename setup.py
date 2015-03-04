#!/usr/bin/env python3

import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='podhub_follower',
    version='v0.0.1',
    packages=['podhub_follower'],
    include_package_data=True,
    license='BSD 3-Clause License',
    description='RSS client for PodHub',
    long_description=README,
    url='https://github.com/podhub/follower',
    author='Jon Chen',
    author_email='bsd@voltaire.sh',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    requires=[
        'feedparser==5.1.3'
    ]
)
