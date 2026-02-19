# Problem 1:
'''
Create a class (2-D vector) and use it to create another class 
representing a 3-D vector. 
'''
class Vector2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j
    def show(self):
            return f"2D vector: {self.i}i + {self.j}J"
class Vector3D(Vector2D):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def show(self):
            return f"3D vector: {self.i}i + {self.j}j + {self.k}k"
a = Vector2D(2, 3)
print(a.show())
b = Vector3D(4, 5, 6)
print(b.show())