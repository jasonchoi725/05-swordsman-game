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
