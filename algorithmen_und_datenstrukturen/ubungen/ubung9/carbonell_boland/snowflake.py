import numpy as np

def kochSnowflake(level):
    if level == 0:
        initialAngles = np.array([0,120,240])
        finalAngles = initialAngles + 90
        finalComplexRadians = np.deg2rad(finalAngles) * 1j 
        lastEdge =  np.exp(finalComplexRadians)
        triangleInitialScale = 1 / np.sqrt(3)
        return triangleInitialScale * lastEdge
    else:
        triangleTop = 0.5 - 0.5j * np.sqrt(3) / 3
        lastPoints = kochSnowflake(level - 1) 
        lastPointsShiftedLeft = np.roll(lastPoints, shift=-1)  
        connectionVector = lastPointsShiftedLeft - lastPoints  
        newTrianglePoints = np.empty(len(lastPoints) * 4, dtype=np.complex128) # an array of complex numbers to replace my manually created vector class
        newTrianglePoints[::4] = lastPoints
        newTrianglePoints[1::4] = lastPoints + connectionVector / 3
        newTrianglePoints[2::4] = lastPoints + connectionVector * triangleTop
        newTrianglePoints[3::4] = lastPoints + connectionVector / 3 * 2
        return newTrianglePoints

points = kochSnowflake(5)
x, y = points.real, points.imag
import matplotlib.pyplot as plt
plt.figure(figsize=(8,8))
plt.axis('equal')
plt.fill(x,y)
plt.show()
