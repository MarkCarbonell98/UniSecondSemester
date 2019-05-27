
class Number:
    def __init__(self, number):
        self.number = number

class Operator:
    def __init__(self, operator, precedence, associativity):
        self.operator = operator
        self.left = self.right = None
        self.precedence = precedence
        self.associativity = associativity

def parse(s):
    print()
    '''
        while there are tokens in S
            
            if token is a number, then push it to the number stack

            if token is an parenthesis then push it to the operator stack

            if token is an operator then

                while(there is a parenthesis at the top of the op. stack || there is op. at the top of op. stack with greater precedence || the op. at the op of op has equal precendence and is left associative && the op at top of op. stack is not a left parenthesis) 
                    pop operators from op. stack to the number stack
                push op. to op. stack

            if char is a left parenthesis, then
                push it to op. stack
            if char is a right paren, then
                while the op. at op stack is not a left paren
                    pop op. from op.stack into the number stack
                if left paren at top of op. stack
                    pop op. from op. stack and erase it
        if no more char to read
            while op. tokens in op stack stack
                pop op. from op. stack and push to number stack
                
        exit
                


    '''






