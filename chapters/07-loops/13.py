people = [("Alice", 25), ("Bob", 17), ("Charlie", 20), ("David", 16), ("Eva", 22)]

x = "Ali,15 Nadiya,20 Amir,30"
mylist = x.split(" ")

for person in mylist:
    data = person.split(",")
    name = data[0]
    age = data[1]
    print(name, age)

