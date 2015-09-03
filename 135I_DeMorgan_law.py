import sys
import collections
import re


probs = open(sys.argv[1]).readlines()

Token = collections.namedtuple('Token', ['typ', 'value', 'pos'])

class Node():
    def __init__(self, rootValue):
        self._leftChild = None
        self._rightChild = None
        self._rootValue = rootValue
        self._parent = None

    @property
    def leftChild(self):
        return self._leftChild

    @leftChild.setter
    def leftChild(self, value):
        self._leftChild = value

    def insertLeftChild(self):
        self._leftChild = Node('')
        return self._leftChild

    @property
    def rightChild(self):
        return self._rightChild

    @rightChild.setter
    def rightChild(self, value):
        self._rightChild = value

    def insertRightChild(self):
        self._rightChild = Node('')
        return self._rightChild

    @property
    def parent(self):
        return self._parent
    @property
    def rootValue(self):
        return self._rootValue

    @rootValue.setter
    def rootValue(self, value):
        self._rootValue = value


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


def parser(tokens):
    root = Node('')
    stack = []
    left_flag = True
    curNode = root
    for index, tok in enumerate(tokens):
        if tok.typ == 'NOT':
            curNode.rootValue = 'NOT'
            if len(stack) == 0: root = curNode
            stack.append(curNode)
            if curNode.rightChild is None :
                curNode.rightChild = Node('')
            curNode = curNode.rightChild
            left_flag = False
        elif tok.typ == 'ID':
            if left_flag :
                if len(tokens) > index+1 and (tokens[index+1].typ == 'AND' or \
                                           tokens[index+1].typ == 'OR'):
                    curNode.rootValue = tok.value
                elif len(tokens) == index+1:
                    curNode.rootValue = tok.value
            else :
                curNode.rootValue = tok.value
                parent = stack.pop()
                curNode = parent
        elif tok.typ  == 'OR' or tok.typ == 'AND':
            parent = Node(tok.typ)
            parent.leftChild = curNode
            if len(stack) == 0: root = parent
            stack.append(parent)
            parent.rightChild = Node('')
            curNode = parent.rightChild
            left_flag = False
        elif tok.typ == 'LBRACKET':
            if curNode.leftChild is None:
                curNode.leftChild = Node('')
            stack.append(curNode)
            curNode = curNode.leftChild
            left_flag = True
        elif tok.typ == 'RBRACKET':
            parent = stack.pop()
            curNode = parent
            if len(stack) == 0: root = parent
            left_flag = False
        else :
            raise RuntimeError('Unexpected tokens {}'.format(tok))
    return root

def pre_order_tranverse(root):
    if root.leftChild is not None:
        print('Left of {}'.format(root.rootValue))
        pre_order_tranverse(root.leftChild)
    print('Node ', root.rootValue)
    if root.rightChild is not None:
        print('Right of {}'.format(root.rootValue))
        pre_order_tranverse(root.rightChild)

for prob in probs:
    print(prob.strip())
    for token in tokenize(prob.strip('\n')):
        print(token)
    print()

print('PARSING')

for prob in probs:
    print(prob.strip())
    pre_order_tranverse(parser(tokenize(prob.strip('\n'))))
    print()
