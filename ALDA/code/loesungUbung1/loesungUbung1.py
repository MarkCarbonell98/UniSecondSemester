# Aufgabe C

# 1)

import math
print(math.sqrt(36))

# 2)

# print(math.sqrt(-1)) # throws ValueError

# 3)

def mysqrt(num):
    try:
        return math.sqrt(num)
    except ValueError:
        return "mysqrt() funktioniert nicht für negative Zahlen, du Dussel!"

def mysqrt2(num):
    if repr(num).isnumeric() and num >= 0:
        return math.sqrt(num)
    else:
        return "mysqrt2() funktioniert nicht für negative Zahlen, du Dussel!"

print(mysqrt(36))
print(mysqrt(-36))
print(mysqrt2(36))
print(mysqrt2(-36))

# 4)

i = -10
while i <= 10:
    print(i, i % 5) # Der Modulo Operator gibt der Rest aus der Division des erstes Parameter und der nachfolgende Zahl.
    i += 1

# 5)

# Um mehrzeilinge Strings zu schreiben
string = """Hallo, ich bin
string, deine Multilinige
Freundin
"""

print(string)

# Der klasse list erzeugt Containers mit numerische (0,1, N...) index und dict erzeugt assoziative Containers dass nach key/value paare zugeordnet sind

myNewList = ["a","b", "c"] #list Konstruktor wird aufgerufen
myNewDict = {"a": 1, "b":2, "c": 3} # dict Konstruktor wird aufgerufen
print(myNewList)
print(myNewDict)


# 6) 

# __init__ wird in OOP auch in anderen Sprachen als Konstruktor bezeichnet. Ist die Funktion wo die Properties und Methoden der Instanzen dieser Klasse definiert wurden. BSP

class Auto(object):
    def __init__(self, model, farbe, geschwindigkeit):
        self.model = model
        self.farbe = farbe
        self.geschwindigkeit = geschwindigkeit
    def autoZeigen(self):
        print(f"""Das model ist {self.model}
        Die Farbe ist {self.farbe}
        Die maximale Geschwindigkeit ist {self.geschwindigkeit}""")

twingo = Auto("Twingo", "Rosa", 60)
twingo.autoZeigen()

exec(open("sieve.py").read())
print(sieve(1000))


#not relevant ----------------------
# test = range(10,100,10)
# print([i for i in test])
# print(test[0:8]) # manipulates test to give the first number position also 10, together with the eighth index position in to the current step, also 90. Step cadency remains the same


