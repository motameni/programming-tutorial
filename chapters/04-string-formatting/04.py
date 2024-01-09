name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
avg = float(input("Enter your average: "))

a = "\nHello %s!\nYour age is %d!\nYour average is %.2f" % (name, age, avg)

print(a)
