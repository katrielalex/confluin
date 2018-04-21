# -*- coding: utf-8 -*-
import jinja2
import logging


log = logging.getLogger('confluin.renderer')


template = jinja2.Environment(
    autoescape=True,
    loader=jinja2.BaseLoader(),
).from_string("""
fmod CONFLUIN is
    sort Msg .

    {% for op, arity in ops.items() -%}
    op {{ op }} {% if underscores %}{{ "_ " * arity }}{% endif %} : {{ "Msg " * arity }} -> Msg .
    {% endfor %}
    vars{% for v in vars %} {{ v }}{% endfor %} : Msg .
    {% for eq in eqs %}
    eq {{ eq }} .
    {% endfor %}
endfm
""")


def render(symbols, muterm=False):
    if muterm:
        use_underscores = True
        mutermify = str.maketrans('(,)', ' ' * 3)
        eqs = {eq.translate(mutermify) for eq in symbols.equations}
    else:
        use_underscores = False
        eqs = symbols.equations

    return template.render(
        ops=symbols.functions,
        vars=symbols.bases,
        eqs=eqs,
        underscores=use_underscores,
    )
