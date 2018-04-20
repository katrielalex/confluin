# -*- coding: utf-8 -*-
"""confluin - A confluence checker for Tamarin equational theories"""

__version__ = '0.1.0'
__author__ = 'Katriel Cohn-Gordon <me@katriel.co.uk>'
__all__ = []


import click
import logging


@click.command()
@click.version_option()
def main():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__package__)
    logger.info('Hello, world!')
