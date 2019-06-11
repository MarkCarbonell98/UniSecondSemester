

class Number:
    def __init__(self, n):
        self.number = n
    
    def evaluate(self):
        return float(self.number)

    def __repr__(self):
        return self.number

    def printTree(self, indent = ''):
        return "(" + self.number + ")\n"

class Operator:
    def __init__(self, left, operator, right):
        if not operator in "+-*/":
            raise SyntaxError("Invalid Operator")
        self.left = left
        self.operator = operator
        self.right = right

    def evaluate(self):
        left,right = self.left.evaluate(), self.right.evaluate()
        if self.operator == '+':
            return left + right
        if self.operator == '-':
            return left - right
        if self.operator == '*':
            return left * right
        if self.operator == '/':
            return left / right

    def __repr__(self):
        return "(" + repr(self.left) + self.operator + repr(self.right) + ")"

    def printTree(self, indent = ''):
        return "(" + self.operator + ") -- " + self.right.printTree(indent + ' |     ') + \
            indent + " |\n" + \
            indent + self.left.printTree(indent)

def findClosingBracket(expression, startIndex):
    count = 1
    for k in range(startIndex + 1, len(expression)):
        if expression[k] == "(": count += 1
        elif expression[k] == ")": count -= 1
        if count == 0: return k
    raise SyntaxError("Invalid Expression")

def rightPriorityIsHigher(expression, startIndex):
    if startIndex == len(expression) - 1:
        return False
    if startIndex == 0:
        return True
    return expression[startIndex - 1] in '+-' and expression[startIndex + 1] in '*/'

def parse(expression):
    if type(expression) is str:
        expression = expression.replace(" ", "")
        expression = [char for char in expression]
    i = 0
    while True:
        if i >= len(expression):
            raise SyntaxError("Invalid expression")
        if type(expression[i]) is str:
            if expression[i] in '0123456789':
                expression[i] = Number(expression[i])
            elif expression[i] == '(':
                end = findClosingBracket(expression, i)
                subtree = parse(expression[i + 1: end])
                expression[i : end + 1] = [subtree]
            else:
                raise SyntaxError("Invalid Expression")
        print(expression, i, rightPriorityIsHigher(expression, i))
        if rightPriorityIsHigher(expression, i):
            i += 2
        elif i >= 2:
            expression[i - 2: i + 1] = [Operator(expression[i - 2], expression[i - 1], expression[i])]
            i -= 2
        if len(expression) == 1:
            print(expression[0], "\n")
            return expression[0]

def evaluateTree(root):
    return root.evaluate()


tree = parse('2*4*(3+(4-7)*8)-(1-6)')
print(tree.printTree())
print(evaluateTree(tree))


