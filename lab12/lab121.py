import math


class Point:

    def __init__(self, x, y, z):
        self.coord = (x, y, z)

    def distance_to_another_point(self, point_coord):
        if len(point_coord) != 3:
            exit('Tuple of coordinates should be length of 3')
        x, y, z = point_coord
        distance = math.sqrt((x - self.coord[0]) ** 2 + (y - self.coord[1]) ** 2 + (z - self.coord[2]) ** 2)
        return distance


class Triangle:

    def __init__(self, point_x, point_y, point_z):
        self.points = (point_x, point_y, point_z)

    def is_existence(self):
        A = self.points[0].coord
        B = self.points[1].coord
        C = self.points[2].coord

        self.AB = self.points[0].distance_to_another_point(B)
        self.BC = self.points[1].distance_to_another_point(C)
        self.CA = self.points[2].distance_to_another_point(A)
        if self.AB + self.BC > self.CA:
            return True
        else:
            return False

    def perimeter(self):
        if self.is_existence():
            return self.AB + self.BC + self.CA
        else:
            exit('Impossible to calculate the perimeter of non existent triangle')

    def area(self):
        if self.is_existence():
            s = self.perimeter() / 2
            area = math.sqrt(s * (s - self.AB) * (s - self.BC) * (s - self.CA))
            return area
        else:
            exit('Impossible to calculate the area of non existent triangle')



point = Point(1, 2, 3)
print(point.distance_to_another_point((-7, -2, 4)))

pointA = Point(1, 2, 3)
pointB = Point(-1, 2, 5)
pointC = Point(1, 4, 3)

triangle = Triangle(pointA, pointB, pointC)
print('Existence of triangle: ', triangle.is_existence())
print('Triangle perimeter: ', triangle.perimeter())
print('Triangle area:', triangle.area())
