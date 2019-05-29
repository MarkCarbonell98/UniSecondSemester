
class Number:
    def __init__(self, number):
        self.val = number

    def __repr__(self):
        return f"Number({self.val})"

class Operator:
    def __init__(self, left, operator, right):
        self.operator = operator
        self.left = left
        self.right = right


    def __repr__(self):
        return f"Operator({self.left}, {self.operator}, {self.right})"

# diese funktion stellt die Prioritäten der Operatoren fest, und gibt dir eine Liste zuruck mit die dazugehörige Operatoren und Zahlen

operationsPrecedence = {
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 9,
    ')': 0,
}

# def checkInfix(infix):
def convertToRPN(infix):
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


def parse(infix):
    postfix = convertToRPN(infix)
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
print(convertToRPN(infix))
postfix = convertToRPN(infix)
print(parse(postfix))
print(evaluateTree(parse(postfix)))



