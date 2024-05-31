import math


class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        return 2 * ((self.radius**2) * math.pi) + 2 * math.pi * self.radius * self.height

    def volume(self):
        return math.pi * (self.radius**2) * self.height


cylinder = Cylinder(2, 4)
print(cylinder.area())
print(cylinder.volume())
