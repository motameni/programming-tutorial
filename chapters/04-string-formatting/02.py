# string formatting

data = [
            ["Ali",     30, "%s's age is %d"],
            ["Nadiya",  25, "%s is %d :)"],
            ["AmirAli", 20, "I am %s and %d years old"]
       ]

for info in data:
    name = info[0]
    age = info[1]
    template = info[2]
    print(template % (name, age))
