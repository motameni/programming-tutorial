# Enter the count of names: 3
# Enter name #1: Alice
# Enter name #2: Bob
# Enter name #3: Charlie

# List of names:
# ['Alice', 'Bob', 'Charlie']

name_count = int(input("Enter the count of names: "))
name_list = []

for i in range(name_count):
    name = input("Enter name #%d: " % (i + 1))
    name_list.append(name)

print("\nList of names:", name_list)
