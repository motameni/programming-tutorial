mylist = [(2, 5), ("12", "23"), (12, 15), ("43", "23"), (12, "12")]

def sum(numbers):
    number1 = numbers[0]
    if type(numbers[0]) == str:
        number1 = int(numbers[0])
    
    number2 = int(numbers[1])
    if type(numbers[1]) == str:
        number2 = int(numbers[1])
        
    return number1 + number2

result = map(sum, mylist)

print(result)
print(list(result))
