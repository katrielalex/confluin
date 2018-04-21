# -*- coding: utf-8 -*-
"""confluin - A confluence checker for Tamarin equational theories"""

__version__ = '0.1.0'
__author__ = 'Katriel Cohn-Gordon <me@katriel.co.uk>'
__all__ = []


import click
import coloredlogs
import distutils.spawn
import logging
import os
import pylocated
import re
import sys


from . import parser
from . import termination
from . import church_rosser

valid_bin = click.Path(
    exists=True,
    file_okay=True,
    dir_okay=False,
    resolve_path=True,
)
log = logging.getLogger(__package__)


def locate(f, advice):
    if advice is not None:
        return advice

    advice = distutils.spawn.find_executable(f)
    if advice is not None:
        log.debug('Using %s for %s', advice, f)
        return advice

    advice = pylocated.locatedb.find(f).getvalue().splitlines()
    if advice:
        for guess in advice:
            if os.path.basename(guess) == f and os.path.isfile(guess):
                log.info('Guessing %s for %s', guess, f)
                return guess

    log.fatal(f'Could not find {f}, quitting. Consider passing --{f}.')
    sys.exit(1)


@click.command()
@click.version_option()
@click.argument('spthy', type=click.File())
@click.option('--maude', help='Path to `maude` binary', type=valid_bin)
@click.option('--muterm', help='Path to `muterm` binary', type=valid_bin)
@click.option('--mfe', help='Path to `mfe.maude`', type=valid_bin)
@click.option('--debug', is_flag=True)
def main(spthy, maude, muterm, mfe, debug):
    coloredlogs.install(level='DEBUG' if debug else 'INFO')

    maude = locate('maude', maude)
    muterm = locate('muterm', muterm)
    mfe = locate('mfe', mfe)

    relevant_line = re.compile('^(functions:|equations:).*$')
    symbols = parser.parse(line.split('//')[0].strip()
                           for line in spthy if relevant_line.match(line))

    termination.check(symbols, muterm)
    log.info('Termination check (using muterm) succeeded!')

    church_rosser.check(symbols, maude, mfe)
    log.info('Church-Rosser check (using Maude 2.6 and MFE) succeeded!')
