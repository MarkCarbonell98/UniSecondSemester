words = ["hallo", "ich", "bin", "marcos"]

for word in words:
    print(word)

for i in range(5):
    print(i)

for i in range(len(words)):
    print(words[i])

print(list(range(5)))

for num in range(2,10):
    if num % 2 == 0:
        print("even", num)
        continue
    print("uneven found!", num)

# pass does not do anything

class MyEmptyClass:
    pass

def initlog(*args):
    pass

def fib(n):
    return n if n <= 1 else fib(n-1) + fib(n-2)

print(fib(5))

f = fib

print(f(10))
print(fib(0))


def ask_ok(prompt, retries = 4, reminder = "Please try again"):
    while True:
        answer = input(prompt)
        if answer in ("y", "ye", "yes"):
            return True
        if answer in ("n", "no", "nope"):
            return False
        retries -= 1
        if retries < 0:
            raise ValueError("Invalid response")
        print(reminder)

# print(ask_ok("Are you gay ?"))

def fib2(n):
    a,b = 0, 1
    while a < n:
        print(a, end=' ')
        a,b = b, a+b
    print()

fib2(2000)

foo = fib2
foo(1000)

def fibList(n):
    result = []
    a,b = 0, 1
    while a < n:
        result.append(a)
        a,b = b, a+b
    return result

print(fibList(10000))

i = 5

def func(arg = i):
    print(arg)

i = 6

func()

def fun2(a, L=[]):
    L.append(a)
    return L

fun2(1)
fun2(2)
fun2(3)
print(fun2(4))

def fun(a, L=None): #the default value is evaluated only once...checking is the calls come consecutively after each other
    if L is None:
        L = []
    L.append(a)
    return L

def multArgs(a,b,c):
    print(a,b,c)

multArgs(c = 1, b = 5, a = 20)
multArgs(20, 5, 1)
multArgs(20,c = 5, b=  1)
# multArgs(a = 20,4,1)

def writeMult(file, sep, *args):
    file.write(sep.join(args))

# writeMult('./', "/", 1,2,3,4)

def concat(* args, sep = "/"):
    return sep.join(args)

print(concat("hello", "tu", "yo"))

list(range(3,6))
args = [3,6]
print(list(range(*args))) # *args deliver lists, ** delivers dictionaries

def myFunc(arg1, *arg2, **arg3):
    print(arg1)
    for arg in arg2:
        print(arg)
    for key in arg3:
        print(key, arg3[key])

myFunc("hellou", [1,2,3,4,5], {"hellou": 1234, "todo": "bien", "si": True})



def increment(n):
    return lambda x: x + n

funky = increment(46)

print(funky(0))
print(funky(1))
print(funky(2))

pairs = [(1,"one"), (2,"two"), (3, "three"), (4, "four")]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

def function():
    """Do nothing bud document it.

    no bro

    ni de vaina"""

    print(function.__doc__) #.__doc__ method containing multiline comments of the function

function()

# type checking with strings, called anotations. the -> gives the return data type.
def funk(ham: str, eggs: str = "eggs") -> str:
    print("Annotiations", f.__annotations__)
    print("arguments", ham, eggs)
    return ham + " and " + eggs

funk("spam")


array = []

array.append(20000)
array.append(20001)
array.append(20002)

array.extend([1,2,3])
array[len(array):] = [4,5,6]
array.insert(2, "hellou")
print(array.pop())
print(array)
print(array.index(4))
print(array.count(4))

stack = [3,4,5]
stack.append(7)
stack.append(8)
stack.append(9)
print(stack)
stack.pop()
stack.pop()
stack.pop()
print(stack)

from collections import deque

queue = deque(["tu", "yo", "nosotros"])
queue.append("terry")
print(queue)
queue.popleft()
print(queue)

squares = list(map(lambda x: x**2, range(20)))
print(squares)
squares2 = [x**2 for x in range(20)]
print(squares2)
notequal = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(notequal)
vec = [x for x in squares if x > 10]
print(vec)
vec2 = [abs(x) for x in squares2]
print(vec2)

fruit = [' banana ', ' berry ', ' pina ', ' fresa ']
fruit2 = [weapon.strip() for weapon in fruit]
print(fruit2)

numberSquarePairs = [(x, x**2) for x in range(10)]
print(numberSquarePairs)
vec = [[1,2,3], [4,5,6], [7,8,9]]
arr = [num for elem in vec for num in elem]
print(arr)

from math import pi
result = [str(round(pi, i)) for i in range(1,6)]
print(result)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

result2 = [[row[i] for row in matrix] for i in range(4)]

#equivalent to 

result3 = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    result3.append(transposed_row)

print(result3)
print(result2)

print(list(zip(*matrix)))

#del statement works to remove items from the list.

del result3[1:3]
# del result3
print(result3)

#tuples 

variable = 1,3,43,[1234],"hellou" #are inmutable just like strings

empty = ()
singleton = "hello",
print(len(empty))
print(len(singleton))

a,b,c,d,e = variable
print(a,b,c,d,e)

basket = set(["apple", "orange", "apple", "vinegar"]) 
print(basket)
print("orange" in basket)

a = set("abracadabra")
b = set("alacazam")

print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

a = {x for x in "abracadabra" if x not in "abc"}
print(a)

myDict = {"yo": "marcos", "tu": "computadora"}
print(myDict["yo"])
del myDict["yo"]
myDict['nosotros'] = "equipo"
print(myDict)
print(list(myDict))
print("yo" in myDict)
print("nosotros" not in myDict)

result4 = dict([("sape", "gato"), ("noseas", "marico"), ("quevainatan", "arrecha")])
print(result4)

result5 = {x : x**2 for x in (2,4,6)} # creating dict using comprehensions
print(result5)
print(dict(sape="gato", noseas="malo", estavainaes="increible")) #create dict out of variable names

knights = {"erwe": "von esse", "bayuste": "a saber"}
print(knights.items())
for k,v in knights.items():
    print(k,v)

for i,v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)

questions = ['name', 'quest', 'color']
answers = ["marcos", "program", "blue"]
for q,a in zip(questions,answers):
    print("What is your {0} ? It is: {1}".format(q,a))

for i in reversed(range(1,10,2)):
    print(i)

# sorted returns a new list
print(0 and 2)

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

print([1,2,3] < [1,2,4])

print("ABC" < "C" < "Pascal" < "Python")

print((1,2,3,4) < (1,2,4))

print((1,2) < (1,2,-1))

print((1, 2, 3)             == (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4))