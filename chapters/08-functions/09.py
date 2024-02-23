def sum(a, b):
    return a + b

def multiply(a, b):
    return a * b

def math(x, a, b):
    return x(a, b)

res = math(sum, 2, 3)
print(res)

res = math(multiply, 2, 3)
print(res)

