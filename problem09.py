nums = [2, 3, 5, 6, 9, 10]
result = []

for num in nums:
    if (num % 2 == 0) and (num % 3 != 0):
        result.append(num)
print(result)
