a = (i for i in range(10)) # generator function 

for i in a:
    print(i)
# run fish
for i in a:
    print(i)

def a():
    i = 0
    while i < 10:
        yield i 
        i += 1

for i in a():
    print(i)

b = a()
print(type(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

# speicher von einen million Element wird nicht notwendig sein