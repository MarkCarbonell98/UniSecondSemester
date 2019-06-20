import time

def fib1(n):                      # Funktion berechnet die n-te Fibonacci-Zahl
    if n <= 1: 
        return n                 # Rekursionsabschluss
    return fib1(n-1) + fib1(n-2)

def fib3Impl(n):
    if n == 0: 
        return 1, 0         # gebe die Fibonacci-Zahl von 1 und die davor zurück
    else:                          # rekursiver Aufruf
        f1, f2 = fib3Impl(n-1)      # f1 ist Fibonacci-Zahl von n, f2 die von (n-1)
        return f1 + f2, f1          # gebe neue Fibonacci-Zahl fn+1 = f1+f2 und die vorherige (fn = f1) zurück.
def fib3(n):
    f1, f2 = fib3Impl(n)    # Hilfsfunktion, f1 ist die Fibonacci-Zahl von (n+1) und f2 ist die Fibonacci-Zahl von n
    return f2

def fib5(n):
    f1, f2 = 1, 0                # f1 ist die Fibonaccizahl für n=1, f2 die für n=0
    while n > 0:
        f1, f2 = f1 + f2, f1     # berechne die nächste Fibonaccizahl in f1 und speichere die letzte in f2
        n -= 1
    return f2

#fib1 funktioniert wie ein Baum und muss für jede Zahl kleiner
#n die Fibonaccizahl berechnen, wobei ein Paar FibonacciZahlen
#sogar mehrfach bestimmt werden, deshalb dauert es länger als
#bei fib3, denn fib3 muss nicht für jede Fibonaccizahl nur eine
#Rekursion durchführen und nicht zwei, deswegen wird hier keine
#Zahl doppelt bestimmt
#fib5 arbeitet am schnellsten, denn fib5 benutzt eine Schleife
#anstatt einer Rekursion, wodurch weniger Speicher und weniger
#Zeit verbraucht wird

def mul2x2(a,b):
    return [a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]]

def fib6(n):
    if n == 0:
        return 0
    if n >= 1:
        matrix1 = [1, 1, 1, 0]
        matrix = matrix1
        for i in range(1, n):
            matrix = mul2x2(matrix, matrix1)
        return matrix[1]
    

def fib7(n):
    X = [1, 1, 1, 0]
    if n == 0:
        return 1
    if n == 1:
        return X[1]
    if n % 2 == 0:
        X = mul2x2(X,X)
        Y = X
        n = (int)(n/2)
        for i in range(1, n):
            X = mul2x2(X,Y)
        return X[1]
    if n % 2 == 1:
        Z = mul2x2(X,X)
        Y = Z
        n = (int)((n-1)/2)
        for i in range(1, n):
            Z = mul2x2(Z,Y)
        X = mul2x2(X, Z)
        return X[1]
    
def zeit(fib):
    time1 = 0
    n = 1
    while(time1 < 10):
        start = time.time()
        fib(n)
        ende = time.time()
        time1 = ende-start
        if time1 <= 10:
            if time1 < 0.5:
                n = n*5
            elif time1 < 1:
                n = n+10
            elif time1 < 3:
                n = n+5
            elif time1 < 5:
                n = n+2
            else:
                n += 1
    return n

print(zeit(fib1))
print(zeit(fib3))       
print(zeit(fib5))
print(zeit(fib6))
print(zeit(fib7))

fib1(38)
#Die erste Fibonaccizahl, bei der die Berechnung über 10 Sekunden dauert ist 38
fib3(2967)
#2967. Fibonaccizahl ist erste Zahl mit RecursionError
fib5(819000)

fib6(285000)
zahl = fib7(350000)


#ungefähre Zahlen durch austesten, die Funktion Zeit dauert zu lange

