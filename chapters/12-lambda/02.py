def compare(func, a, b):
    return func(a, b)

res = compare(lambda a, b: a < b, 3, 4)
print(res)
