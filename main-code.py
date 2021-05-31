import random

class Swordsman:
    def __init__(self, name, job, level, power, skill):
        self.name = name
        self.job = job
        self.level = level
        self.power = power
        self.skill = skill
        print("제 이름은 {name}입니다. 저의 직업은 {job}입니다. 제 레벨은 {level}입니다. 제 파워는 {power}입니다. 제 주 스킬은 {skill}입니다.".format(
            name=self.name, job=self.job, level=self.level, power=self.power, skill=self.skill))

    def damage(self):
        return self.level * self.power


class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def fight(self):
        total_damage1 = int(random.random() * 10 * self.player1.damage())
        total_damage2 = int(random.random() * 10 * self.player2.damage())
        if total_damage1 > total_damage2:
            print("player1 wins", total_damage1, ">", total_damage2)
        else:
            print("player2 wins", total_damage1, "<", total_damage2)


class RepeatBattles:
    def __init__(self, player1, player2, Battle):
        self.player1 = player1
        self.player2 = player2
        self.Battle = Battle

    def repeat_three(self):
        for i in range(5):
            self.Battle.fight()


jason = Swordsman("Jason", "swordsman", 1, 1, "slash")
ben = Swordsman("Ben", "swordsman", 2, 2, "slash")
RepeatBattles(jason, ben, Battle(jason, ben)).repeat_three()
