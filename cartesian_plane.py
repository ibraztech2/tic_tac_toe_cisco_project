from math import hypot


class Point:
    def __init__(self, __x=0.0, __y=0.0):
        self.__x2 = __x
        self.__y2 = __y

    def getx(self):
        return self.__x2

    def gety(self):
        return self.__y2

    def distance_from_xy(self, __x, __y):
        self.__x1 = __x
        self.__y1 = __y
        __distancexy = hypot(float(self.__x1 - self.__x2), float(self.__y1 - self.__y2))
        return __distancexy

    def distance_from_point(self, __point):
        return self.distance_from_xy(__point.getx(), __point.gety())


class Triangle(Point):
    def __init__(self, __vertice1, __vertice2, __vertice3):
        Point.__init__(self)
        __x1, __y1 = __vertice1.getx(), __vertice1.gety()
        __x2, __y2 = __vertice2.getx(), __vertice2.gety()
        __x3, __y3 = __vertice3.getx(), __vertice3.gety()
        self.__distance12 = hypot(float(__x1 - __x2), float(__y1 - __y2))
        self.__distance23 = hypot(float(__x3 - __x2), float(__y3 - __y2))
        self.__distance13 = hypot(float(__x1 - __x3), float(__y1 - __y3))

    def perimeter(self):
        self.perimeter_ = self.__distance12 + self.__distance23 + self.__distance13
        return self.perimeter_


point1 = Point(0, 0)
point2 = Point(1, 0)
point3 = Point(0, 1)
triangle = Triangle(point1, point2, point3)
print(point1.distance_from_point(point2))
print(f"{point2.distance_from_xy(2, 0):}")
print(triangle.perimeter())

