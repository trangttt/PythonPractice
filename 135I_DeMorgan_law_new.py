import unittest
import sys
import collections
import re


Token = collections.namedtuple('Token', ['typ', 'value', 'pos'])

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
    for mo in re.finditer(tok_regex, prob):
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind == 'ID' and value in keywords:
            kind = value
        if kind == 'SKIP':
            continue
        if kind == 'MISMATCH':
            raise RuntimeError('{} Unexpected at col {}'.format(value, mo.start()))
        yield Token(kind, value, mo.start())
        #result.append(Token(kind, value, mo.start()))
    #return result

class ExprAST:
    def negate(self):
        pass

class BinOpExprAST(ExprAST):
    def __init__(self, op, lhs, rhs):
        self._op = op
        self._lhs = lhs
        self._rhs = rhs

    def negate(self):
        if self._op == 'AND':
           return BinOpExprAST('OR', self._lhs.negate(), self._rhs.negate())
        elif self._op == 'OR':
            return BinOpExprAST('AND', self._lhs.negate(), self._rhs.negate())
        else :
            raise BinOpError("Unknown Operation {}".format(self._op))
            return 0

    def __str__(self):
        #return "BinOp : ({} {} {})".format(self._op, self._lhs, self._rhs)
        return "({}) {} ({})".format(self._lhs, self._op, self._rhs)

class UniOpExpAST(ExprAST):
    def __init__(self, op, rhs):
        self._op = op
        self._rhs = rhs

    def negate(self):
        return self._rhs

    def __str__(self):
        #return "UniOp : ({} {})".format(self._op, self._rhs)
        return "{} ({})".format(self._op, self._rhs)


class VariableExprAST(ExprAST):
    def __init__(self, value):
        self._value = value

    def negate(self):
        return UniOpExpAST('NOT', self)

    def __str__(self):
        #return "Var   : ({})".format(self._value)
        return "{}".format(self._value)


class ExprError(Exception):
    def __init__(self, str):
        self._str = str

    def __str__(self):
        return "ExprError  : " + repr(self._str)

class UniOpError(ExprError):
    def __init__(self, str):
        ExprError.__init__(self, str)

    def __str__(self):
        return "UniOpError : " + repr(self._str)

class BinOpError(ExprError):
    def __init__(self, str):
        ExprError.__init__(self, str)
    def __str__(self):
        return "BinOpError : " + repr(self._str)

class Parser:
    def __init__(self, name, token_iter):
        self._name = name
        self._curTok = ''
        self._token_iter = token_iter

    def _getNextToken(self):
        try:
            self._curTok = next(self._token_iter)
            return self._curTok
        except StopIteration:
            print('End of tokens')
            #self._curTok = 0
            return 0

    @staticmethod
    def _errorUniOp(str):
        raise UniOpError(str)

    @staticmethod
    def _errorBinOp(str):
        raise BinOpError(str)

    @staticmethod
    def _errorExpr(str):
        raise ExprError(str)

    def parse(self):
        '''
        Expr = LHS | LHS RHS
        '''
        self._getNextToken()
        lhs = self.parsePrimary()
        if not lhs: return 0
        return self.parseBinOpRHS(lhs)

    def parsePrimary(self):
        '''
        PrimaryExpr = NOT PrimaryExpr | ID | LBRACKET ParenExpr
        '''
        if self._curTok.typ == 'NOT':
            self._getNextToken()
            return UniOpExpAST('NOT', self.parsePrimary())
        elif self._curTok.typ == 'ID':
            value = self._curTok.value
            self._getNextToken()
            return VariableExprAST(value)
        elif self._curTok.typ == 'LBRACKET':
            return self.parseParenExpr()
        else:
            self._errorExpr("Unknown Token {}".format(self._curTok.typ))
            return 0

    def parseParenExpr(self):
        '''
        ParenExpr := Expr RBRACKET
        '''
        exprAst = self.parse()
        if not exprAst:
            return 0
        if self._curTok.typ != 'RBRACKET':
            self._errorExpr("Expected RBRACKET - received {}".format(self._curTok.value))
        self._getNextToken()
        return exprAst

    def parseBinOpRHS(self, lhs):
        '''
        RHS = OR PrimaryExpr | AND PrimaryExpr
        '''
        while self._curTok.typ in ('OR', 'AND'):
            op = self._curTok.typ

            self._getNextToken()
            rhs = self.parsePrimary()
            if not rhs:
                return 0
            lhs = BinOpExprAST(op, lhs, rhs)
        return lhs



class TestDeMorgan(unittest.TestCase):
    def lexer(self, expr, result):
        res = list(tokenize(expr))
        return self.assertEqual(res, result)

    def test_simple(self):
        self.lexer('a', [Token('ID', 'a', 0)])



if __name__ == "__main__":
    if len(sys.argv) > 1:
        probs  = open(sys.argv[1]).readlines()

        for prob in probs:
            print(prob.strip())
            for token in tokenize(prob.strip('\n')):
                print(token)
            print()

        for index, prob in enumerate(probs):
            print(prob.strip())
            parser = Parser(index, tokenize(prob.strip()))
            result = parser.parse()
            print(result)
            print('NEGATE')
            print(result.negate())
            print('\n\n')
    else:
        unittest.main()

