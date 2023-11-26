# You are given the following code snippet:

# a = 5
# b = 5.0

# if ___CONDITION___:
#     result = "Same type"
# else:
#     result = "Different types"

# Fill in the ___CONDITION___ such that the value of the variable result becomes "Same type" if the variables a and b are of the same data type and "Different types" if they are not.

# What would be the value of the result variable after executing the code?


a = 5
b = 5.0

if type(a) == type(b):
    result = "Same type"
else:
    result = "Different types"

# step 1: if type(a) == type(b):
# step 2: if <class: 'int'> == <class: 'float'>
# step 3: if False

print(result)

# Note: 
# Ctrl + /: Comment selected lines

# logical operator:
# ==
# !=
# <=
# <
# >=
# >

# not False -> True
# not True -> False


# Function

# input -> function -> output
# print(input) -> input yes output no
# random() -> input no output yes
