import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
calCnt = {-1: 0, 0: 0, 1: 0}


def sameNum(arr):
    num = arr[0][0]
    for row in arr:
        for element in row:
            if element != num:
                return False
    return True


def splitBoard(arr):
    if sameNum(arr):
        calCnt[arr[0][0]] += 1
        return

    length = len(arr)
    sub_size = length // 3

    for i in range(0, length, sub_size):
        for j in range(0, length, sub_size):
            rows = []
            for c in range(i, i + sub_size):
                rows.append(arr[c][j: j + sub_size])

            splitBoard(rows)


if sameNum(board):
    calCnt[board[0][0]] += 1
else:
    splitBoard(board)

print(calCnt[-1])
print(calCnt[0])
print(calCnt[1])
print("\n")

# ------------- 분할 정복 ------------

def dfs(x, y, z):
    global answer
    target = board[x][y]

    for i in range(x, x + z):
        for j in range(y, y + z):
            if board[i][j] != target:  # 첫번째 값과 다르다면 분리할 것임
                for k in range(3):  # 서브 배열을 3X3으로 분할하기 위해
                    for l in range(3):
                        dfs(x + k * z // 3, y + l * z // 3, z // 3)
                return

    if target == -1:
        answer[0] += 1
    elif target == 0:
        answer[1] += 1
    else:
        answer[2] += 1


answer = [0, 0, 0]
dfs(0, 0, N)
print(answer[0], answer[1], answer[2], sep="\n")
