def func1(a, b, c):
    return a * b + c

res = func1(3, 2, 1)
print(res)

res = func1(c = 1, b = 2, a = 3)
print(res)



def func2(c, a = 3, b = 2):
    return a * b + c

res = func2(1)
print(res)


def func3(a = 3, b = 2, c = 1):
    return a * b + c

res = func3(c = 0)
print(res)
