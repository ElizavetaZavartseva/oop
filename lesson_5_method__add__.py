class MethodAdd:

    def __init__(self, arg):
        self.arg = arg
        self.__arg2 = arg

    def __add__(self, arg2):
        return MethodAdd(self.arg + arg2.arg)

a = MethodAdd(1)
b = MethodAdd(2)

res = a + b

print(res.arg)
