import numpy as np

twod = np.array([[1, 2, 3], [4, 5, 6]])
oned = np.array([[1], [2], [3]])


print(twod)
print(oned)

res = np.dot(twod, oned)
print(res)

res = twod * twod
print(res)
