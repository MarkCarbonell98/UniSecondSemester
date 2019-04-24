word = "hellou"
print(word[2:4])
print(word[:4])
print(word[1:])
print(word[123:])
squares = [1,2,3,4,5]
secondList = [1,2,3,4,5]
print(squares[2])
print(squares[2:])
print(squares[:]) #shallow copy

print(squares + secondList)
secondList[2:5] = []
print(secondList)

a,b = 0, 1
while a < 10:
    print(a)
    a,b = b, a + b


x = int(input("Please enter an int: "))
if x > 5:
    print("x is greter than five")
elif x == 5:
    print("x equals five")
else:
    print("marcos es marico")

