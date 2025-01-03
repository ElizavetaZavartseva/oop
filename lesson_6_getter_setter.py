class MyClass:
    def __init__(self, val1, val2):
        self.__val1 = val1
        self.__val2 = val2
        self.__val3 = None

    def get_val1(self):
        return self.__val1

    def get_val2(self):
        return self.__val2

    def calculate_val_3(self):
        self.__val3 = self.__val1 + self.__val2
        return self.__val3

    def set_val1(self, new_val):
        if new_val == 5:
            self.__val1 = new_val
            self.__val2 = 55
        self.__val1 = new_val

    def set_val2(self, new_val):
        if self.__val2 == 55:
            return
        self.__val2 = new_val

a = MyClass(1, 2)

print(a.get_val1())
print(a.get_val2())

a.set_val1(5)
a.set_val2(6)

print(a.get_val1())
print(a.get_val2())


class MyClass1:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
        self.val3 = None

    def calculate_val_3(self):
        self.val3 = self.val1 + self.val2
        return self.val3


a = MyClass1(1, 2)

a.calculate_val_3()

