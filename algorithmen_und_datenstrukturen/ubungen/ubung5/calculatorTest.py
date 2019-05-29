class Number:
    def __init__(self, number):
        self.value_ = number

class Operator:
    def __init__(self, left, operator, right):
        self.operator_ = operator
        self.left_ = left
        self.right_ = right

from collections import namedtuple
from pprint import pprint as pp
 
OpInfo = namedtuple('OpInfo', 'prec assoc')
L, R = 'Left Right'.split()
 
operations = {
 '*': OpInfo(prec=3, assoc=L),
 '/': OpInfo(prec=3, assoc=L),
 '+': OpInfo(prec=2, assoc=L),
 '-': OpInfo(prec=2, assoc=L),
 '(': OpInfo(prec=9, assoc=L),
 ')': OpInfo(prec=0, assoc=L),
 }
 
NUM, LPAREN, RPAREN = 'NUMBER ( )'.split()
 
 
def prepareInfixString(char = None):
    'charuts an expression and returns list of (TOKENTYPE, tokenvalue)'

    if char is None:
        char = input('expression: ')
    tokens = list(char)
    s = []
    for token in tokens:
        if token in operations:
            s.append((token, operations[token]))
        else:    
            s.append((NUM, token))
    return s

def createRPN(s):
    string = prepareInfixString(s)
    outq, stack = [], []
    for token, val in string:
        if token is NUM:
            outq.append(val)
        elif token in operations:
            t1, (p1, a1) = token, val
            while stack:
                t2, (p2) = stack[-1]
                if (a1 == L and p1 <= p2) or (a1 == R and p1 < p2):
                    if t1 != RPAREN:
                        if t2 != LPAREN:
                            stack.pop()
                            outq.append(t2)
                        else:    
                            break
                    else:        
                        if t2 != LPAREN:
                            stack.pop()
                            outq.append(t2)
                        else:    
                            stack.pop()
                            break
                else:
                    break
            if t1 != RPAREN:
                stack.append((token, val))
    while stack:
        t2, (p2, a2) = stack[-1]
        stack.pop()
        outq.append(t2)
    return outq
 

def evaluateTree(postfixList):
    a=[]
    b={'+': lambda x,y: y+x, '-': lambda x,y: y-x, '*': lambda x,y: y*x,'/': lambda x,y:y/x}
    for c in postfixList:
        if c in b: a.append(b[c](a.pop(),a.pop()))
        else: a.append(float(c))
    return a

# infix = '2*4*(3+(4-7)*8)-(1-6)'
infix = '2+5*3'
rp = createRPN(infix)
print(rp)
print(evaluateTree(rp))





#TestCases
#import unittest
#import random

#   def setUp(self):

#       firstNumber = random.randin(1,20)
#       secondNumber = random.randin(1,20)

#   def test_addition(self):
#       calc = TODO
#       infix = '{}+{}'.format(firstNumber,secondNumber)
#       
#       assert calc.evaluateTree(calc.evaluateTree(tree.postfix(infix))) == firstNumber+secondNumber 

#   def test_substraction(self):
#       calc = TODO
#       infix = '{}-{}'.format(firstNumber,secondNumber)
#       
#       assert calc.evaluateTree(calc.evaluateTree(tree.postfix(infix))) == firstNumber-secondNumber 

#   def test_multiplication(self):
#       calc = TODO
#       infix = '{}*{}'.format(firstNumber,secondNumber)
#       
#       assert calc.evaluateTree(calc.evaluateTree(tree.postfix(infix))) == firstNumber*secondNumber 

#   def test_division(self):
#       calc = TODO
#       infix = '{}/{}'.format(firstNumber,secondNumber)
#       
#       assert calc.evaluateTree(calc.evaluateTree(tree.postfix(infix))) == firstNumber/secondNumber 

#   def test_operator_order(self):
