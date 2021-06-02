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
            Battle(jason, ben).fight()



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


#
# RepeatBattles(ben, jason, Battle(ben, jason)).repeat_three()
# print("----------------------------------")
# RepeatBattles(ben, boss1, Battle(ben, boss1)).repeat_three()

import numpy as np

class Map:
    def __init__(self):
    #     # self.vertical = vertical
    #     # self.horizontal = horizontal
    #     print("게임을 시작합니다.")
        pass

    def print_map(self):
        print(Map().create_map())

    def create_map(self):
        v = int(input("원하는 맵의 세로 길이를 입력하세요 (<21) ----> "))
        h = int(input("원하는 맵의 가로 길이를 입력하세요 (<11) ----> "))
        A = np.full((v, h), "^")
        print("마운틴 던전 맵이 소환 되었습니다.")
        print(A)
        return A

    def create_monsters(self, map):
        self.map = map
        input("던전 보스몹을 소환하려면 아무 키를 누르세요.")
        print("던전 보스몹들을 소환합니다. 숫자 7, 8, 9가 보스몹들입니다.")
        self.map[10,2] = 6
        self.map[11,2] = 6
        self.map[12,2] = 6
        self.map[10,3] = 6
        self.map[11,3] = 6
        self.map[12,3] = 6
        self.map[10,4] = 6
        self.map[11,4] = 6
        self.map[12,4] = 6
        self.map[10,5] = 6
        self.map[11,5] = 6
        self.map[12,5] = 6
        self.map[15,6] = 8
        self.map[16,6] = 8
        self.map[17,6] = 8
        self.map[15,7] = 8
        self.map[16,7] = 8
        self.map[17,7] = 8
        self.map[15,8] = 8
        self.map[16,8] = 8
        self.map[17,8] = 8
        self.map[19,9] = 9
        print(self.map)
        return self.map

    def create_user(self, map):
        self.map = map
        input("유저 캐릭터를 소환하려면 아무 키를 누르세요.")
        print("유저 캐릭터를 소환합니다. 숫자 1이 유처 캐릭터입니다.")
        self.map[0, 0] = 1
        print(self.map)
        return self.map





# Map().print_map()

# A = Map().create_monsters(Map.create_map())
# print(A)

# input("마운틴 던전을 소환하려면 m을 입력하세요 ----> ")
# print("마운틴 던전을 소환합니다.")
# A = np.full((30,10), "^")
# print(A)
# print("--------------------------")
# input("던전 보스몹들을 소환하려면 d를 입력하세요 ----> ")

# print(A)
# print("--------------------------")
# input("유저 캐릭터를 만드려면 c를 입력하세요 ----> ")
# print("캐릭터를 소환합니다. 숫자 1이 유저 캐릭터입니다.")
# A[0,0] = 1
# print(A)
# print("--------------------------")


class Move:
    def __init__(self, map):
        self.map = map


    def move(self):
        a = input("움직일 방향의 번호를 입력하세요. 1.w 2.s 3.a 4.d ----> ")
        if a == "w":
            print("위로 한칸 움직였습니다.")
            # print("Moving player 1 to the right - step 1: find 2")
            a = np.where(self.map == "1")
            # print(a)
            # print("--------------------------")
            # print("Moving player 1 to the right - step 2: Change 2 to 1")
            self.map[a] = "^"
            # print(A)
            # print("--------------------------")
            # print("Moving player 1 to the right - step 3: Change a value on the right to 2")
            # https://moonbooks.org/Articles/How-to-extract-a-small-matrix-by-selecting-neighbors-for-a-given-index-using-numpy-in-python-/
            up = (a[0]-1, a[1])
            self.map[up] = 1
            print(self.map)

        elif a == "s":
            print("아래로 한칸 움직였습니다.")
            # print("Moving player 1 to the right - step 1: find 2")
            a = np.where(self.map == "1")
            # print(a)
            # print("--------------------------")
            # print("Moving player 1 to the right - step 2: Change 2 to 1")
            self.map[a] = "^"
            # print(A)
            # print("--------------------------")
            # print("Moving player 1 to the right - step 3: Change a value on the right to 2")
            # https://moonbooks.org/Articles/How-to-extract-a-small-matrix-by-selecting-neighbors-for-a-given-index-using-numpy-in-python-/
            down = (a[0]+1, a[1])
            self.map[down] = 1
            print(self.map)

        elif a == "a":
            print("왼쪽으로 한칸 움직였습니다.")
            # print("Moving player 1 to the right - step 1: find 2")
            a = np.where(self.map == "1")
            # print(a)
            # print("--------------------------")
            # print("Moving player 1 to the right - step 2: Change 2 to 1")
            self.map[a] = "^"
            # print(A)
            # print("--------------------------")
            # print("Moving player 1 to the right - step 3: Change a value on the right to 2")
            # https://moonbooks.org/Articles/How-to-extract-a-small-matrix-by-selecting-neighbors-for-a-given-index-using-numpy-in-python-/
            left = (a[0], a[1]-1)
            self.map[left] = 1
            print(self.map)

        elif a == "d":
            print("오른쪽으로 한칸 움직였습니다.")
            # print("Moving player 1 to the right - step 1: find 2")
            a = np.where(self.map == "1")
            # print(a)
            # print("--------------------------")
            # print("Moving player 1 to the right - step 2: Change 2 to 1")
            self.map[a] = "^"
            # print(A)
            # print("--------------------------")
            # print("Moving player 1 to the right - step 3: Change a value on the right to 2")
            # https://moonbooks.org/Articles/How-to-extract-a-small-matrix-by-selecting-neighbors-for-a-given-index-using-numpy-in-python-/
            right = (a[0], a[1]+1)
            self.map[right] = 1
            print(self.map)

        else:
            print("유효하지 않은 움직임입니다. 다시 입력해주세요.")
            print(self.map)
            Move(self.map).move()


# 캐릭터 생성
jason = Character("Jason", "swordsman", 1, 1, "Vertical slash", "Side slash", "Diagonal slash")
ben = Character("Ben", "swordsman", 1, 1, "Vertical slash", "Side slash", "Diagonal slash")
boss1 = Character("Boss", "swordsman", 2, 2, "Vertical slash", "Side slash", "Diagonal slash")
# 게임 시작
A = Map().create_user(Map().create_monsters(Map().create_map()))
a = np.where(A != "^")
b = (np.delete(a[0],0), np.delete(a[1],0))
while True:
    Move(A).move()
    if "1" in A[b]:
        RepeatBattles(ben, jason, Battle(ben, jason)).repeat_three()
        c = np.where(A != "^")
        b = (np.delete(c[0], 0), np.delete(c[1], 0))
        print(A)
