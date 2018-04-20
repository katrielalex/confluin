# -*- coding: utf-8 -*-
# Generated from confluin/parser/spequation.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write('\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17')
        buf.write('Q\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7')
        buf.write('\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16')
        buf.write('\t\16\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3')
        buf.write('\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3')
        buf.write('\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\6\nA\n\n\r\n\16')
        buf.write('\nB\3\n\3\n\3\13\3\13\3\f\3\f\3\r\6\rL\n\r\r\r\16\rM\3')
        buf.write('\16\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23')
        buf.write("\13\25\f\27\r\31\16\33\17\3\2\3\5\2\13\13\17\17\"\"\2")
        buf.write('R\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13')
        buf.write('\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3')
        buf.write('\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2')
        buf.write('\2\2\3\35\3\2\2\2\5(\3\2\2\2\7*\3\2\2\2\t,\3\2\2\2\13')
        buf.write('\67\3\2\2\2\r9\3\2\2\2\17;\3\2\2\2\21=\3\2\2\2\23@\3\2')
        buf.write('\2\2\25F\3\2\2\2\27H\3\2\2\2\31K\3\2\2\2\33O\3\2\2\2\35')
        buf.write("\36\7h\2\2\36\37\7w\2\2\37 \7p\2\2 !\7e\2\2!\"\7v\2\2")
        buf.write("\"#\7k\2\2#$\7q\2\2$%\7p\2\2%&\7u\2\2&\'\7<\2\2\'\4\3")
        buf.write('\2\2\2()\7.\2\2)\6\3\2\2\2*+\7\61\2\2+\b\3\2\2\2,-\7g')
        buf.write('\2\2-.\7s\2\2./\7w\2\2/\60\7c\2\2\60\61\7v\2\2\61\62\7')
        buf.write('k\2\2\62\63\7q\2\2\63\64\7p\2\2\64\65\7u\2\2\65\66\7<')
        buf.write('\2\2\66\n\3\2\2\2\678\7?\2\28\f\3\2\2\29:\7*\2\2:\16\3')
        buf.write('\2\2\2;<\7+\2\2<\20\3\2\2\2=>\7\f\2\2>\22\3\2\2\2?A\t')
        buf.write('\2\2\2@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2BC\3\2\2\2CD\3\2\2')
        buf.write('\2DE\b\n\2\2E\24\3\2\2\2FG\4C\\\2G\26\3\2\2\2HI\4c|\2')
        buf.write('I\30\3\2\2\2JL\5\33\16\2KJ\3\2\2\2LM\3\2\2\2MK\3\2\2\2')
        buf.write('MN\3\2\2\2N\32\3\2\2\2OP\4\62;\2P\34\3\2\2\2\5\2BM\3\b')
        buf.write('\2\2')
        return buf.getvalue()


class spequationLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    EOL = 8
    WS = 9
    UPPER = 10
    LOWER = 11
    INTEGER = 12
    DIGIT = 13

    channelNames = [u'DEFAULT_TOKEN_CHANNEL', u'HIDDEN']

    modeNames = ['DEFAULT_MODE']

    literalNames = [
        '<INVALID>',
        "'functions:'", "','", "'/'", "'equations:'", "'='", "'('",
        "')'", "'\n'",
    ]

    symbolicNames = [
        '<INVALID>',
        'EOL', 'WS', 'UPPER', 'LOWER', 'INTEGER', 'DIGIT',
    ]

    ruleNames = [
        'T__0', 'T__1', 'T__2', 'T__3', 'T__4', 'T__5', 'T__6',
        'EOL', 'WS', 'UPPER', 'LOWER', 'INTEGER', 'DIGIT',
    ]

    grammarFileName = 'spequation.g4'

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion('4.7.1')
        self._interp = LexerATNSimulator(
            self, self.atn, self.decisionsToDFA, PredictionContextCache(),
        )
        self._actions = None
        self._predicates = None
