def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("b should not be zero")
    if a % b == 0:
        return a // b
    return a / b

while True:
    try:
        a = int(input())
        b = int(input())
        c = divide(a, b)
        print(c)
    except Exception as e:
        print(e)
