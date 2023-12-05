a = input() # "2 5 6 8 12"

b = a.split(" ") # ["2", "5", "6", "8", "12"]

numbers = []

for i in b:
    numbers.append(int(i))

print(b)
print(numbers)
