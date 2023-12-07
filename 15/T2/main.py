import math

class MyMath:
    @classmethod
    def circle_circumference(cls, radius):
        return 2 * math.pi * radius

    @classmethod
    def circle_area(cls, radius):
        return math.pi * radius ** 2

    @classmethod
    def cube_volume(cls, side_length):
        return side_length ** 3

    @classmethod
    def sphere_surface_area(cls, radius):
        return 4 * math.pi * radius ** 2

res_1 = MyMath.circle_circumference(radius=5)
res_2 = MyMath.circle_area(radius=6)
print(res_1)
print(res_2)
