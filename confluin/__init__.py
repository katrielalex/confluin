# -*- coding: utf-8 -*-
"""confluin - A confluence checker for Tamarin equational theories"""

__version__ = '0.1.0'
__author__ = 'Katriel Cohn-Gordon <me@katriel.co.uk>'
__all__ = []


import click
import distutils.spawn
import logging
import re


from . import parser


valid_bin = click.Path(
    exists=True, file_okay=True,
    dir_okay=False, resolve_path=True,
)


@click.command()
@click.version_option()
@click.argument('spthy', type=click.File())
@click.option('--maude', help='Path to `maude` binary', type=valid_bin)
def main(spthy, maude):
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__package__)
    logger.info('Hello, world!')

    if maude is None:
        maude = distutils.spawn.find_executable('maude')
    assert maude is not None, 'Cannot find maude. Consider passing --maude=/path/to/maude.'

    relevant_line = re.compile('^(functions:|equations:).*$')
    parser.parse(line.split('//')[0].strip()
                 for line in spthy if relevant_line.match(line))
