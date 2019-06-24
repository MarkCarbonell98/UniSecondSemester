from math import sin, cos
import numpy as np

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = (x**2 + y**2)**(.5)

    def getPerpendicular(self):
        return Vector(-self.y, self.x)

    def __mul__(self,num):
        return Vector(self.x * num, self.y * num)
    
    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector):
        return Vector(self.x - vector.x , self.y - vector.y)
    
    def __repr__(self):
        return f"Vec({self.x}, { self.y}, {self.length})"

# Unterteilungsregel 


vertex1 = Vector(0, 0)
vertex2 = Vector(1, 0)
vertex3 = Vector(.5, (3**(.5))/2)

def kochSnowflake(level):
    if level == 0:
        # initial triangle
        angles = np.array([0, 120, 240]) + 90
        return 1 / np.sqrt(3) * np.exp(np.deg2rad(angles) * 1j)
    else:
        ZR = 0.5 - 0.5j * np.sqrt(3) / 3
        p1 = kochSnowflake(level - 1) 
        p2 = np.roll(p1, shift=-1)  
        dp = p2 - p1  
        new_points = np.empty(len(p1) * 4, dtype=np.complex128)
        print(new_points, p1, p2, ZR, dp)
        new_points[::4] = p1
        new_points[1::4] = p1 + dp / 3
        new_points[2::4] = p1 + dp * ZR
        new_points[3::4] = p1 + dp / 3 * 2
        print(new_points)
        return new_points

def kochSnowflake2(level):
    start = [Vector(0,0), Vector(.5, (3**(.5))/2) ,Vector(1,0)]
    if level == 0:
        return start
    connectionVector = (start[2] - start[0]) + start[0]
    middlePoint = connectionVector * .5
    l = connectionVector * (1/3)
    x1 = l
    x2 = l * 2
    invertedMiddlePoint = Vector.getPerpendicular(middlePoint)
    middleUnitVector = invertedMiddlePoint * (1/invertedMiddlePoint.length)
    height = (l.length**2 - (l.length/2)**2)**(1/2)
    x3 = middlePoint + (middleUnitVector * height)
    # oldPoints = kochSnowflake(level - 1)



class KochSnowflake:
    def __init__(self, p1, p2, p3):
        self.sides = [p1, p2, p3]

    def divide(self):
        connectionVector = (self.sides[2] - self.sides[0]) + self.sides[0]
        middlePoint = connectionVector *.5
        l = connectionVector * (1/3)
        x1 = l
        x2 = l * 2
        invertedMiddlePoint = Vector.getPerpendicular(middlePoint)
        middleUnitVector = invertedMiddlePoint * (1/invertedMiddlePoint.length) 
        height = (l.length**2 - (l.length/2)**2)**(1/2)
        x3 = middlePoint + (middleUnitVector * height)
        print(x1,x2,x3)
        

        temp = self.sides[2]
        self.sides[2] = self.sides[1]
        self.sides[1] = temp
        self.sides.insert(1,x1)
        self.sides.insert(2,x3)
        self.sides.insert(3,x2)
        

x = []
y = []
points = kochSnowflake(1)
x, y = points.real, points.imag
import matplotlib.pyplot as plt
plt.figure(figsize=(8,8))
plt.axis('equal')
plt.fill(x,y)
plt.show()
