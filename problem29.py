# factorial

# 8! = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
# 8! = 8 * 7!
# 7! = 7 * 6!
# ...
# 1! = 1

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

result = factorial(4)

print(result)
