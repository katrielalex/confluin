# -*- coding: utf-8 -*-
import setuptools

setuptools.setup(
    name='confluin',
    version='0.1.0',
    url='https://github.com/katrielalex/confluin',

    author='Katriel Cohn-Gordon',
    author_email='me@katriel.co.uk',

    description='A confluence checker for Tamarin equational theories',
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=['click'],

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
