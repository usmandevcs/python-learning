# Problem 5:
'''
Write a class vector representing a vector of n dimensions. Overload 
the + and * operator which calculates the sum and the dot(.) product 
of them. 
'''
class Vector:
    def __init__(self, components):
        self.components = components  # list or tuple of numbers

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Dimension mismatch in addition")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Dimension mismatch in dot product")
        dot = sum(a * b for a, b in zip(self.components, other.components))
        return dot

    def __str__(self):
        return f"Vector({self.components})"

# Example usage:
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = Vector([7, 8, 9])
v4 = Vector([10, 11, 12])

v5 = v1 + v2        # Vector addition
dot1 = v1 * v2       # Dot product
v6 = v3 + v4
dot2 = v3 * v4

print(v5)           # Vector([5, 7, 9])
print(dot1)          # 32
print(v6)           # Vector([17, 19, 21])
print(dot2)          # 266