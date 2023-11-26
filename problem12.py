numbers = [1, 4, 7, 12, 15, 20, 25, 30, 35, 40]

sum = 0

for i in range(10):
    if numbers[i] % 2 == 0:
        sum = sum + numbers[i]
