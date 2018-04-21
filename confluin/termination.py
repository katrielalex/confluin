# -*- coding: utf-8 -*-
import logging
import subprocess
import tempfile


from . import renderer


log = logging.getLogger('confluin.termination')


def check(symbols, muterm):
    with tempfile.NamedTemporaryFile(buffering=False, suffix='.maude') as f:
        rendered = renderer.render(symbols, muterm=True)
        log.debug('Rendered template: \n%s', rendered)
        f.write(rendered.encode('ascii'))
        result = subprocess.run(
            [muterm, '-i', f.name],
            check=True,
            stdout=subprocess.PIPE,
        )

    log.debug('Muterm result: \n{}'.format(result.stdout.decode('ascii')))
    assert result.stdout.startswith(
        b'YES',
    ), 'Termination check failed. Thanks, muterm!'
