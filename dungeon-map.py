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
