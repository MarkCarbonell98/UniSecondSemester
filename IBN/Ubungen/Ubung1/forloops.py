words = ['cat', 'window', 'something else']
for w in words:
    print(w, len(w))

for w in words[:]:
    if len(w) > 6:
        words.insert(0,w)

print(words)

for i in range(5):
    print(i)

for i in range(len(words)):
    print(words[i])

print(list(range(100)))

def fib(n):
    a,b = 0,1
    while a < n:
        print(a,end=" ")
        a,b = b, a +b
    print()

fib(2000)

c,d,e = 0,1, []
while c < 2000:
    e.append(c) # aquivalent to push
    c,d = d, c + d

print(e)