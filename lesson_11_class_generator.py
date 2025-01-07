import random

def generator(qty, rng_st, rng_fn):
    while qty > 0:
        qty -= 1
        print("before", qty)
        yield random.randint(rng_st, rng_fn)
        print("after", qty)

# a = generator(5, 30,100)

# for i in a:
#     print("out", i)


def generator1():
    # create table
    print("start")
    yield from generator(10, 0, 10)
    print("end")
    # table.truncate()
b = generator1()

for i in b:
    print("out", i)