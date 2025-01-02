import random


class GameEntity:
    def __init__(self, id, team):
        self.id = id
        self.team = team

class Hero(GameEntity):
    def __init__(self, id, team):
        super().__init__(id, team)
        self.level = 0
    def level_up(self):
        self.level += 1

class Soldier(GameEntity):

    def follow_hero(self, hero: Hero):
        print(f"I'm soldier {self.id}, following my Hero {hero.id}.")

class Team:
    def __init__(self, team_name: str, hero: Hero):
        self.name = team_name
        self.hero = hero
        self.soldiers: list[Soldier] = []


    def set_hero(self, hero: Hero):
        if self.hero is None:
            self.hero = hero
        else:
            raise Exception("Team already has a hero!")

    def add_soldier(self, soldier: Soldier):
        self.soldiers.append(soldier)

def main():

    a = Hero(id=1, team="a")
    b = Hero(id=2, team="b")
    c = Hero(id=3, team="c")

    teams: dict[str, Team] = {
        "a": Team(team_name="a", hero=a),
        "b": Team(team_name="b", hero=b),
        "c": Team(team_name="c", hero=c),
    }

    for i in range(100):
        current_team = random.choice(["a", "b", "c"])
        current_soldier = Soldier(id=i+100, team=current_team)

        teams[current_team].add_soldier(current_soldier)


    biggest_team_val = 0
    biggest_team_name = ''

    for k,v in teams.items():
        print(f"Team {k} has {len(v.soldiers)}.")
        if len(v.soldiers) > biggest_team_val:
            biggest_team_val = len(v.soldiers)
            biggest_team_name = k

    teams[biggest_team_name].hero.level_up()

    random_soldier: Soldier = random.choice(teams[biggest_team_name].soldiers)

    random_soldier.follow_hero(hero=teams[biggest_team_name].hero)
    print(f"Hero: {teams[biggest_team_name].hero.id}\nSoldier: {random_soldier.id}")

if __name__ == "__main__":
    main()










