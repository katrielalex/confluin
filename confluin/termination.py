# -*- coding: utf-8 -*-
import jinja2
import logging
import subprocess
import tempfile


log = logging.getLogger('confluin.termination')


template = jinja2.Environment(
    autoescape=True,
    loader=jinja2.BaseLoader(),
).from_string("""
fmod CONFLUIN is
    sort Msg .

    {% for op, arity in ops.items() -%}
    op {{ op }} {{ "_ " * arity }}: {{ "Msg " * arity }} -> Msg .
    {% endfor %}
    vars{% for v in vars %} {{ v }}{% endfor %}: Msg .
    {% for eq in eqs %}
    eq {{ eq }} .
    {% endfor %}
endfm
""")


def render(symbols):
    mutermify = str.maketrans('(,)', ' ' * 3)
    return template.render(
        ops=symbols.functions,
        vars=symbols.bases,
        eqs={eq.translate(mutermify) for eq in symbols.equations},
    )


def check(symbols, muterm):
    with tempfile.NamedTemporaryFile(buffering=False, suffix='.maude') as f:
        rendered = render(symbols)
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
