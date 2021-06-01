# class Person:
#     intro = "안녕하세요."
#     def __init__(self, name, age, school):
#         self.name = name
#         self.age = age
#         self.school = school
#
#     def say_hello(self):
#         print("{intro} 저는 {name}입니다. 제 나이는 {age}입니다. 저는 {school}을 다닙니다.".format(intro=self.intro, name=self.name, age=self.age, school=self.school))
#
# i = Person("Jason", "29", "Yonsei University")
# i.say_hello()


# class Circle:
#     pi = 3.14
#
#     def __init__(self, r):
#         self.r = r
#         print(self.pi)
#         print(self.r)
#
#     def surface_area(self):
#         return (self.pi)*(self.r*self.r)
#
#     def circumference(self):
#         return 2*(self.pi)*self.r
#
# a = Circle(5)

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

import numpy as np

input("마운틴 던전을 소환하려면 m을 입력하세요 ----> ")
print("마운틴 던전을 소환합니다.")
A = np.full((30,10), "^")
print(A)
print("--------------------------")
input("던전 보스몹들을 소환하려면 d를 입력하세요 ----> ")
print("던전 보스몹들을 소환합니다. 숫자 7, 8, 9가 보스몹들입니다.")
A[18,2] = 7
A[19,2] = 7
A[20,2] = 7
A[18,3] = 7
A[19,3] = 7
A[20,3] = 7
A[18,4] = 7
A[19,4] = 7
A[20,4] = 7
A[18,5] = 7
A[19,5] = 7
A[20,5] = 7
A[23,6] = 8
A[24,6] = 8
A[25,6] = 8
A[23,7] = 8
A[24,7] = 8
A[25,7] = 8
A[23,8] = 8
A[24,8] = 8
A[25,8] = 8
A[29,9] = 9
print(A)
print("--------------------------")
input("유저 캐릭터를 만드려면 c를 입력하세요 ----> ")
print("캐릭터를 소환합니다. 숫자 1이 유저 캐릭터입니다.")
A[0,0] = 1
print(A)
print("--------------------------")

def move(A):
    a = input("움직일 방향의 번호를 입력하세요. 1.w 2.s 3.a 4.d ----> ")
    if a == "w":
        print("위로 한칸 움직였습니다.")
        # print("Moving player 1 to the right - step 1: find 2")
        a = np.where(A == "1")
        # print(a)
        # print("--------------------------")
        # print("Moving player 1 to the right - step 2: Change 2 to 1")
        A[a] = "^"
        # print(A)
        # print("--------------------------")
        # print("Moving player 1 to the right - step 3: Change a value on the right to 2")
        # https://moonbooks.org/Articles/How-to-extract-a-small-matrix-by-selecting-neighbors-for-a-given-index-using-numpy-in-python-/
        up = (a[0]-1, a[1])
        A[up] = 1
        print(A)

    elif a == "s":
        print("아래로 한칸 움직였습니다.")
        # print("Moving player 1 to the right - step 1: find 2")
        a = np.where(A == "1")
        # print(a)
        # print("--------------------------")
        # print("Moving player 1 to the right - step 2: Change 2 to 1")
        A[a] = "^"
        # print(A)
        # print("--------------------------")
        # print("Moving player 1 to the right - step 3: Change a value on the right to 2")
        # https://moonbooks.org/Articles/How-to-extract-a-small-matrix-by-selecting-neighbors-for-a-given-index-using-numpy-in-python-/
        down = (a[0]+1, a[1])
        A[down] = 1
        print(A)

    elif a == "a":
        print("왼쪽으로 한칸 움직였습니다.")
        # print("Moving player 1 to the right - step 1: find 2")
        a = np.where(A == "1")
        # print(a)
        # print("--------------------------")
        # print("Moving player 1 to the right - step 2: Change 2 to 1")
        A[a] = "^"
        # print(A)
        # print("--------------------------")
        # print("Moving player 1 to the right - step 3: Change a value on the right to 2")
        # https://moonbooks.org/Articles/How-to-extract-a-small-matrix-by-selecting-neighbors-for-a-given-index-using-numpy-in-python-/
        left = (a[0], a[1]-1)
        A[left] = 1
        print(A)

    if a == "d":
        print("오른쪽으로 한칸 움직였습니다.")
        # print("Moving player 1 to the right - step 1: find 2")
        a = np.where(A == "1")
        # print(a)
        # print("--------------------------")
        # print("Moving player 1 to the right - step 2: Change 2 to 1")
        A[a] = "^"
        # print(A)
        # print("--------------------------")
        # print("Moving player 1 to the right - step 3: Change a value on the right to 2")
        # https://moonbooks.org/Articles/How-to-extract-a-small-matrix-by-selecting-neighbors-for-a-given-index-using-numpy-in-python-/
        right = (a[0], a[1]+1)
        A[right] = 1
        print(A)

    else:
        move(A)

for i in range(100):
    move(A)
