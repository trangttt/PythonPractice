import re
import unittest
from collections import namedtuple
import sys


###########################################################
#           TOKENIZING
##########################################################

Token = namedtuple('Token', ['typ', 'value', 'pos'])


def tokenize(prob):
    keywords = ['AND', 'OR', 'NOT']
    token_specification = [
        ('ID', r'[a-zA-Z]+'),   #Identifiers
        ('LBRACKET', r'[(]'),      #Left bracket
        ('RBRACKET', r'[)]'),      #Right bracket
        ('SKIP', r'[ \t]+'),    #skipping whitespace and tabs
        ('MISMATCH', r'.')      #Any other character
    ]

    tok_regex = "|".join("(?P<{}>{})".format(*pair) for pair in token_specification)
    result = []
    for mo in re.finditer(tok_regex, prob):
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind == 'ID' and value in keywords:
            kind = value
        if kind == 'SKIP':
            continue
        if kind == 'MISMATCH':
            raise RuntimeError('{} Unexpected at col {}'.format(value, mo.start()))
        result.append(Token(kind, value, mo.start()))
    return result


###########################################################
#           PARSER UTILITIES
##########################################################
class Result(object):
    """Storing result from parsing
    """
    def __init__(self, value, position):
       self.__value__  = value
       self.__position__ = position

    @property
    def value(self):
        return self.__value__

    @property
    def pos(self):
        return self.__position__

    def __str__(self):
        return "Result ({}, {})".format(self.__value__, self.__position__)

class Equality(object):
    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
            self.__dict__ == other.__dict__

    def __neq__(self, other):
        return not self.__eq__(other)

class Parser(Equality):
    """Basic parser with basic operator
    """""
    def __call__(self, tokens, pos):
        pass

    def __add__(self, other):
        return Concat(self, other)

    def __mul__(self, other):
        return Exp(self, other)

    def __or__(self, other):
        return Alternate(self, other)

    def __xor__(self, function):
        return Process(self, function)

class Concat(Parser):
    """
    Parser that returns the concatenation of results from two parsers
    """
    def __init__(self, left, right):
        self.__left__ = left
        self.__right__ = right

    def __call__(self, tokens, pos):
        left_result = self.__left__(tokens, pos)
        if left_result:
            right_result = self.__right__(tokens, left_result.pos)
            combined_result = (left_result.value, right_result.value)
            return Result(combined_result, right_result.pos)
        return None

class Alternate(Parser):
    """Parser that takes two parser
    It applies the first parser, and return the result if success
    Otherwise, it applies the second parser
    """
    def __init__(self, left, right):
       self.__left__ = left
       self.__right__ = right

    def __call__(self, tokens, pos):
        left_result = self.__left__(tokens, pos)
        if left_result:
            return left_result
        else:
            return self.__right__(tokens, pos)

class Exp(Parser):
    """Take two parsers
    It applies the first parser, and then the second parser
    The second parser returns a funtions showing how to combine the two result
    """
    def __init__(self, parser, separator):
        self.__parser__ = parser
        self.__separator__ = separator

    def __call__(self, tokens, pos):
        result = self.__parser__(tokens, pos)

        def process_next(parsed):
            (sep_func, right_value)  = parsed
            return sep_func(result.value, right_value)

        next_parser = self.__separator__ + self.__parser__ ^ process_next

        next_result = result
        while next_result:
            next_result = next_parser(tokens, result.pos)
            if next_result:
                result = next_result
        return result

class Process(Parser):
    """Parser takes one parser and one function
    It execute the parser, if sucess, applies the function on result"""
    def __init__(self, parser, function):
       self.__parser__ = parser
       self.__function__ = function

    def __call__(self, tokens, pos):
        result = self.__parser__(tokens, pos)
        if result :
            ret = self.__function__(result.value)
            if ret:
                return Result(ret, result.pos)
        return None

class Keyword(Parser):
    """parser that accepts keywords"""
    def __init__(self, value, tag):
        self.__value__ = value
        self.__tag__ = tag

    def __call__(self, tokens, pos):
        if len(tokens) > pos and \
                tokens[pos].value == self.__value__ and \
                tokens[pos].typ == self.__tag__:
            return Result(tokens[pos].value, pos+1)
        else: return None


class Tag(Parser):
    """
    Parser that accepts Identifiers
    """
    def __init__(self, tag):
        self.__tag__ = tag

    def __call__(self, tokens, pos):
        if len(tokens) > pos and \
                self.__tag__ == tokens[pos].typ:
            return Result(tokens[pos].value, pos+1)
        else: return None


class LazyParser(Parser):
    """LazyParser is used when defining recursive parse. It is used
    to postpone definition of parser until it is actually called"""
    def __init__(self, parser_function):
       self.__parser__ = None
       self.__parser_function__ = parser_function

    def __call__(self, tokens, pos):
        if self.__parser__ == None:
            self.__parser__ = self.__parser_function__()
        return self.__parser__(tokens, pos)


###########################################################
#           PARSER CONSTRUCTION
###########################################################

var_p = Tag("ID") ^ (lambda x: VarAST(x))

def process_binop(value):
    return lambda l, r: BinOpAST(value, l, r)

binop_p = Keyword("OR", "OR") | Keyword("AND", "AND")

lbr_p = Keyword("(", "LBRACKET")
rbr_p = Keyword(")", "RBRACKET")

def process_bracket_result(parsed):
    ((_, value), _) = parsed
    return value

def bracket_parser():
    return lbr_p + LazyParser(exp_parser) + rbr_p ^ process_bracket_result

def term_parser():
    return var_p | bracket_parser()

def exp_parser():
    return (term_parser() | not_parser()) * (binop_p ^ process_binop)

def not_parser():
    return Keyword("NOT", "NOT") + term_parser() ^ (lambda x: UniOpAST("NOT", x[1]))


###########################################################
#           ABSTRACT SYNTAX TREE
###########################################################

class VarAST(Equality):
    """Representing Variables"""
    def __init__(self, value):
        self.__value__ = value

    def __str__(self):
        return "(VarAST: {})".format(self.__value__)


class BinOpAST(Equality):
    """Binary Operation"""
    def __init__(self, value, left, right):
        self.__value__ = value
        self.__left__ = left
        self.__right__ = right

    def __str__(self):
        return "(BinOpAST : {}, {}, {})".format(self.__value__, self.__left__, \
                                                self.__right__ )

class UniOpAST(Equality):
    def __init__(self, value, right):
        self.__value__ = value
        self.__right__ = right

    def __str__(self):
        return "(UniOpAST : {}, {})".format(self.__value__, self.__right__)

###########################################################
#           RUNNING
###########################################################
if __name__ == "__main__":
    if len(sys.argv) > 1:
        exps = open(sys.argv[1]).readlines()
        for e in exps:
            res = exp_parser()(tokenize(e.strip('\n')), 0)
            print(res.value)

###########################################################
#           TESTING
###########################################################

class ParserTesting(unittest.TestCase):
    def test_primitive_parsers(self):
        str1 = "a"
        res1 = var_p(tokenize(str1), 0)
        self.assertEqual(res1.value, VarAST("a"))

        str2 = "NOT a"
        res2 = not_parser()(tokenize(str2), 0)
        self.assertEqual(res2.value, UniOpAST("NOT", VarAST("a")))

        str3 = "a AND b"
        res3 = exp_parser()(tokenize(str3), 0)
        self.assertEqual(res3.value, BinOpAST("AND", VarAST("a"), VarAST("b")))

        str4 = "a OR b"
        res4 = exp_parser()(tokenize(str4), 0)
        self.assertEqual(res4.value, BinOpAST("OR", VarAST("a"), VarAST("b")))

        str5 = "(a AND b) OR c"
        res5 = exp_parser()(tokenize(str5), 0)
        self.assertEqual(res5.value, \
                         BinOpAST("OR", BinOpAST("AND", VarAST("a"), VarAST("b")), VarAST("c")))


        str6 = "NOT (a OR b AND c) OR NOT (a AND NOT b )"
        res6 = exp_parser()(tokenize(str6), 0)
        print(res6.value)
