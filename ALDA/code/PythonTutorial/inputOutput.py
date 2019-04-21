name = "marcos"
age = 20
print(f"He is {age} years old and is called {name}")

yes = 42_572_654
no = 21_322_151

percentage = yes / (yes + no)

print('{:-9} YES votes with {:3.3%}'.format(yes, percentage))

# f = open("modules.py", "w")
with open("modules.py") as f:
    read_data = f.read()
print(f.closed)

f = open("fibo.py", "r+")
for line in f:
    print(line, end = "\n")

f.write(" \n hellou = True \n world = 0")

for line in f:
    print(line, end = "\n")

# f.read() returns the entire file
# f.readline() returns the last read line
# f.write() appends text to the file, returns the number of characters written
# f.tell() returns an integer with the files current position as a byte representation
# f.seek(offset, from_what) changes the files object position. f.seek(5) returns the 5th byte of the file, f.seek(-3,2) the third byte before the end
# 

import json
jsonData = json.dumps([1, "simple", "list"])
print(jsonData)

x = {
    "hellou": 20,
    "50": 30,
    "gay": True,
    "super": "yes"
}
f = open("text.txt", "r+")
print(json.dump(x, f))
x = json.load(f)
print(x)


