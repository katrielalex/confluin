# -*- coding: utf-8 -*-
"""confluin - A confluence checker for Tamarin equational theories"""

__version__ = '0.1.0'
__author__ = 'Katriel Cohn-Gordon <me@katriel.co.uk>'
__all__ = []


import click
import coloredlogs
import distutils.spawn
import logging
import re


from . import parser
from . import termination

valid_bin = click.Path(
    exists=True,
    file_okay=True,
    dir_okay=False,
    resolve_path=True,
)


@click.command()
@click.version_option()
@click.argument('spthy', type=click.File())
@click.option('--maude', help='Path to `maude` binary', type=valid_bin)
@click.option('--muterm', help='Path to `muterm` binary', type=valid_bin)
@click.option('--debug', is_flag=True)
def main(spthy, maude, muterm, debug):
    coloredlogs.install(level='DEBUG' if debug else 'INFO')
    log = logging.getLogger(__package__)

    if maude is None:
        maude = distutils.spawn.find_executable('maude')
    assert maude is not None, 'Cannot find maude. Consider passing --maude=/path/to/maude.'

    if muterm is None:
        muterm = distutils.spawn.find_executable('muterm')
    assert muterm is not None, 'Cannot find muterm. Consider passing --muterm=/path/to/muterm.'

    relevant_line = re.compile('^(functions:|equations:).*$')
    symbols = parser.parse(line.split('//')[0].strip()
                           for line in spthy if relevant_line.match(line))

    termination.check(symbols, muterm)
    log.info('Termination check (using muterm) succeeded!')
