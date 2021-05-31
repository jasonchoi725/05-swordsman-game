import random

class Character:
    def __init__(self, name, job, level, power, skill1, skill2, skill3):
        self.name = name
        self.job = job
        self.level = level
        self.power = power
        self.skill1 = skill1
        self.skill2 = skill2
        self.skill3 = skill3

        self.skilllist = [self.skill1, self.skill2, self.skill3]

        print("제 이름은 {name}입니다. 저의 직업은 {job}입니다. 제 레벨은 {level}입니다."
              "제 파워는 {power}입니다. 제 스킬은 {skill1}, {skill2}, {skill3}입니다."
            .format(name=self.name, job=self.job, level=self.level,
                    power=self.power, skill1=self.skill1, skill2=self.skill2,
                    skill3=self.skill3))

    def damage(self):
        return self.level * self.power


class Battle:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def player_1_skill_damage(self):
        a = random.choice(self.player1.skilllist)
        if a == "vertical slash":
            return 3
        elif a == "side slash":
            return 2
        else:
            return 1

    def player_2_skill_damage(self):
        a = random.choice(self.player2.skilllist)
        if a == "vertical slash":
            return 3
        elif a == "side slash":
            return 2
        else:
            return 1

    def fight(self):
        total_damage1 = int(random.random() * 10 * self.player1.damage() * self.player_1_skill_damage())
        total_damage2 = int(random.random() * 10 * self.player2.damage() * self.player_2_skill_damage())
        if total_damage1 > total_damage2:
            print("player1 wins by", total_damage1, ">", total_damage2)
        else:
            print("player2 wins by", total_damage1, "<", total_damage2)


class RepeatBattles:
    def __init__(self, player1, player2, Battle):
        self.player1 = player1
        self.player2 = player2
        self.Battle = Battle

    def repeat_three(self):
        for i in range(5):
            self.Battle.fight()


jason = Character("Jason", "swordsman", 1, 1, "vertical slash", "side slash", "diagonal slash")
ben = Character("Ben", "swordsman", 1, 1, "vertical slash", "side slash", "diagonal slash")
Battle(jason, ben).fight()
# RepeatBattles(jason, ben, Battle(jason, ben)).repeat_three()
