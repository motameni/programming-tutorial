# Create
phonebook = {
    "Ali": 123234345,
    "Nadiya": 234345456
}

phonebook["AmirAli"] = 345456567
print(phonebook)

# Read
num1 = phonebook["AmirAli"]
print(num1)

# Update
phonebook["Ali"] = 456567678
print(phonebook)

# Delete
del phonebook["Ali"]
phonebook.pop("Nadiya")
print(phonebook)
