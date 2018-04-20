# -*- coding: utf-8 -*-
# Generated from confluin/parser/spequation.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and '.' in __name__:
    from .spequationParser import spequationParser
else:
    from spequationParser import spequationParser

# This class defines a complete listener for a parse tree produced by spequationParser.


class spequationListener(ParseTreeListener):

    # Enter a parse tree produced by spequationParser#spec.
    def enterSpec(self, ctx: spequationParser.SpecContext):
        pass

    # Exit a parse tree produced by spequationParser#spec.
    def exitSpec(self, ctx: spequationParser.SpecContext):
        pass

    # Enter a parse tree produced by spequationParser#functions.
    def enterFunctions(self, ctx: spequationParser.FunctionsContext):
        pass

    # Exit a parse tree produced by spequationParser#functions.
    def exitFunctions(self, ctx: spequationParser.FunctionsContext):
        pass

    # Enter a parse tree produced by spequationParser#function.
    def enterFunction(self, ctx: spequationParser.FunctionContext):
        pass

    # Exit a parse tree produced by spequationParser#function.
    def exitFunction(self, ctx: spequationParser.FunctionContext):
        pass

    # Enter a parse tree produced by spequationParser#arity.
    def enterArity(self, ctx: spequationParser.ArityContext):
        pass

    # Exit a parse tree produced by spequationParser#arity.
    def exitArity(self, ctx: spequationParser.ArityContext):
        pass

    # Enter a parse tree produced by spequationParser#name.
    def enterName(self, ctx: spequationParser.NameContext):
        pass

    # Exit a parse tree produced by spequationParser#name.
    def exitName(self, ctx: spequationParser.NameContext):
        pass

    # Enter a parse tree produced by spequationParser#equations.
    def enterEquations(self, ctx: spequationParser.EquationsContext):
        pass

    # Exit a parse tree produced by spequationParser#equations.
    def exitEquations(self, ctx: spequationParser.EquationsContext):
        pass

    # Enter a parse tree produced by spequationParser#equation.
    def enterEquation(self, ctx: spequationParser.EquationContext):
        pass

    # Exit a parse tree produced by spequationParser#equation.
    def exitEquation(self, ctx: spequationParser.EquationContext):
        pass

    # Enter a parse tree produced by spequationParser#term.
    def enterTerm(self, ctx: spequationParser.TermContext):
        pass

    # Exit a parse tree produced by spequationParser#term.
    def exitTerm(self, ctx: spequationParser.TermContext):
        pass

    # Enter a parse tree produced by spequationParser#base.
    def enterBase(self, ctx: spequationParser.BaseContext):
        pass

    # Exit a parse tree produced by spequationParser#base.
    def exitBase(self, ctx: spequationParser.BaseContext):
        pass

    # Enter a parse tree produced by spequationParser#application.
    def enterApplication(self, ctx: spequationParser.ApplicationContext):
        pass

    # Exit a parse tree produced by spequationParser#application.
    def exitApplication(self, ctx: spequationParser.ApplicationContext):
        pass
