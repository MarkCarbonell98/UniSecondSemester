class Number:
    def __init__(self, number):
        self.val = number

    def __repr__(self):
        return "Number({val})".format(val = self.val)

class Operator:
    def __init__(self, left, operator, right):
        self.operator = operator
        self.left = left
        self.right = right

    def __repr__(self):
        return "Operator({left}, {operator}, {right})".format(left=self.left, operator=self.operator, right=self.right)

# diese funktion stellt die Prioritaeten der Operatoren fest, und gibt dir eine Liste zuruck mit die dazugehoerige Operatoren und Zahlen

operationsPrecedence = {
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 9,
    ')': 0,
}

# mittels der shunting yard algorithmus wird der infix String auf postfix uebersetzt
def convertToPostfix(infix):
    if not infix:
        raise SyntaxError
    expr = list(infix)
    outputQueue, operatorStack = [], []
    for token in expr:
        if token.isdigit():
            outputQueue.append(token)
        elif token in operationsPrecedence:
            while operatorStack:
                stackTop = operatorStack[-1]
                if operationsPrecedence[token] <= operationsPrecedence[stackTop]:
                    if token != ')':
                        if stackTop != '(':
                            operatorStack.pop()
                            outputQueue.append(stackTop)
                        else:
                            break
                    else:
                        if stackTop != '(':
                            operatorStack.pop()
                            outputQueue.append(stackTop)
                        else:
                            operatorStack.pop()
                            break
                else:
                    break
            if token != ")":
                operatorStack.append(token)
    while operatorStack:
        remainingItem = operatorStack[-1]
        operatorStack.pop()
        outputQueue.append(remainingItem)
    return outputQueue


def parse(s):
    postfix = convertToPostfix(s)
    if not postfix:
        raise SyntaxError
    stack = []
    for token in postfix:
        if token in operationsPrecedence:
            stack.append(Operator(stack.pop(), token, stack.pop()))
        else:
            stack.append(Number(token))
    if len(stack) != 1: raise SyntaxError
    return stack[0]

def evaluateTree(tree):
    if not tree:
        raise SyntaxError
    if isinstance(tree, Number):
        return tree.val

    leftEvaluation = int(evaluateTree(tree.left))
    rightEvaluation = int(evaluateTree(tree.right))
    if tree.operator == '+':
        return rightEvaluation + leftEvaluation
    elif tree.operator == '-':
        return rightEvaluation - leftEvaluation
    elif tree.operator == '*':
        return rightEvaluation * leftEvaluation
    elif tree.operator == '/':
        return rightEvaluation / leftEvaluation



infix = '2*4*(3+(4-7)*8)-(1-6)'
print(convertToPostfix(infix))
rpn = convertToPostfix(infix)
print(parse(rpn))
print(evaluateTree(parse(rpn)))

#TestCases
import unittest
import random

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.firstNumber = random.randint(1,20)
        self.secondNumber = random.randint(1,20)
        self.evaluateTree = evaluateTree
        self.postfix = convertToPostfix

    def test_addition(self):
        infix = '{}+{}'.format(self.firstNumber,self.secondNumber)
        assert self.evaluateTree(self.postfix(infix) == self.firstNumber+self.secondNumber)

    def test_substraction(self):
        infix = '{}-{}'.format(self.firstNumber,self.secondNumber)
        assert self.evaluateTree(self.postfix(infix)) == self.firstNumber-self.secondNumber 

    def test_multiplication(self):
        infix = '{}*{}'.format(self.firstNumber,self.secondNumber)
        assert self.evaluateTree(self.postfix(infix)) == self.firstNumber*self.secondNumber 

    def test_division(self):
        infix = '{}/{}'.format(self.firstNumber,self.secondNumber)
        assert self.evaluateTree(self.postfix(infix)) == self.firstNumber/self.secondNumber 

    def test_operator_order(self):
        infixAdd = '{}++{}'.format(self.firstNumber,self.secondNumber)
        infixSub = '{}--{}'.format(self.firstNumber,self.secondNumber)
        infixMul = '{}**{}'.format(self.firstNumber,self.secondNumber)
        infixDiv = '{}//{}'.format(self.firstNumber,self.secondNumber)
        infixBracketsOpen1 =  infixDiv = '({}+{}'.format(self.firstNumber,self.secondNumber)
        infixBracketsOpen2 =  infixDiv = '(({}+{}'.format(self.firstNumber,self.secondNumber)
        infixBracketsClosed1 =  infixDiv = '{})+{}'.format(self.firstNumber,self.secondNumber)
        infixBracketsClosed2 =  infixDiv = '{}))+{}'.format(self.firstNumber,self.secondNumber)

        assert self.evaluateTree(self.postfix(infixAdd)) == False
        assert self.evaluateTree(self.postfix(infixSub)) == False
        assert self.evaluateTree(self.postfix(infixMul)) == False
        assert self.evaluateTree(self.postfix(infixDiv)) == False
        assert self.evaluateTree(self.postfix(infixBracketsOpen1)) == False
        assert self.evaluateTree(self.postfix(infixBracketsOpen2)) == False
        assert self.evaluateTree(self.postfix(infixBracketsClosed1)) == False
        assert self.evaluateTree(self.postfix(infixBracketsClosed2)) == False

    def test_char(self):
        infix = '{}*a'.format(self.firstNumber)
        assert self.evaluateTree(self.postfix(infix)) == False

    def test_precedence(self):
        infix = '{}+{}*{}'.format(self.firstNumber,self.secondNumber,self.firstNumber)
        assert self.evaluateTree(self.postfix(infix)) == self.firstNumber+self.secondNumber*self.firstNumber

    def test_bracketing(self):
        infix = '({}+{})*{}'.format(self.firstNumber,self.secondNumber,self.firstNumber)
        assert self.evaluateTree(self.postfix(infix)) == (self.firstNumber+self.secondNumber)*self.firstNumber

if __name__ == '__main__':
    unittest.main()
