def divide(a, b):
    return a / b

try:
    result = divide(12, 0)
    print(result)
except Exception as e:
    print("Error:", e)
