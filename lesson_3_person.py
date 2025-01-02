class Person:
    def __init__(self, name, surename, qualification=1):
        self.name = name
        self.surname = surename
        self.qualification = qualification

    def get_full_name(self):
        return self.name + " " + self.surname + " " + " " + str(self.qualification)

    def __del__(self):
        print(f"Good bye! {self.get_full_name()}")

def main():

    a = Person("Nikita", "Zavartsev", 3)
    b = Person("Elizaveta", "Zavartseva", 2)
    c = Person("Fridolin", "Herbert")

    completion = input()

    min_q = min(a.qualification, b.qualification, c.qualification)

    for ob in [a, b, c]:
        if ob.qualification == min_q:
            del ob

    print(a.get_full_name())
    print(b.get_full_name())
    print(c.get_full_name())

    del c

    completion = input()

if __name__ == "__main__":
    main()