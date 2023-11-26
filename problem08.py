# You are given a list of numbers. 
# Write a Python program to calculate the sum of all the numbers in the list that are greater than or equal to 5. 
# You should use only a for loop to iterate through the list.
# Initialize a variable to store the sum
# Write a for loop to calculate the sum of numbers greater than or equal to 5
# Print the sum of numbers greater than or equal to 5
# print("Sum of numbers greater than or equal to 5:", total)


numbers = [2, 7, 4, 1, 9, 6, 3, 8, 10, 2, 3, 4, -100]
total = 0

for number in numbers:
    if number >= 5:
        total = total + number

print("Sum of numbers greater than or equal to 5:", total)

