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

    def player_1_skill_type(self):
        # a = random.choice(self.player1.skilllist)
        a = input("Choose a skill to use.[1,2,3]. 1.Vertical slash 2.Side slash 3.Diagonal slash  ---> ")
        if a == "1":
            b = "Vertical slash"
        elif a == "2":
            b = "Side slash"
        elif a == "3":
            b = "Diagonal slash"
        else:
            b = "Please restart"
        print("player1 used:", b)
        return b

    def player_2_skill_type(self):
        a = random.choice(self.player2.skilllist)
        print("player2 used:", a)
        return a

    def fight(self):
        p1_skill_type = self.player_1_skill_type()
        p2_skill_type = self.player_2_skill_type()
        if p1_skill_type == "Vertical slash" and p2_skill_type == "Vertical slash":
            # print(self.player_1_skill_damage())
            # print(self.player_2_skill_damage())
            total_damage1 = int(random.random() * 10 * self.player1.damage() * 1)
            total_damage2 = int(random.random() * 10 * self.player2.damage() * 1)
            if total_damage1 > total_damage2:
                print("player1 wins by", total_damage1, ">", total_damage2)
                return 1
            else:
                print("player2 wins by", total_damage1, "<", total_damage2)
                return 0
        elif p1_skill_type == "Vertical slash" and p2_skill_type == "Side slash":
            # print(self.player_1_skill_damage())
            # print(self.player_2_skill_damage())
            total_damage1 = int(random.random() * 10 * self.player1.damage() * 2)
            total_damage2 = int(random.random() * 10 * self.player2.damage() * 1)
            if total_damage1 > total_damage2:
                print("player1 wins by", total_damage1, ">", total_damage2)
                return 1
            else:
                print("player2 wins by", total_damage1, "<", total_damage2)
                return 0
        elif p1_skill_type == "Vertical slash" and p2_skill_type == "Diagonal slash":
            # print(self.player_1_skill_damage())
            # print(self.player_2_skill_damage())
            total_damage1 = int(random.random() * 10 * self.player1.damage() * 1)
            total_damage2 = int(random.random() * 10 * self.player2.damage() * 2)
            if total_damage1 > total_damage2:
                print("player1 wins by", total_damage1, ">", total_damage2)
                return 1
            else:
                print("player2 wins by", total_damage1, "<", total_damage2)
                return 0
        elif p1_skill_type == "Side slash" and p2_skill_type == "Side slash":
            # print(self.player_1_skill_damage())
            # print(self.player_2_skill_damage())
            total_damage1 = int(random.random() * 10 * self.player1.damage() * 1)
            total_damage2 = int(random.random() * 10 * self.player2.damage() * 1)
            if total_damage1 > total_damage2:
                print("player1 wins by", total_damage1, ">", total_damage2)
                return 1
            else:
                print("player2 wins by", total_damage1, "<", total_damage2)
                return 0
        elif p1_skill_type == "Side slash" and p2_skill_type == "Diagonal slash":
            # print(self.player_1_skill_damage())
            # print(self.player_2_skill_damage())
            total_damage1 = int(random.random() * 10 * self.player1.damage() * 2)
            total_damage2 = int(random.random() * 10 * self.player2.damage() * 1)
            if total_damage1 > total_damage2:
                print("player1 wins by", total_damage1, ">", total_damage2)
                return 1
            else:
                print("player2 wins by", total_damage1, "<", total_damage2)
                return 0
        elif p1_skill_type == "Side slash" and p2_skill_type == "Vertical slash":
            # print(self.player_1_skill_damage())
            # print(self.player_2_skill_damage())
            total_damage1 = int(random.random() * 10 * self.player1.damage() * 1)
            total_damage2 = int(random.random() * 10 * self.player2.damage() * 2)
            if total_damage1 > total_damage2:
                print("player1 wins by", total_damage1, ">", total_damage2)
                return 1
            else:
                print("player2 wins by", total_damage1, "<", total_damage2)
                return 0
        elif p1_skill_type == "Diagonal slash" and p2_skill_type == "Diagonal slash":
            # print(self.player_1_skill_damage())
            # print(self.player_2_skill_damage())
            total_damage1 = int(random.random() * 10 * self.player1.damage() * 1)
            total_damage2 = int(random.random() * 10 * self.player2.damage() * 1)
            if total_damage1 > total_damage2:
                print("player1 wins by", total_damage1, ">", total_damage2)
                return 1
            else:
                print("player2 wins by", total_damage1, "<", total_damage2)
                return 0
        elif p1_skill_type == "Diagonal slash" and p2_skill_type == "Vertical slash":
            # print(self.player_1_skill_damage())
            # print(self.player_2_skill_damage())
            total_damage1 = int(random.random() * 10 * self.player1.damage() * 2)
            total_damage2 = int(random.random() * 10 * self.player2.damage() * 1)
            if total_damage1 > total_damage2:
                print("player1 wins by", total_damage1, ">", total_damage2)
                return 1
            else:
                print("player2 wins by", total_damage1, "<", total_damage2)
                return 0
        elif p1_skill_type == "Diagonal slash" and p2_skill_type == "Side slash":
            # print(self.player_1_skill_damage())
            # print(self.player_2_skill_damage())
            total_damage1 = int(random.random() * 10 * self.player1.damage() * 1)
            total_damage2 = int(random.random() * 10 * self.player2.damage() * 2)
            if total_damage1 > total_damage2:
                print("player1 wins by", total_damage1, ">", total_damage2)
                return 1
            else:
                print("player2 wins by", total_damage1, "<", total_damage2)
                return 0
        else:
            print(1)
            # Battle(jason, ben).fight()



        # while self.player_1_skill_damage() == "vertical slash":
        #     if self.player_2_skill_damage() == "vertical slash":
        #         total_damage1 = int(random.random() * 10 * self.player1.damage() * 1)
        #         total_damage2 = int(random.random() * 10 * self.player2.damage() * 1)
        #         if total_damage1 > total_damage2:
        #             print("player1 wins by", total_damage1, ">", total_damage2)
        #         else:
        #             print("player2 wins by", total_damage1, "<", total_damage2)
        #     elif self.player_2_skill_damage() == "side slash":
        #         total_damage1 = int(random.random() * 10 * self.player1.damage() * 2)
        #         total_damage2 = int(random.random() * 10 * self.player2.damage() * 1)
        #         if total_damage1 > total_damage2:
        #             print("player1 wins by", total_damage1, ">", total_damage2)
        #         else:
        #             print("player2 wins by", total_damage1, "<", total_damage2)
        #     elif self.player_2_skill_damage() == "diagonal slash":
        #         total_damage1 = int(random.random() * 10 * self.player1.damage() * 1)
        #         total_damage2 = int(random.random() * 10 * self.player2.damage() * 2)
        #         if total_damage1 > total_damage2:
        #             print("player1 wins by", total_damage1, ">", total_damage2)
        #         else:
        #             print("player2 wins by", total_damage1, "<", total_damage2)




class RepeatBattles:
    def __init__(self, player1, player2, Battle):
        self.player1 = player1
        self.player2 = player2
        self.Battle = Battle

    # def append(self, number, number_list=[]):
    #     number_list.append(number)
    #     return number_list

    def repeat_three(self):
        a = 0
        for i in range(3):
            b = self.Battle.fight()
            a = a + b
        if a > 1:
            print("Player1 won the battle")
        else:
            print("Player1 lost the battle")
            # print(a)
            # a = list()
            # # if i <=30:
            # a.append(self.Battle.fight())
            # # else:
            # print(a)
            # # self.Battle.fight()
            # # print(self.Battle.fight())
            # # print(self.Battle.player_1_skill_damage())
            # # print(self.Battle.player_2_skill_damage())



# jason = Character("Jason", "swordsman", 1, 1, "Vertical slash", "Side slash", "Diagonal slash")
# ben = Character("Ben", "swordsman", 1, 1, "Vertical slash", "Side slash", "Diagonal slash")
# boss1 = Character("Boss", "swordsman", 2, 2, "Vertical slash", "Side slash", "Diagonal slash")
#
# RepeatBattles(ben, jason, Battle(ben, jason)).repeat_three()
# print("----------------------------------")
# RepeatBattles(ben, boss1, Battle(ben, boss1)).repeat_three()
