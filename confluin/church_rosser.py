# -*- coding: utf-8 -*-
import logging
import pexpect


from . import renderer


log = logging.getLogger('confluin.termination')


def check(symbols, maude, mfe):
    rendered = renderer.render(symbols)

    maude = pexpect.spawn(f'{maude} {mfe}')

    def do(*cmds):
        for cmd in cmds:
            maude.sendline(cmd)
        maude.expect('Maude>')
        log.debug('Maude: {}'.format(maude.before.decode()))

    # wait to load mfe, and check the right maude version
    do('')
    assert 'Maude 2.6' in maude.before.decode(
    ), "mfe doesn't work with Maude 2.7, apparently"

    do('( select tool CRC . )')
    do('( set include BOOL off . )')
    do('(', *rendered.splitlines(), ')')
    do('( check Church-Rosser .) ')

    important_facts = {
        'The specification is locally-confluent.',
        'All critical pairs have been joined.',
        'The module is sort-decreasing.',
    }

    assert all(fact in maude.before.decode() for fact in important_facts), \
        'Maude failed to prove Church-Rosser'
