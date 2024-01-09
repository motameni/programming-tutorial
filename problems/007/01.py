numbers = [2, 7, 4, 1, 9, 6, 3, 8, 10, 2, 3, 4, -100]
total = 0

for number in numbers:
    if number >= 5:
        total = total + number

print("Sum of numbers greater than or equal to 5:", total)
