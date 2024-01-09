# Write a Python function called generate_multiplication_table that takes an integer n as
# input and prints the multiplication table for the numbers 1 through 10 for that value of n.

# Your program should prompt the user to enter a number, call the generate_multiplication_table
# function, and display the resulting multiplication table.

# Sample Input:
# Enter a number: 7

# Sample Output:
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

def generate_multiplication_table(n):
    for m in range(1, 11):
        text = "%d x %d = %d" % (n, m, n * m)
        print(text)


x = int(input("Enter a number: "))

generate_multiplication_table(x)
