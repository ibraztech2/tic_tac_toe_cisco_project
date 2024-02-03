from math import hypot
class Point:
    def __init__(self, __x = 0.0, __y = 0.0):
        self.__x2 = __x
        self.__y2 = __y

    def __getx(self):
        return self.__x2
    def __gety(self):
        return self.__y2
    def distance_from_xy(self,__x,__y):
        self.__x1 = __x
        self.__y1 = __y
        distancexy = hypot(float(self.__x1 - self.__x2),float(self.__y1 - self.__y2))
        return distancexy
    def distance_from_point(self,__point):
        self.__point = __point
        self.__x2= self.__getx()
        self.__y2 = self.__gety()
        self.__x1  = self.__point.__getx()
        self.__y1  = self.__point.__gety()
        distancexy = hypot(float(self.__x1 - self.__x2), float(self.__y1 - self.__y2))
        return distancexy


point = Point()
point1 = Point(0,0)
point2 = Point(1,1)
print(point1.distance_from_point(point2))
print(f"{point2.distance_from_xy(2,0):.2f}")