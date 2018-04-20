# -*- coding: utf-8 -*-
import attr
import antlr4
import logging


from .spequationLexer import spequationLexer as Lexer
from .spequationListener import spequationListener as Listener
from .spequationParser import spequationParser as Parser


log = logging.getLogger('confluin.parser')


@attr.s
class Collector(Listener):
    functions = attr.ib(default=attr.Factory(dict))
    equations = attr.ib(default=attr.Factory(set))
    _bases = attr.ib(default=attr.Factory(set))

    def enterFunction(self, ctx):
        self.functions[ctx.name().getText()] = int(ctx.arity().getText())

    def enterEquation(self, ctx):
        self.equations.add(ctx.getText())

    def enterBase(self, ctx):
        self._bases.add(ctx.getText())

    @property
    def bases(self):
        return self._bases - self.functions.keys()


def parse(s):
    lexer = Lexer(antlr4.InputStream('\n'.join(s)))
    parser = Parser(antlr4.CommonTokenStream(lexer))
    # parser._errHandler = antlr4.error.ErrorStrategy.BailErrorStrategy()

    symbols = Collector()
    antlr4.ParseTreeWalker().walk(symbols, parser.spec())

    return symbols
