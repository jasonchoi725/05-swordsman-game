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
