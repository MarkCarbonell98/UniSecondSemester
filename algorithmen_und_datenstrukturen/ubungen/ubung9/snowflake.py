from math import sin, cos

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = (x**2 + y**2)**(.5)

    @staticmethod
    def calculateThirdVertex(vector1, vector2):
        return Vector((vector1.x + vector2.x + (vector1.y - vector2.y)**(1/3))/2, ((vector1.y + vector2.y + (vector2.x - vector1.x)**(1/3))/2))

    def __mul__(self,num):
        return Vector(self.x * num, self.y * num)
    
    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector):
        return Vector(vector.x - self.x, vector.y - self.y)
    
    def __repr__(self):
        return f"Vec({self.x},{self.y}, {self.length})"


vertex1 = Vector(0, 0)
vertex2 = Vector(1, 0)
vertex3 = Vector(.5, (3**(.5))/2)

side1 = vertex1 - vertex2
side2 = vertex1 - vertex3
side3 = vertex2 - vertex3
print(side1, side2, side3)


class KochSnowflake:
    def __init__(self, vec1, vec2, vec3):
        self.sides = [side1, side2, side3]

    def divide(self):
        oneThird = 1/3
        newSides = []
        for i in range(len(self.sides)):
            newVector = self.sides[i] * oneThird
            print(newVector)
        


snowflake = KochSnowflake(side1, side2, side2)
snowflake.divide()
print(snowflake)


# import matplotlib.pyplot as plt
# plt.figure(figsize=(8,8))
# plt.axis('equal')
# plt.fill(x,y)
# plt.show()
