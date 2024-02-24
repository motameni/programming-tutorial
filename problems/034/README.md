# NumPy Challenge

This challenge requires you to work with NumPy, a powerful library for numerical computing in Python. You'll be dealing with a 2D NumPy array and performing various operations that will give you a hands-on experience with NumPy functions and techniques.

## Tasks

Given a 2D NumPy array of random integers between 1 and 100, complete the following tasks:

1. **Create Array:** Generate a 2D NumPy array of shape (10, 10) with random integers between 1 and 100.
2. **Overall Mean:** Compute the mean of the entire array.
3. **Row Means:** Compute the mean of each row.
4. **Column Means:** Compute the mean of each column.
5. **Closest to Mean:** Find the closest value to the overall mean within the array.
6. **Normalization:** Normalize the array so that the minimum value is 0 and the maximum is 1.
7. **Max Position:** Find the index of the maximum value in the array.
8. **Flattening:** Flatten the array into a single dimension.
9. **Reshaping:** Reshape the flattened array back to its original shape of (10, 10).
10. **Boolean Mask:** Create a boolean mask where all elements greater than the overall mean are set to `True` otherwise `False`.

## Guidelines

- Use `numpy.random.randint` to create the initial 2D array.
- Apply `numpy.mean` to calculate means.
- Utilize `numpy.abs` and `numpy.argmin` to find the value closest to the mean.
- Adjust array values to the [0, 1] range using the `min` and `max` methods of the array.
- Locate the maximum value using `numpy.argmax`.
- Convert the array shape with `numpy.ndarray.flatten` and `numpy.reshape`.
- Generate the boolean mask with comparison operators on the array.