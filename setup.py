# -*- coding: utf-8 -*-
import os
import setuptools
import sys

assert sys.version_info.major > 2, 'Use Python 3 to run this setup.py. Thanks, antlr.'

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.rst')) as readme:
    long_description = readme.read()

setuptools.setup(
    name='confluin',
    version='0.1.0',
    url='https://github.com/katrielalex/confluin',

    author='Katriel Cohn-Gordon',
    author_email='me@katriel.co.uk',

    description='A confluence checker for Tamarin equational theories',
    long_description=long_description,

    packages=setuptools.find_packages(),

    install_requires=[
        'attrs',
        'antlr4-python3-runtime',
        'click',
        'coloredlogs',
        'jinja2',
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3',
    ],

    entry_points={
        'console_scripts': [
            'confluin=confluin:main',
        ],
    },
)
