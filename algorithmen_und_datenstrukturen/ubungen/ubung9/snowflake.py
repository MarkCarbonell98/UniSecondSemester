
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = (x**2 + y**2)**(.5)
    
    def __repr__(self):
        return f"Vec({self.x},{self.y}, {self.length})"

vec1 = Vector(0, 0)
vec2 = Vector(1, 0)
vec3 = Vector(.5, (3**(.5))/2)
print(vec1)
print(vec2)
print(vec3)

class KochSnowflake:
    def __init__(self, vec1, vec2, vec3):
        self.sides = [vec1, vec2, vec3]

    def divide(self, amount):
        for i in range(amount):
            for j in range(len(self.sides)):
                self.sides.append("hallo")
                self.sides.append("hallo")
                self.sides.append("hallo")

    def __repr__(self):
        result = ""
        for vec in self.sides:
            result += " " + repr(vec)
        return result

snowflake = KochSnowflake(vec1, vec2, vec3)
snowflake.divide(1)
print(snowflake)
