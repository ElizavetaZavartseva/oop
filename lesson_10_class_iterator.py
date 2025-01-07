import random
# from typing import Iterable


class ClassIterator:
    def __init__(self, qty, rng_st, rng_fn):
        self.qty = qty
        self.rng_st = rng_st
        self.rng_fn = rng_fn

    def __iter__(self):
        return self

    def __next__(self):
        if self.qty > 0:
            self.qty -= 1
            return random.randint(self.rng_st, self.rng_fn)
        else:
            raise StopIteration

a = ClassIterator(5, 1, 100)

for i in a: # <-- iter(a)
    # i <-- next(iter_a_)
    # if StopIteration ->> stop
    # do something, your code
    print(i)

# isinstance([], Iterable)