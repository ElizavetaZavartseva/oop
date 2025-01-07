from math import pi


class Cylinder:
    num_cylinders = 0
    @staticmethod
    def make_area(d, h):
        circle = pi * d ** 2 / 4
        side = pi * d * h
        return round(circle * 2 + side, 2)

    @classmethod
    def increment_num_cylinders(cls):
        cls.num_cylinders += 1
        print(cls)

    def __init__(self, di, hi):
        self.dia = di
        self.h = hi
        self.__area = self.make_area(di, hi)
        self.increment_num_cylinders()

    def __setattr__(self, attr, value):
        self.__dict__[attr] = value
        if hasattr(self, "dia") and hasattr(self, "h") and hasattr(self, "_Cylinder__area") and attr != "_Cylinder__area":
            self.__area = self.make_area(self.dia, self.h)

    def get_area(self):
        return self.__area


a = Cylinder(1, 2)
print(a.get_area())
print(a.dia)
print(a.__dict__)

b = Cylinder(1, 2)
c = Cylinder(1, 2)

a.dia = 4
print(a.get_area())
print(a.dia)
print(a.__dict__)
print(Cylinder.num_cylinders)



