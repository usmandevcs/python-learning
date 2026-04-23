# Introduction:
'''
Numpy is a powerful library in Python for numerical computing. 
It provides support for large, multi-dimensional arrays and matrices, 
along with a collection of mathematical functions to operate on 
these arrays efficiently. Numpy is widely used in data science, 
machine learning, and scientific computing due to its speed and 
ease of use.
'''
# What is Numpy? and numerical computing? and why is it important?
'''
Numpy is a library in Python that provides support for large, 
multi-dimensional arrays and matrices, along with a collection o
f mathematical functions to operate on these arrays efficiently.
Numerical computing:
Numerical computing refers to the use of algorithms and computational 
techniques to solve mathematical problems that involve numerical 
data. 
Importance of Numpy:
Numpy is important because it allows for efficient manipulation and 
analysis of large datasets, making it a fundamental tool for data 
scientists, machine learning practitioners, and researchers in 
various scientific fields.
'''
# Importing Numpy:
import numpy as np
# Creating Numpy Arrays:
# 1D Array:
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)
# 2D Array:
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)
# 3D Array:
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array:\n", array_3d)
# Array Attributes:
print("Shape of 2D Array:", array_2d.shape)
print("Data Type of 1D Array:", array_1d.dtype)
print("Number of Dimensions of 3D Array:", array_3d.ndim)
print("Size of 2D Array:", array_2d.size)
# Array Operations:
# Element-wise addition:
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
result_add = array_a + array_b
print("Element-wise Addition:", result_add)
# Element-wise multiplication:
result_mul = array_a * array_b
print("Element-wise Multiplication:", result_mul)
# Broadcasting:
array_c = np.array([1, 2, 3])
result_broadcast = array_c + 10
print("Broadcasting Result:", result_broadcast)
# Conclusion:
'''Numpy is a fundamental library for numerical computing in Python,
providing powerful tools for working with arrays and performing
efficient mathematical operations. It is essential for data science,
machine learning, and scientific computing tasks.'''