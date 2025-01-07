import module as m

r1 = m.Room(6, 3, 2.7)
print(r1.get_total_square())  # выведет 48.6

r1.add_wd(1, 1)
r1.add_wd(3, 1)
r1.add_wd(1, 2)

input1 = float(input("Please, enter the wallpaper roll width: "))
input2 = float(input("Please, enter the wallpaper roll length: "))

print(r1.get_work_square())  # выведет 44.6
# print(r1.wallpaper_calculation(0.53, 10.05))
print(r1.wallpaper_calculation(input1, input2))