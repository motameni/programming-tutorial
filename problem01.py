# Question:
# You are given the following variables:

# name = "Alice"
# age = 30
# height = 5.8
# is_student = False

# Write Python code to do the following:
# Calculate the year of birth (birth_year) based on the current year (considering the current year as 2023) and the age.
# Create a new variable is_teenager and assign it a Boolean value True if the age is between 13 and 19 (inclusive), or False otherwise.
# Determine the data type of each variable (name, age, height, is_student) and store them in separate variables (name_type, age_type, height_type, is_student_type).
# This question assesses your knowledge of variables, data types, and basic calculations in Python.

name = "Alice" # string
age = 30 # int
height = 5.8 # float
is_student = False # bool
current_year = 2023

# Calculate the year of birth

birth_year = current_year - age

    # step 1: birth_year = current_year - age
    # step 2: birth_year = 2023 - 30
    # step 3: birth_year = 1993

# Calculate is_teenager

    # approach 1: is_teenager = (13 <= age) and (age <= 19)
    # approach 2: is_teenager = 13 <= age <= 19

        # step 1: is_teenager = 13 <= age <= 19
        # step 2: is_teenager = 13 <= age and age <= 19
        # step 3: is_teenager = True and False
        # step 4: is_teenager = False

    # approach 3:

    # is_teenager = False
    # if 13 <= age:
    #     if age <= 19:
    #         is_teenager = True

    # approach 4:

is_teenager = None

if 13 <= age:
    if age <= 19:
        is_teenager = True
    else:
        is_teenager = False
else:
    is_teenager = False

# Determine types of the variables

name_type = type(name)
age_type = type(age)
height_type = type(height)
is_student_type = type(is_student)

# Print the results
print(birth_year)
print(is_teenager)
print(name, age, height, is_student)
print(name_type, age_type, height_type, is_student_type)

# Note:

# Operator Priority (High to Low):
# ()
# **
# * /
# + -

# Logical Combination of "and":
# True and True => True
# True and False => False
# False and True => False
# False and False => False

# Logical Combination of "or":
# True or True => True
# True or False => True 
# False or True => True
# False or False => False


# if and and or operates from left to right:

# step 1: True and True and True or False
# step 2: True and True or False
# step 3: True or False
# step 4: True

# How to run using Terminal?
# 1. Open new terminal from the menu
# 2. Run this command:
    # python3 file_name.py
    
    # Linux note:
    # ls: list of files and directories in the current dirctory
    # pwd: show the path of the current directory
