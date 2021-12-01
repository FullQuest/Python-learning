# Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples
# return the slope and distance of the line.
from math import sqrt

print('\nProblem 1 - Line class. Instances defined by 2 coordinates')

class Line():

    def __init__(self, cord1, cord2):
        self.cord1 = cord1
        self.cord2 = cord2

    def distance(self):
        return sqrt((self.cord2[0] - self.cord1[0]) ** 2 + (self.cord2[1] - self.cord1[1]) ** 2)

    def __str__(self):
        return f"Coordinate1 is {self.cord1}, coordinate2 is {self.cord2}"

    def slope(self):
        return (self.cord2[1]-self.cord1[1])/(self.cord2[0]-self.cord1[0])


coordinate1 = (3, 2)
coordinate2 = (8, 10)
my_line = Line(coordinate1, coordinate2)

print(f"The distance is {my_line.distance()}")
print(f"The slope is {my_line.slope()}")
print(my_line)
print('\nProblem 2. Define cylinder class that will have volume and surface_area methods')


# Problem 2. Define cylinder class that will have volume and surface_area methods
class Cylinder():
    pi = 3.14

    def __init__(self, radius=1, height=1):
        self.radius = radius
        self.height = height
        self.circle_surface_area = self.pi * self.radius ** 2
        self.circle_len = 2 * self.pi * self.radius

    def __len__(self):
        return self.height

    def __str__(self):
        return f'Cylinder with radius = {self.radius}, height = {self.height}'

    def volume(self):
        return self.circle_surface_area * self.height

    def surface_area(self):
        return self.circle_len * self.height + 2 * self.circle_surface_area


my_cylinder = Cylinder(height=2, radius=3)

print(my_cylinder.volume())
print(my_cylinder.surface_area())
print(len(my_cylinder))
print(my_cylinder)
