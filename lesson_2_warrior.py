import random
class Warrior:
    health = 100

a = Warrior()
b = Warrior()

hit = [a, b]

while a.health > 0 and b.health > 0:
    hitter = random.choice(hit)
    if hitter == a:
        b.health -= 20
        print(f"Warrior 'a' attacked. Warrior 'b' has {b.health} health points. Warrior 'a' has {a.health} health points.")
    else:
        a.health -=20
        print(f"Warrior 'b' attacked. Warrior 'a' has {a.health} health points. Warrior 'b' has {b.health} health points.")

if a.health > b.health:
    print("Game over! Warrior 'a' has won.")
else:
    print("Game over! Warrior 'b' has won.")
