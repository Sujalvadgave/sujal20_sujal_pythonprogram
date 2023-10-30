import numpy as np

# Create a 1D NumPy array
arr1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr1d)

# Create a 2D NumPy array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:")
print(arr2d)

# Create a 3D NumPy array
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("\n3D Array:")
print(arr3d)

# array with specific data type

a = np.array([1,2,3],datatype='i')
print(a)
print(np.power(a,2))