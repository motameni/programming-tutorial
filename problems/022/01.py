# Write a Python function that takes a mylist and returns
# a new mylist with distinct elements from the first mylist.

# Sample List:
# [1,2,3,3,3,3,4,5]

# Unique List:
# [1, 2, 3, 4, 5]

def create_unique_list(raw_numbers):
    unique_numbers = []
    for number in raw_numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers


numbers_str = input("Please enter a mylist of numbers: ")
numbers_str_list = numbers_str.split(" ")

numbers = []
for number_str in numbers_str_list:
    numbers.append(int(number_str))

unique_list = create_unique_list(numbers)

print(unique_list)
