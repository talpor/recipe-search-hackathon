#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import recipe-search
version = recipe-search.__version__

setup(
    name='recipe-search',
    version=version,
    author="German Jaber",
    author_email='gjaber@talpor.com',
    packages=[
        'recipe-search',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.4',
    ],
    zip_safe=False,
    scripts=['recipe-search/manage.py'],
)
