'''
class Person:
    def __init__(self, name:str, age: int | float):
        self.name = name
        self.age = round(age, 1)
        
'''
import math
class Vector:
    def __init__(self, x:int | float, y:int | float):
        if isinstance(x, int) or isinstance(x, int):
            self.x = int(x)
            self.y = int(y)
        else:
            self.x = round(x, 2)
            self.y = round(y, 2)
        
        
    def __add__(self, vector):
        """Adds 2 Vectors

        Args:
            vector (Vector): Vector To Add

        Returns:
            Vector: Returns New Vector Created By Adding 2
        """
        return Vector(self.x + vector.x, self.y + vector.y)
    
    
    def __sub__(self, vector):
        """Substract 2 Vectors

        Args:
            vector (Vector): Vector To Substract

        Returns:
            Vector: Returns New Vector Created By Substracting 2
        """
        return Vector(self.x - vector.x, self.y - vector.y)
    
    
    def __mul__(self, vector):
        """Multiply 2 Vectors

        Args:
            vector (Vector): Vector To Multiply

        Returns:
            Vector: Returns New Vector Created By Multiplying 2
        """
        return Vector(self.x * vector.x, self.y * vector.y)
    
    
    def __truediv__(self, vector):
        """Devides 2 Vectors

        Args:
            vector (Vector): Vector To Devide

        Returns:
            Vector: Returns New Vector Created By Deviding 2
        """
        return Vector(round(self.x / vector.x, 2), round(self.y / vector.y, 2))

    
    def __repr__(self):
        """Return Shape Of Vector

        Returns:
            String: [X, Y]
        """
        return f'{[self.x, self.y]}'
    
    
    def __len__(self):
        """Return Len Of Vector

        Returns:
            int: Len Of Vector
        """
        return int(math.sqrt((self.x**2+self.y**2)))
            
    def __call__(self):
        return f'Len: {len(self)}\nShape: {self}'
        
v1 = Vector(10,20)
v2 = Vector(2,5)
v3 = v1/v2
print(v3())