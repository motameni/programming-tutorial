numbers_str = input("Please enter a list of numbers: ")
numbers_str_list = numbers_str.split(" ")

numbers = []
for number_str in numbers_str_list:
    numbers.append(int(number_str))
    
unique_numbers = []
for number in numbers:
    if not number in unique_numbers:
        unique_numbers.append(number)
        
print(unique_numbers)
