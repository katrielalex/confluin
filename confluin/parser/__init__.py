# -*- coding: utf-8 -*-
import antlr4
import logging


from .spequationLexer import spequationLexer as Lexer
from .spequationParser import spequationParser as Parser


log = logging.getLogger('confluin.parser')


def parse(s):
    text = '\n'.join(s)
    logging.info(text)
    input_stream = antlr4.InputStream(text)
    lexer = Lexer(input_stream)
    token_stream = antlr4.CommonTokenStream(lexer)
    parser = Parser(token_stream)
    # parser._errHandler = antlr4.error.ErrorStrategy.BailErrorStrategy()

    spec = parser.spec()
    functions = {}
    for fs in spec.functions():
        for f in fs.function():
            functions[f.name().getText()] = f.arity().getText()

    equations = {}
    for es in spec.equations():
        for e in es.equation():
            pass

    return functions, equations
