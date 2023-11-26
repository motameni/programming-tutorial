temperature = 'N'
type_of_weathers = ["Freezing", "Cold", "Moderate", "Warm"]

if type(temperature) != int and type(temperature) != float:
    print("Invalid")

elif temperature <= 0:
    print("Freezing")

elif 0 < temperature <= 12:
    print("Cold")

elif 12 < temperature <= 24:
    print("Moderate")

elif temperature > 24:
    print ("Warm")

