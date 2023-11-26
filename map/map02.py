mylist = [(2, 5), (3, 7), (12, 15), (9, 3)]

def sum(numbers):
    return numbers[0] + numbers[1]

result = map(sum, mylist)

print(result)
print(list(result))
