name = "Alice"  # string
age = 30  # int
height = 5.8  # float
is_student = False  # bool
current_year = 2023

# Calculate the year of birth

birth_year = current_year - age

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
