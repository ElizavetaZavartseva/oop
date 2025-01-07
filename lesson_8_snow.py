class Snow:
    def __init__(self, number_snowflakes: int):
        self.number_snowflakes = number_snowflakes
        self.i = 0

    def __call__(self, new_number_snowflakes):
        self.number_snowflakes = new_number_snowflakes

    def __add__(self, arg):
        add = self.number_snowflakes + arg
        return add

    def __sub__(self, arg):
        sub = self.number_snowflakes - arg
        return sub

    def __mul__(self, arg):
        mul = self.number_snowflakes * arg
        return mul

    def __truediv__(self, arg):
        truediv = self.number_snowflakes / arg
        return round(truediv)

    def make_snow(self, row_snowflakes):

        number_row = self.number_snowflakes // row_snowflakes
        remaining_snowflakes = self.number_snowflakes - (number_row * row_snowflakes)
        make_snow = ("*" * row_snowflakes +  "\n") * number_row + ("*" * remaining_snowflakes)
        make_snow = make_snow.strip("\n")
        return make_snow

    def __getitem__(self, item):
        if item == "Lisa":
            return "lol"
        raise KeyError(f"key {item} not found")

    def __next__(self):
        if self.i <= self.number_snowflakes:
            self.i += 1
            return self.i - 1
        else:
            raise StopIteration


    def __iter__(self):
        return self

    def __anext__(self):
        pass

    def __aiter__(self):
        pass


a = Snow(7)

b = a * 3
print(b)

c = a / 2
print(c)

print(a.make_snow(3))

a(6)
print(a.make_snow(3))

# print(a['Lisa1'])

for snowflake in a:
    print("test")