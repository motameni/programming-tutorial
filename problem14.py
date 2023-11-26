from_number = 3
to_number = 10

generated_list = []

havij_list = [0] * (to_number - from_number)

for _ in havij_list:
    generated_list.append(from_number)
    from_number = from_number + 1

print("Generated list is:", generated_list)
