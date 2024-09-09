import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(x, y):
    for d in range(4):
        nx = x + dir[d][0]
        ny = y + dir[d][1]

        if 0 <= nx < R and 0 <= ny < C:
            if board[nx][ny] == "S":  # 바로 옆이 양이면 울타리 못침
                return False
            if board[nx][ny] == ".":
                board[nx][ny] = "D"
    return True


for i in range(R):
    for j in range(C):
        flag = True
        if board[i][j] == "W":
            flag = bfs(i, j)

            if not flag:
                print(0)
                break

if flag:
    print(1)
    for i in board:
        print(''.join(i))
