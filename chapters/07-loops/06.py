mylist = ["Ali", "John", "Jane", "John", "Jane", "Asghar", "Ali"]

mylist2 = []

for item in mylist:
    counter = 0
    for mored in mylist2:
        if item == mored:
            counter = counter + 1 
    if counter == 0:
        mylist2.append(item)

print(mylist2)
