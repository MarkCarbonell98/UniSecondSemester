from math import log, e
from numpy import arange

def lnFolge(n, x):
    return n * ((pow(x, 1/n)) - 1)

n1 = .2
n2 = 5

resultN1FiveDec = str(log(n1))[0:7]
resultN1TenDec = str(log(n1))[0:13]
resultN2FiveDec = str(log(n2))[0:7]
resultN2TenDec = str(log(n2))[0:13]

print("for n = 1/5")
for i in arange(0,100000):

    n = int(1e9 + i)
    comparison = str(lnFolge(n, n1))[0:13]
    print(comparison, resultN1TenDec)
    if resultN2FiveDec == comparison:
        print(n)
        break


print("result = 1/5 ",log(n1))
print("result = 5 ",log(n2))
print("log base 10 result = 1/5 ",log(n1,10))
print("log base 10 result = 5 ",log(n2,10))
# print("for n = 5")
# for i in arange(20):
#     print(lnFolge(n2, i))

