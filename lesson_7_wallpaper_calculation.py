# import typing as t
# class WinDoor:
#     def __init__(self, x, y):
#         self.square = x * y
#
# class Room:
#     def __init__(self, width, length, height):
#         self.width = width
#         self.length = length
#         self.height = height
#         self.wd = []
#         # self.total_square: float = 0.0
#         # self.work_square: float = 0.0
#         # self.get_total_square()
#         # self.get_work_square()
#
#     def add_wd(self, w, h):
#         self.wd.append(WinDoor(w, h))
#
#     def get_total_square(self):
#         self.total_square = 2 * self.height * (self.width + self.length)
#         return self.total_square
#
#     def get_work_square(self):
#         self.work_square = self.total_square
#         for i in self.wd:
#             self.work_square -= i.total_square
#         return self.work_square
#
#     def wallpaper_calculation(self, wp_width: float ,wp_length: float):
#         wp_square = wp_width * wp_length
#         wallpaper_calc = self.work_square / wp_square
#         return wallpaper_calc
#
# r1 = Room(6, 3, 2.7)
# print(r1.get_total_square())  # выведет 48.6
# r1.add_wd(1, 1)
# r1.add_wd(1, 1)
# r1.add_wd(1, 2)
#
# input1 = float(input("Please, enter the wallpaper roll width: "))
# input2 = float(input("Please, enter the wallpaper roll length: "))
#
# print(r1.get_work_square())  # выведет 44.6
# # print(r1.wallpaper_calculation(0.53, 10.05))
# print(r1.wallpaper_calculation(input1, input2))


import typing as t
class WinDoor:
    def __init__(self, x, y):
        self.square = x * y

class Room:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height
        self.wd: list[WinDoor] = []

    def add_wd(self, w, h):
        self.wd.append(WinDoor(w, h))

    def get_total_square(self):
        total_square = 2 * self.height * (self.width + self.length)
        return total_square

    def get_work_square(self):
        work_square = self.get_total_square()
        for i in self.wd:
            work_square -= i.square
        return work_square

    def wallpaper_calculation(self, wp_width: float ,wp_length: float):
        wp_square = wp_width * wp_length
        wallpaper_calc = self.get_work_square() / wp_square
        return wallpaper_calc

r1 = Room(6, 3, 2.7)
print(r1.get_total_square())  # выведет 48.6

r1.add_wd(1, 1)
r1.add_wd(1, 1)
r1.add_wd(1, 2)

input1 = float(input("Please, enter the wallpaper roll width: "))
input2 = float(input("Please, enter the wallpaper roll length: "))

print(r1.get_work_square())  # выведет 44.6
# print(r1.wallpaper_calculation(0.53, 10.05))
print(r1.wallpaper_calculation(input1, input2))
