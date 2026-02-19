# Problem 6:
'''
Write __str__() method to print the vector as follows: 
            7i + 8j +10k  
Assume vector of dimension 3 for this problem. 
'''
class Vector:
    def __init__(self, components):
        if len(components) != 3:
            raise ValueError("This class supports only 3D vectors (i, j, k)")
        self.components = components

    def __add__(self, other):
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        dot = sum(a * b for a, b in zip(self.components, other.components))
        return dot

    def __str__(self):
        return f"{self.components[0]}i + {self.components[1]}j + {self.components[2]}k"

# Example usage:
v1 = Vector([7, 8, 10])
print(v1)   # Output: 7i + 8j + 10k
