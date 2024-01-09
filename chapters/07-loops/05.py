from_number = 3
to_number = 150

generated_list = []

for i in range(-1_000_000_000_000, 1_000_000_000_000):
    if from_number <= i < to_number:
        generated_list.append(i)

print(generated_list)
