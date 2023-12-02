# BMI: https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html

weight_kg = int(input("Enter weight (kg): "))
height_cm = int(input("Enter height (cm): "))

height_m = height_cm / 100

bmi = weight_kg / height_m ** 2

message = "BMI is %.2f" % bmi

print(message)
