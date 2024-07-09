import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
zero = []

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zero.append([i, j])


def checkHorizontal(x, num):
    for i in range(9):
        if board[x][i] == num:
            return False
    return True


def checkVertical(y, num):
    for i in range(9):
        if board[i][y] == num:
            return False
    return True


def checkRect(x, y, num):
    nx = x // 3 * 3
    ny = y // 3 * 3

    for i in range(3):
        for j in range(3):
            if board[nx + i][ny + j] == num:
                return False
    return True


def dfs(idx):
    if idx == len(zero):
        for i in range(9):
            print(*board[i])
        exit(0)

    for i in range(1, 10):  # 1부터 9까지 존재하는지 확인
        x = zero[idx][0]
        y = zero[idx][1]

        if checkHorizontal(x, i) and checkVertical(y, i) and checkRect(x, y, i):
            board[x][y] = i
            dfs(idx + 1)
            board[x][y] = 0


dfs(0)
