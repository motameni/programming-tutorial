# python -m venv .venv
# source .venv/bin/activate
# pip install numpy

height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 95.25, 86.18, 88.45]

length = len(height)

bmi = [0] * length

for i in range(length):
    if height[i] != None and weight[i] != None:
        bmi[i] = weight[i] / height[i] ** 2
        temp_bmi = int(bmi[i] * 100)
        bmi[i] = temp_bmi / 100
    else:
        bmi[i] = None

print(bmi)


# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2
bmi = bmi.round(2)

print(type(bmi))
print(np.average(bmi))

print(type(bmi.tolist()))

print(bmi[bmi > 25])
