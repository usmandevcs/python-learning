# Arrays:
'''
An array is a collection of items stored at contiguous memory 
locations. In the context of Numpy, an array is a grid of values, 
all of the same type, indexed by tuples of non-negative integers.
in simple terms, an array is a data structure that can hold multiple
values of the same type, and it allows for efficient storage and
manipulation of data. Numpy arrays are more efficient than Python
lists for numerical operations because they are implemented in C and
use less memory.
'''
# Types of Arrays:
'''
1. 1D Array: A single row or column of elements.
2. 2D Array: A matrix with rows and columns.
3. 3D Array: A cube of elements with depth, rows, and columns.
4. N-D Array: An array with N dimensions.
'''
# Explanation of each type of array:
'''
1. 1D Array: A one-dimensional array is a simple list of elements. 
    It can be thought of as a single row or column of data. For example, 
    [1, 2, 3, 4, 5] is a 1D array.
2. 2D Array: A two-dimensional array is a matrix that has rows and 
    columns. It can be visualized as a table of data. For example,
    [[1, 2, 3], [4, 5, 6]] is a 2D array.
3. 3D Array: A three-dimensional array is a cube of elements that has
    depth, rows, and columns. It can be visualized as a stack of 2D arrays. 
    For example, [[[1, 2], [3, 4]], [[5, 6], [7, 8]]] is a 3D array.
4. N-D Array: An N-dimensional array is an array that can have any number
    of dimensions. It is a generalization of the previous types of arrays.
    For example, a 4D array could be visualized as a stack of 3D arrays.
'''

# Creating and Manipulating Arrays:
'''
Numpy provides various functions to create and manipulate arrays.
1. Creating Arrays: You can create arrays using functions like np.array(), 
    np.zeros(), np.ones(), np.arange(), and np.linspace().
2. Manipulating Arrays: You can perform various operations on arrays,
    such as reshaping, slicing, indexing, and mathematical operations.
3. Array Attributes: Numpy arrays have attributes like shape, dtype, 
ndim, and size that provide information about the array.
4. Array Operations: You can perform element-wise operations, 
broadcasting, and other mathematical operations on arrays.
'''
