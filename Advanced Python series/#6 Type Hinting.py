'''def func(num: int | float) -> int | float:
    return num*2

print(func(3.2))'''


'''class Vector:
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __add__(self, vector: Vector) -> Vector:
        return Vector(self.x+vector.x, self.y+vector.y)
    
    
#if __name__=="__main__":
vec = Vector(2,5)
vec2 = Vector(3,4)
vec3 = vec+vec2
print(vec3)'''