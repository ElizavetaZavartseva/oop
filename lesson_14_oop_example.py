import random


class Data:
    def __init__(self, *info):
        self.info = list(info)

    def __getitem__(self, i):
        return self.info[i]


class Teacher:
    def __init__(self):
        self.work = 0

    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
            self.work += 1


class Pupil:
    def __init__(self):
        self.knowledge = []

    def take(self, info):
        self.knowledge.append(info)

    def loose(self):
        self.knowledge.remove(random.choice(self.knowledge))

lesson = Data('class', 'object', 'inheritance', 'polymorphism', 'encapsulation')
marIvanna = Teacher()
vasy = Pupil()
pety = Pupil()
marIvanna.teach(lesson[2], vasy, pety)
marIvanna.teach(lesson[0], pety)

print("Vasy", vasy.knowledge)

print("Pety", pety.knowledge)

vasy.take(lesson[3])

print("Vasy", vasy.knowledge)

vasy.loose()
print("Vasy has lost some knowledge", vasy.knowledge)